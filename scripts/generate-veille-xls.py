#!/usr/bin/env python3
"""Génère veille-presentation.xls (SpreadsheetML) — résumé de veille.md."""

from pathlib import Path
import xml.sax.saxutils as xml

OUT = Path(__file__).resolve().parent.parent / "veille-presentation.xls"


def esc(text):
    return xml.escape(str(text))


def row(cells, style=None):
    parts = ['<Row>']
    for c in cells:
        t = "String"
        val = c
        if isinstance(c, (int, float)):
            t = "Number"
            val = c
        st = f' ss:StyleID="{style}"' if style else ""
        parts.append(f'<Cell{st}><Data ss:Type="{t}">{esc(val)}</Data></Cell>')
    parts.append("</Row>")
    return "".join(parts)


def sheet(name, rows):
    body = "\n".join(rows)
    return f"""<Worksheet ss:Name="{esc(name)}">
<Table>
{body}
</Table>
</Worksheet>"""


def header_row(cells):
    return row(cells, "Header")


def title_block(title, subtitle=""):
    rows = [
        row([title], "Title"),
    ]
    if subtitle:
        rows.append(row([subtitle], "Subtitle"))
    rows.append(row([]))
    return rows


rows_presentation = title_block(
    "Veille technologique — CATASTERRE",
    "Résumé présentation · juin 2026 · Projet 10 OpenClassrooms",
) + [
    header_row(["Section", "Contenu"]),
    row(["Objectif", "Constats sectoriels pour la prise de décision — pas de solution imposée"]),
    row(["Application", "Visualisation catastrophes naturelles · imagerie satellite · immobilier"]),
    row(["4 axes", "Architecture · Performance · Dette technique · Bonnes pratiques Full-Stack"]),
    row(["Méthode", "Tendances 2025-2026 croisées avec backlog 11 US / 75 SP"]),
    row(["Équipe", "Dimitry (front) · Rachida (DevOps/back) · Jorge (UX) · Expert (agile)"]),
    row(["Stack", "Angular · Spring Boot/Security/Data · MySQL · Docker · GitHub Actions · k8s/AWS"]),
    row([]),
    header_row(["Contrainte", "Constat"]),
    row(["Maturité", "Brownfield < 1 an — lenteurs, erreurs, instabilités"]),
    row(["Roadmap", "Étape A Docker → Étape B microservices"]),
    row(["Sprint 1", "Stabilisation UX + Docker (12 SP ajustés)"]),
]

rows_archi = title_block("Axe 1 — Architectures applicatives") + [
    header_row(["Thème", "Constat", "Lien CATASTERRE", "Question clé"]),
    row([
        "Monolithe modulaire",
        "Bounded contexts internes avant extraction réseau — consensus 2025-2026",
        "Étape A Docker · US-6 Sprint 4+",
        "Structurer modules images/risques/auth/export avant 1er service ?",
    ]),
    row([
        "Strangler Fig",
        "Migration incrémentale shadow → canary → cutover",
        "Étape B · US-6 (13 SP)",
        "Premier contexte : RiskCalculation ou ImageIngestion ?",
    ]),
    row([
        "Anti-Corruption Layer",
        "Traduit modèles legacy vers nouveaux services",
        "App peu documentée — risque fuite dette",
        "ACL à la frontière API ou couche service ?",
    ]),
    row([
        "Géo cloud-native",
        "COG · PMTiles/MVT · STAC — scaling élastique CDN",
        "US-9 · objectif zones inondation côtières",
        "Format actuel GeoJSON vs tuiles ? Migration Sprint 4+ ?",
    ]),
    row([
        "OpenAPI contract-first",
        "Sync front Angular / back Spring · tests de contrat",
        "US-2 erreurs intégration",
        "OpenAPI dès Sprint 2 ou après S1 ?",
    ]),
    row([]),
    header_row(["Bounded context", "Responsabilité", "US"]),
    row(["ImageIngestion", "Images satellite", "—"]),
    row(["RiskCalculation", "Calcul risques inondation", "US-9"]),
    row(["UserAccess", "Auth", "—"]),
    row(["Export", "Export CSV/PDF/GeoJSON", "US-11"]),
    row(["Presentation", "UX · carte · A11Y", "US-1, US-2, US-3, US-10"]),
]

rows_perf = title_block("Axe 2 — Performances") + [
    header_row(["Couche", "Thème", "Constat", "Lien backlog"]),
    row(["Front Angular", "Zoneless + Signals", "Angular 20.2+ · moins de change detection", "US-1, US-10"]),
    row(["Front Angular", "OnPush + @defer", "Composants lourds (carte) à la demande", "Lenteurs client"]),
    row(["Front Angular", "NgOptimizedImage", "Lazy-load images satellite · réduit CLS", "Imagerie"]),
    row(["Back Spring", "N+1 / OSIV", "open-in-view=false · JOIN FETCH · DTO", "US-9"]),
    row(["Back Spring", "Cache Caffeine/Redis", "Données stables uniquement", "US9-T2"]),
    row(["Back Spring", "Virtual threads Java 21", "Débit I/O JDBC", "Post-Docker"]),
    row(["Back Spring", "Batch JDBC", "Écritures groupées export", "US-11"]),
    row(["Géospatial", "GeoJSON vs tuiles", "700k polygones = 350-500 Mo · tuiles ÷10-25", "Cause probable lenteurs"]),
    row(["Géospatial", "Index spatial MySQL", "Sans index = full scan", "US9-T2"]),
    row(["Géospatial", "CDN tuiles", "Latence < 50 ms", "Post-Docker AWS"]),
    row([]),
    header_row(["Métrique", "Seuil indicatif", "Outil"]),
    row(["LCP", "≤ 2,5 s", "Lighthouse"]),
    row(["CLS", "≤ 0,1", "Lighthouse"]),
    row(["INP", "≤ 200 ms", "Lighthouse"]),
    row(["API p95", "À définir après profiling", "Actuator / Micrometer"]),
    row(["Principe", "Mesurer avant d'optimiser", "US9-T1 profiling"]),
]

rows_dette = title_block("Axe 3 — Dette technique") + [
    header_row(["Principe", "Constat", "Application"]),
    row(["Pas de big-bang", "Réécriture = risque downtime/budget", "Approche incrémentale sprints 1-6"]),
    row(["Audit structural", "Analyse statique réduit périmètre ~30 %", "Avant US-6"]),
    row(["TIME / MoSCoW", "Tolerate · Invest · Migrate · Eliminate", "US-4 Won't · US-9/11 Could"]),
    row(["Parallel run", "Legacy autoritaire jusqu'à validation env test", "US-8"]),
    row(["Dette dans backlog", "Stories dédiées pas seulement bugs", "US-1/2 UX · US-7 process"]),
    row([]),
    header_row(["Type dette", "User Stories", "Priorité sprint"]),
    row(["UX (styles, erreurs, A11Y)", "US-1, US-2, US-3", "Haute · S1-S2"]),
    row(["Process (CI/CD, env test)", "US-7, US-8", "Haute · S2-S3"]),
    row(["Deploy (containerisation)", "US-5", "Haute · S1"]),
    row(["Structurelle (monolithe)", "US-6", "Moyenne · S4+"]),
    row(["Métier (perf, export)", "US-9, US-11", "Luxueuse · S4+"]),
    row(["Reportée (thème)", "US-4", "Basse · reporté"]),
    row([]),
    header_row(["Indicateur suivi", "Objectif"]),
    row(["Ratio bugs / features", "Par sprint"]),
    row(["Couverture tests", "Progression via US-7-T2 + formation"]),
    row(["Temps build/deploy", "Réduction continue"]),
    row(["Requêtes SQL / endpoint", "Après audit Hibernate"]),
    row(["Vélocité vs engagement", "12 SP S1 · 14 SP cible S2"]),
]

rows_fullstack = title_block("Axe 4 — Bonnes pratiques Full-Stack") + [
    header_row(["Domaine", "Pratique", "Lien sprint / US"]),
    row(["DevOps", "Docker multi-stage", "US-5"]),
    row(["DevOps", "docker-compose local", "US5-T3"]),
    row(["DevOps", "GitHub Actions lint + tests", "US-7"]),
    row(["DevOps", "Trivy + Semgrep en CI", "US-7-T2"]),
    row(["DevOps", "Flyway/Liquibase migrations", "À évaluer"]),
    row(["DevOps", "Envs dev → staging → prod", "US-8"]),
    row(["DevOps", "Smoke tests post-deploy", "US8-T4"]),
    row(["Qualité", "Composant erreur unifié + mapping HTTP", "US-2"]),
    row(["Qualité", "WCAG AA · clavier · ARIA", "US-3"]),
    row(["Qualité", "Vitest/Jasmine front · JUnit/Testcontainers back", "US-7-T2 · formation tests"]),
    row(["Qualité", "Revue UX Jorge formalisée", "US1-T4"]),
    row(["Agile", "DoD partagée · vélocité ajustée", "backlog.md · comite-projet.md"]),
    row(["Agile", "Veille en rétrospective", "1 tendance / sprint"]),
]

rows_matrice = title_block("Synthèse — Matrice décisionnelle") + [
    header_row(["US", "Titre", "Architecture", "Performance", "Dette", "Full-Stack"]),
    row(["US-1", "Style CSS", "—", "OnPush, NgOptimizedImage", "Dette UX", "Lint, revue Jorge"]),
    row(["US-2", "Messages erreur", "Contrat API", "—", "Dette UX", "Composant + mapping HTTP"]),
    row(["US-3", "Accessibilité", "—", "—", "Dette UX", "WCAG AA"]),
    row(["US-4", "Nouveau thème", "—", "—", "Reportée", "Angular theming"]),
    row(["US-5", "Docker", "Conteneurisation", "—", "Dette deploy", "Multi-stage, compose"]),
    row(["US-6", "Microservices", "Strangler, ACL", "—", "Dette structurelle", "OpenAPI, contract tests"]),
    row(["US-7", "CI/CD", "—", "Anti-régression", "Dette process", "GH Actions, scans"]),
    row(["US-8", "Env. test", "—", "—", "Parallel run", "Profils Spring, smoke"]),
    row(["US-9", "Risque inondation", "RiskCalculation", "JPA, tuiles, index", "—", "Profiling d'abord"]),
    row(["US-10", "Compatibilité nav.", "—", "@defer, polyfills", "—", "Matrice navigateurs"]),
    row(["US-11", "Export données", "Export", "Batch JDBC", "Luxueuse", "API Spring + UI"]),
]

rows_sprints = title_block("Veille × Sprints") + [
    header_row(["Sprint", "SP", "US prioritaires", "Axes veille dominants"]),
    row(["Sprint 1", "12", "US-1, US-2, US-5", "Perf front · Docker · Dette UX · FORM-T0"]),
    row(["Sprint 2", "12-14", "US-3, US-7, TEST-T1/T2", "A11Y · CI/CD · Formation tests"]),
    row(["Sprint 3", "~16", "US-8, US-10, TEST-T3", "Env test · Navigateurs · Cypress"]),
    row(["Sprint 4+", "—", "US-6, US-9, US-11", "Strangler · Perf géo · Export"]),
    row([]),
    header_row(["Question comité", ""]),
    row(["Audit code + perf + données géo avant S3 ?", ""]),
    row(["Monolithe modulaire prérequis explicite US-6 ?", ""]),
    row(["Indicateurs dette suivis en rétrospective ?", ""]),
]

rows_biblio = title_block("Bibliographie (sélection)") + [
    header_row(["Axe", "Source", "URL"]),
    row(["Architecture", "Monolith to Microservices 2026", "knowledgelib.io"]),
    row(["Architecture", "Strangler Fig Pattern", "learn.microsoft.com"]),
    row(["Architecture", "Modern WebGIS Architecture", "offnadir-delta.com"]),
    row(["Performance", "Spring Boot JPA Performance 2026", "blog.devops-monk.com"]),
    row(["Performance", "700K polygons satellite maps", "agfianf.github.io"]),
    row(["Performance", "Angular v21 Zoneless", "zyraui.dev"]),
    row(["Dette", "Modernizing Legacy Software 2025", "javra.com"]),
    row(["Full-Stack", "Angular + Spring Boot Guide", "innovirtuoso.com"]),
    row(["Full-Stack", "DevSecOps Spring+Angular", "github.com/georgesfk/secspringterracloud"]),
    row([]),
    row(["Document source", "veille.md · projet10 · juin 2026"]),
]

styles = """
<Styles>
  <Style ss:ID="Default"><Alignment ss:Vertical="Top" ss:WrapText="1"/></Style>
  <Style ss:ID="Title"><Font ss:Bold="1" ss:Size="16"/><Alignment ss:Horizontal="Left"/></Style>
  <Style ss:ID="Subtitle"><Font ss:Italic="1" ss:Size="11" ss:Color="#666666"/></Style>
  <Style ss:ID="Header"><Font ss:Bold="1" ss:Color="#FFFFFF"/>
    <Interior ss:Color="#1D76DB" ss:Pattern="Solid"/>
    <Alignment ss:WrapText="1"/></Style>
</Styles>
"""

workbook = f"""<?xml version="1.0" encoding="UTF-8"?>
<?mso-application progid="Excel.Sheet"?>
<Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet">
{styles}
{sheet("Presentation", rows_presentation)}
{sheet("1-Architecture", rows_archi)}
{sheet("2-Performance", rows_perf)}
{sheet("3-Dette", rows_dette)}
{sheet("4-Full-Stack", rows_fullstack)}
{sheet("Matrice-US", rows_matrice)}
{sheet("Sprints", rows_sprints)}
{sheet("Bibliographie", rows_biblio)}
</Workbook>
"""

OUT.write_text(workbook, encoding="utf-8")
print(f"Created: {OUT} ({OUT.stat().st_size} bytes)")
