#!/usr/bin/env python3
"""Import or sync backlog items from CSV into GitHub issues and Project."""

import argparse
import csv
import json
import re
import subprocess
import sys
import time
from pathlib import Path

REPO = "laurentcoufinal/projet10"
OWNER = "laurentcoufinal"
PROJECT_TITLE = "Projet10 backlog"
SCRIPT_DIR = Path(__file__).resolve().parent
CSV_PATH = SCRIPT_DIR / "backlog-items.csv"

SPRINT_LABELS = {
    "Sprint 1": "sprint:1",
    "Sprint 2": "sprint:2",
    "Sprint 3": "sprint:3",
    "Sprint 4+": "sprint:4plus",
    "Reporté": "sprint:reporte",
}

PRIORITY_LABELS = {
    "Haute": "priority:haute",
    "Moyenne": "priority:moyenne",
    "Basse": "priority:basse",
    "Luxueuse": "priority:luxueuse",
}

LABEL_COLORS = {
    "user-story": "0E8A16",
    "task": "FEF2C0",
    "formation": "C968FF",
    "priority:haute": "B60205",
    "priority:moyenne": "FBCA04",
    "priority:basse": "C5DEF5",
    "priority:luxueuse": "D4C5F9",
    "sprint:1": "1D76DB",
    "sprint:2": "1D76DB",
    "sprint:3": "1D76DB",
    "sprint:4plus": "1D76DB",
    "sprint:reporte": "EDEDED",
    "assignee:dimitry": "BFD4F2",
    "assignee:rachida": "BFD4F2",
    "assignee:jorge": "BFD4F2",
    "assignee:expert": "BFD4F2",
}

MANAGED_LABEL_PREFIXES = ("sprint:", "sp:", "assignee:", "priority:")
TYPE_LABELS = {"user_story": "user-story", "task": "task", "formation": "formation"}


def run(cmd, check=True):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError(
            f"Command failed: {' '.join(cmd)}\nstdout: {result.stdout}\nstderr: {result.stderr}"
        )
    return result


def ensure_label(name, color):
    result = run(
        ["gh", "label", "list", "--repo", REPO, "--search", name, "--limit", "10"],
        check=False,
    )
    if result.returncode == 0 and any(line.startswith(f"{name}\t") for line in result.stdout.splitlines()):
        return
    create = run(
        ["gh", "label", "create", name, "--repo", REPO, "--color", color, "--force"],
        check=False,
    )
    if create.returncode != 0 and "already exists" not in (create.stderr or "").lower():
        raise RuntimeError(f"Failed to create label {name}: {create.stderr}")


def ensure_labels():
    for sp in range(0, 14):
        ensure_label(f"sp:{sp}", "0052CC")
    for name, color in LABEL_COLORS.items():
        ensure_label(name, color)


def parse_assignees(assignee_field):
    mapping = {
        "dimitry": "assignee:dimitry",
        "rachida": "assignee:rachida",
        "jorge": "assignee:jorge",
        "expert": "assignee:expert",
    }
    labels = []
    lower = assignee_field.lower()
    for key, label in mapping.items():
        if key in lower:
            labels.append(label)
    return labels


def sprint_label(sprint):
    return SPRINT_LABELS.get(sprint, "")


def find_existing_issue(item_id):
    query = f"repo:{REPO} [{item_id}] in:title"
    result = run(
        ["gh", "issue", "list", "--repo", REPO, "--search", query, "--json", "number,url,title,labels", "--limit", "10"],
        check=False,
    )
    if result.returncode != 0:
        return None
    issues = json.loads(result.stdout or "[]")
    prefix = f"[{item_id}]"
    for issue in issues:
        if issue["title"].startswith(prefix):
            if "url" not in issue:
                issue["url"] = f"https://github.com/{REPO}/issues/{issue['number']}"
            return issue
    return None


def build_labels(row):
    labels = []
    item_type = row["type"]
    type_label = TYPE_LABELS.get(item_type)
    if type_label:
        labels.append(type_label)

    if item_type == "user_story" and row["priority"]:
        pl = PRIORITY_LABELS.get(row["priority"])
        if pl:
            labels.append(pl)
    elif item_type == "formation":
        pass  # type_label "formation" déjà ajouté via TYPE_LABELS

    sl = sprint_label(row["sprint"])
    if sl:
        labels.append(sl)

    if row["sp"] != "":
        labels.append(f"sp:{row['sp']}")

    labels.extend(parse_assignees(row["assignee"]))
    return labels


def source_links(row):
    if row["type"] == "formation":
        return "\n---\nSources: [formation.md](../formation.md) · [comite-projet.md](../comite-projet.md)"
    return "\n---\nSource: [backlog.md](../backlog.md)"


def build_body(row, parent_issue=None):
    lines = [
        f"**ID :** `{row['id']}`",
        f"**Type :** {row['type']}",
        f"**Assigné :** {row['assignee']}",
        f"**Story Points :** {row['sp'] if row['sp'] != '' else '0 (hors vélocité)'}",
        f"**Sprint :** {row['sprint']}",
    ]
    if row["parent"]:
        lines.append(f"**Parent :** {row['parent']}")
    if row["priority"]:
        lines.append(f"**Priorité :** {row['priority']}")
    if row["criteria"]:
        lines.append(f"\n## Critère de succès\n{row['criteria']}")
    if parent_issue:
        lines.append(f"\nParent issue: #{parent_issue['number']}")
    lines.append(source_links(row))
    return "\n".join(lines)


def get_issue_labels(number):
    result = run(
        ["gh", "issue", "view", str(number), "--repo", REPO, "--json", "labels"],
        check=False,
    )
    if result.returncode != 0:
        return []
    data = json.loads(result.stdout or "{}")
    return [lbl["name"] for lbl in data.get("labels", [])]


def sync_issue_labels(number, desired_labels):
    current = get_issue_labels(number)
    to_remove = [
        lbl for lbl in current
        if lbl.startswith(MANAGED_LABEL_PREFIXES) or lbl in TYPE_LABELS.values()
    ]
    for lbl in to_remove:
        if lbl not in desired_labels:
            run(
                ["gh", "issue", "edit", str(number), "--repo", REPO, "--remove-label", lbl],
                check=False,
            )
    for lbl in desired_labels:
        if lbl not in current:
            run(
                ["gh", "issue", "edit", str(number), "--repo", REPO, "--add-label", lbl],
                check=False,
            )


def update_issue(row, issue_number, parent_number=None):
    title = f"[{row['id']}] {row['title']}"
    body = build_body(row, {"number": parent_number} if parent_number else None)
    run(
        ["gh", "issue", "edit", str(issue_number), "--repo", REPO, "--title", title, "--body", body],
        check=False,
    )
    sync_issue_labels(issue_number, build_labels(row))
    print(f"  updated: {row['id']} -> #{issue_number}")


def create_issue(row, parent_number=None):
    existing = find_existing_issue(row["id"])
    if existing:
        parent_for_update = parent_number
        update_issue(row, existing["number"], parent_for_update)
        return existing

    title = f"[{row['id']}] {row['title']}"
    labels = build_labels(row)
    body = build_body(row, {"number": parent_number} if parent_number else None)

    cmd = [
        "gh", "issue", "create",
        "--repo", REPO,
        "--title", title,
        "--body", body,
    ]
    for label in labels:
        cmd.extend(["--label", label])

    if parent_number and row["type"] in ("task", "formation"):
        cmd.extend(["--parent", str(parent_number)])

    result = run(cmd, check=False)
    if result.returncode != 0 and parent_number:
        body = build_body(row, {"number": parent_number})
        cmd = [
            "gh", "issue", "create",
            "--repo", REPO,
            "--title", title,
            "--body", body,
        ]
        for label in labels:
            cmd.extend(["--label", label])
        result = run(cmd)

    url = result.stdout.strip()
    number = int(url.rstrip("/").split("/")[-1])
    issue = {"number": number, "url": url, "title": title}
    print(f"  created: {row['id']} -> #{issue['number']}")
    time.sleep(0.3)
    return issue


def sync_issue(row, parent_number=None):
    existing = find_existing_issue(row["id"])
    if existing:
        update_issue(row, existing["number"], parent_number)
        return existing
    return create_issue(row, parent_number)


def get_project_number():
    result = run(
        ["gh", "project", "list", "--owner", OWNER, "--format", "json", "--limit", "50"],
        check=False,
    )
    if result.returncode != 0:
        return None
    data = json.loads(result.stdout or "{}")
    projects = data.get("projects", data if isinstance(data, list) else [])
    for p in projects:
        if p.get("title") == PROJECT_TITLE:
            return p.get("number")
    return None


def create_project():
    result = run(
        ["gh", "project", "create", "--owner", OWNER, "--title", PROJECT_TITLE, "--format", "json"],
        check=False,
    )
    if result.returncode != 0:
        return None
    data = json.loads(result.stdout)
    return data.get("number")


def load_items():
    items = []
    with CSV_PATH.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(row)
    return items


def sum_sp_for_sprint(sprint_label_name):
    items = load_items()
    total = 0
    for row in items:
        if row["type"] not in ("task",) or row["sprint"] != sprint_label_name:
            continue
        try:
            sp = int(row["sp"])
        except ValueError:
            sp = 0
        if sp > 0:
            total += sp
    return total


def main():
    parser = argparse.ArgumentParser(description="Import/sync backlog to GitHub")
    parser.add_argument("--sync", action="store_true", help="Update existing issues and create missing ones")
    args = parser.parse_args()

    if not CSV_PATH.exists():
        print(f"Missing {CSV_PATH}", file=sys.stderr)
        sys.exit(1)

    print("==> Ensuring labels...")
    ensure_labels()

    items = load_items()
    user_stories = [i for i in items if i["type"] == "user_story"]
    formations = [i for i in items if i["type"] == "formation"]
    tasks = [i for i in items if i["type"] == "task"]

    parent_numbers = {}
    upsert = sync_issue if args.sync else create_issue

    print(f"==> {'Syncing' if args.sync else 'Creating'} {len(user_stories)} user stories...")
    for row in user_stories:
        issue = upsert(row)
        parent_numbers[row["id"]] = issue["number"]

    print(f"==> {'Syncing' if args.sync else 'Creating'} {len(formations)} formation modules...")
    for row in formations:
        parent_num = parent_numbers.get(row["parent"]) if row["parent"] else None
        upsert(row, parent_number=parent_num)

    print(f"==> {'Syncing' if args.sync else 'Creating'} {len(tasks)} tasks...")
    for row in tasks:
        parent_num = parent_numbers.get(row["parent"]) if row["parent"] else None
        upsert(row, parent_number=parent_num)

    all_issues = []
    for row in items:
        issue = find_existing_issue(row["id"])
        if issue:
            all_issues.append(issue)

    print("==> Adding issues to GitHub Project...")
    project_number = get_project_number()
    if not project_number:
        print("  Project not found, creating...")
        project_number = create_project()

    if project_number:
        added = 0
        for issue in all_issues:
            url = issue.get("url") or f"https://github.com/{REPO}/issues/{issue['number']}"
            result = run(
                [
                    "gh", "project", "item-add", str(project_number),
                    "--owner", OWNER,
                    "--url", url,
                ],
                check=False,
            )
            if result.returncode == 0:
                added += 1
            time.sleep(0.15)
        print(f"  Added {added}/{len(all_issues)} items to project #{project_number}")
        print(f"  Project URL: https://github.com/users/{OWNER}/projects/{project_number}")
    else:
        print("  WARNING: Could not access GitHub Projects.")
        print(f"  Issues in repo: https://github.com/{REPO}/issues")

    s1_sp = sum_sp_for_sprint("Sprint 1")
    s2_sp = sum_sp_for_sprint("Sprint 2")
    print(f"\nDone. {len(all_issues)} issues in {REPO}.")
    print(f"Vélocité CSV — Sprint 1: {s1_sp} SP dev | Sprint 2: {s2_sp} SP dev")


if __name__ == "__main__":
    main()
