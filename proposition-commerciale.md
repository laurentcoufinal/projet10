# Projet évolution d'application — Proposition commerciale CATASTERRE

> **Date :** juin 2026  
> **Source d'analyse :** [comparaison_projets_2.md](comparaison_projets_2.md)  
> **Documents de référence :** [projet.md](projet.md) · [backlog.md](backlog.md) · [risque.md](risque.md) · [veille.md](veille.md) · [formation.md](formation.md)

Application **brownfield** (< 1 an) en évolution incrémentale. Les 3 scénarios contractuels intègrent **systématiquement** le plan formation tests (contrainte non négociable — blocage Daily Scrum Rachida, risque RS-11). Budget cible : **78–118 k€ HT**.

## 1. Contexte

### 1.1 Contexte global

L’entreprise développe une application web utilisée par des notaires et agences immobilières afin d’évaluer les risques liés à la vente de biens immobiliers (zones inondables, risques sismiques, périmètres nucléaires, etc.).

Face à l’augmentation du nombre d’utilisateurs et à l’évolution des besoins métier, l’application montre aujourd’hui ses limites techniques et fonctionnelles :

complexité croissante du code,
difficultés à faire évoluer l’architecture,
manque de visibilité sur la roadmap technique,
coordination perfectible entre les équipes front-end, back-end et UX.
La direction a décidé de lancer un projet structurant de développement et d’évolution de l’application, avec pour objectif produit de :

améliorer l'expérience utilisateur,
garantir la disponibilité, et améliorer la maintenabilité et l’évolutivité du produit,
fiabiliser l’organisation du développement.

### 1.2 Fonctionnalités métier

#### Domaines fonctionnels

**1. Consultation et visualisation cartographique**

- Affichage des **zones côtières inondables** sur la carte (US9-T3)
- Pages principales avec rendu visuel cohérent — polices, typographie, espacements (US-1, US1-T1 à T3)
- **Compatibilité multi-navigateurs** (Chrome, Firefox, Safari, Edge) pour garantir l'accès aux professionnels (US-10, US10-T1 à T3)

**2. Recherche et navigation**

- **Formulaire de recherche** de propriétés et parcours résultats (US3-T1 — audit des parcours critiques)
- Navigation clavier, focus visible et attributs ARIA pour utilisateurs à accessibilité réduite (US3-T2, US3-T3)

**3. Évaluation des risques naturels**

- **Calcul du risque d'inondation** — fonctionnalité cœur de CATASTERRE (US-9)
- Optimisation des performances de calcul et de traitement back-end (US9-T1, US9-T2)
- **Validation métier** sur un jeu de données de référence — 10 cas de test (US9-T4)

**4. Export et exploitation des données**

- Export des données au format **CSV, PDF ou GeoJSON** (US-11, US11-T1)
- Endpoint d'export back-end et **téléchargement depuis l'interface** Angular (US11-T2, US11-T3)

**5. Qualité de l'expérience utilisateur**

- Messages d'erreur **clairs et compréhensibles** pour les 5 cas les plus fréquents (US-2, US2-T2/T3)
- **Accessibilité WCAG AA** : contrastes, labels ARIA, navigation clavier (US-3, US3-T3/T4)
- Thème alternatif *(hors priorité — reporté, dark theme déjà en place)* (US-4)

**6. Évolutions d'architecture** *(support indirect des fonctionnalités métier)*

- Disponibilité et scalabilité via containerisation Docker (US-5)
- Fiabilisation des livraisons — CI/CD et environnement de test isolé (US-7, US-8)
- Modularisation future par domaines métier : **images, risques, auth, export** (US6-T1/T2)

> **Périmètre contractuel :** US-4 (thème) reportée. US-5, US-6, US-7 et US-8 sont des prérequis techniques pour fiabiliser et maintenir les fonctionnalités métier — leur couverture varie selon la proposition (P1/P2/P3), voir §2.1.

---

## 2. Réalisation du projet

Le projet CATASTERRE vise l'évolution d'une application web existante (visualisation de catastrophes naturelles via imagerie satellite) en mode Scrum, avec des sprints de 2 semaines et une équipe de 4 personnes à 40 h/semaine.

### 2.1 Définition des tâches techniques

Les travaux sont organisés en 4 epics, alignées sur le cahier des charges :

**Epic A — Stabilisation UX / front-end** (Dimitry, Jorge)

- Correction des erreurs de styles (fontes, messages d'erreur)
- Amélioration du parcours utilisateur et de l'accessibilité
- Audit UX des pages critiques

**Epic B — Performance et back-end** (Rachida)

- Optimisation Spring Boot (performance, sécurité Spring Data / Security)
- Correction de bugs critiques back-end

**Epic C — DevOps et disponibilité** (Rachida)

- Containerisation Docker (Dockerfile, docker-compose)
- Pipeline CI/CD (GitHub Actions)
- Environnement de tests séparé de la production

**Epic D — Pilotage agile et qualité** (Expert)

- Mise en place des pratiques Scrum
- Revue technique, coordination inter-équipes
- Suivi vélocité et amélioration continue

Phase ultérieure (hors périmètre Sprint 1-3 selon proposition) : découpage en microservices.

#### Périmètre par proposition — couverture User Stories

| US | Titre | Priorité | SP | P1 | P2 | P3 |
|----|-------|----------|-----|:--:|:--:|:--:|
| US-1 | Style CSS | Haute | 5 | oui | oui | oui |
| US-2 | Messages d'erreur | Haute | 5 | oui | oui | oui |
| US-3 | Accessibilité (A11Y) | Haute | 8 | oui | oui | oui |
| US-4 | Nouveau thème | Basse | 5 | — | — | oui |
| US-5 | Encapsuler (Docker) | Haute | 5 | oui | oui | oui |
| US-6 | Micro-services | Moyenne | 13 | — | prép. (T1/T2) | oui |
| US-7 | CI/CD | Haute | 8 | partiel | oui | oui |
| US-8 | Env. de test | Moyenne | 8 | — | oui | oui |
| US-9 | Risque inondation | Luxueuse | 8 | — | partiel | oui |
| US-10 | Compatibilité navigateurs | Moyenne | 5 | — | oui | oui |
| US-11 | Export données | Luxueuse | 5 | — | — | oui |

| Priorité | User Stories | SP total | P1 | P2 | P3 |
|----------|--------------|----------|:--:|:--:|:--:|
| **Haute** | US-1, US-2, US-3, US-5, US-7 | 31 | 100 % | 100 % | 100 % |
| **Moyenne** | US-6, US-8, US-10 | 26 | 0 % | 100 % | 100 % |
| **Basse** | US-4 | 5 | 0 % | 0 % | 100 % |
| **Luxueuse** | US-9, US-11 | 13 | 0 % | partiel (US-9) | 100 % |

---

### 2.2 Gestion des points de complexité

**Méthode retenue :** Story Points Fibonacci (1, 2, 3, 5, 8, 13), estimés en Planning Poker.

**Échelle de calibration :**

| SP | Niveau | Durée indicative |
|----|--------|------------------|
| 1 | Tâche triviale | 2–4 h, 1 dev |
| 2 | Tâche simple | 4–8 h, 1 dev |
| 3 | Tâche moyenne | 1–1,5 j, 1 dev |
| 5 | Tâche complexe | 2–3 j, 1 dev |
| 8 | Tâche très complexe | 3–5 j, 1 dev |
| 13 | Epic | À découper avant engagement sprint |

**Vélocité de l'équipe (ajustée post-comité projet) :**

| Sprint | Vélocité dev | Commentaire |
|--------|--------------|-------------|
| **Sprint 1** (engagement) | **12 SP** | Calibrage legacy ; formation tests hors SP (FORM-T0, PROC-T2) |
| **Sprint 2** (ajusté) | 12 SP confirmés + marge 2 SP (cible 14 SP) | Formation tests S2 (TEST-T1/T2) |
| **Sprints 3+** (stabilisé) | ~14–20 SP/sprint | Plafond 20 SP selon proposition |

**Règle d'ajustement Sprint 2 :**

- S1 livré ≤ 10 SP → S2 = S1 + 2 SP (max 14 SP)
- S1 livré 11–14 SP → S2 = S1 + 3 SP
- S1 livré ≥ 15 SP → S2 = S1 + 4 SP (max 20 SP)

**Détail des calculs de capacité :**

- 2 développeurs actifs (Dimitry, Rachida) : ~72 h dev livrables/semaine
- Facteur brownfield (legacy, dette technique) : −30 %
- Capacité productive : ~100 h/sprint sur 2 semaines
- Conversion 1 SP ≈ 2 h dev effectif → ~20 SP théoriques, ajustés à la vélocité réelle

**Exception DoD Sprint 1 :** tests **manuels documentés** (PROC-T2) — exception validée en comité ; tests automatisés reportés S2 (RS-11).

> Jorge (UX) ne contribue pas directement aux SP « Done » en développement ; son travail alimente les stories des sprints suivants.

**Backlog total :** 75 SP (11 US + procédures + tests + formation).

#### Référentiel de complexité — Sprint 1 (calibrage)

| Tâche technique | Complexité (SP) | Estimation temps | Marge |
|-----------------|-----------------|------------------|-------|
| Corriger erreurs de styles (fontes, messages d'erreur) | 3 | 1,5 j (Dimitry) | +0,5 j |
| Audit et correction de 2 bugs critiques | 5 | 2,5 j (D+Expert) | +1 j |
| Dockerfile + docker-compose (encapsulation app) | 5 | 2,5 j (Rachida) | +1 j |
| Conventions Git et branches (fondation process) | 1 | 0,5 j (Expert) | +0,25 j |
| Audit UX des pages critiques (wireframes Figma) | 3 | 1,5 j (Jorge) | +0,5 j |
| Amélioration accessibilité formulaire de recherche | 5 | 2,5 j (Dimitry) | +1 j |
| Pipeline CI/CD (build + lint, GitHub Actions) | 8 | 4 j (Rachida) | +1 j |
| Optimisation performance back-end Spring Boot | 5 | 2,5 j (Rachida) | +1 j |
| Environnement de tests séparé de la production | 8 | 4 j (Rachida) | +1 j |
| **Total Sprint 1 engagé** | **12 SP** | | |
| Backlog Sprint 1 (buffer non engagé) | 2 SP | | |

---

### 2.3 Coûts

#### Méthode de calcul

- **Coût** = TJM × nombre de jours facturés
- **Jours facturés retenus :** 18 j/mois (convention ESN : congés, fériés, cérémonies Scrum)
- **Hypothèse géographique :** hors Paris / national (+10 à 20 % en Île-de-France)

**Sources TJM (baromètres marché France 2025-2026) :** Silkhom, Elynix Jobs, Freelance Solution, Portage360, Free-Work.

#### TJM retenus par profil

| Membre | Profil | Exp. | Fourchette marché | TJM retenu | Coût/mois (18 j) |
|--------|--------|------|-------------------|-----------|------------------|
| Expert | Lead agile / pilotage qualité | — | 600–750 €/j | 680 €/j | 12 240 € HT |
| Dimitry | Dev front-end Angular / RxJS | 3 ans | 430–550 €/j | 480 €/j | 8 640 € HT |
| Rachida | DevOps (k8s, AWS, CI) + Spring | 5 ans | 550–720 €/j | 620 €/j | 11 160 € HT |
| Jorge | UX Designer senior (Figma) | 12 ans | 520–700 €/j | 580 €/j | 10 440 € HT |
| **TOTAL équipe** (4 × 40 h/semaine) | | | | | **42 480 € HT/mois** |

**Coût sprint moyen :** ~19 680 € HT.

#### Coût Sprint 1 (2 semaines, allocation partielle)

| Tâche / période | Temps | Membre | TJM | Total |
|-----------------|-------|--------|-----|-------|
| Pilotage agile, revue, conventions Git | 8 j | Expert | 680 € | 5 440 € |
| Corrections styles + bugs front-end | 9 j | Dimitry | 480 € | 4 320 € |
| Docker + fondations DevOps | 9 j | Rachida | 620 € | 5 580 € |
| Audit UX + wireframes pages critiques | 6 j | Jorge | 580 € | 3 480 € |
| **TOTAL Sprint 1** | **32 j** | | | **18 820 € HT** |

#### Trois scénarios contractuels

| Proposition | Intention | Durée | Sprints | SP dev | Coût HT |
|-------------|-----------|-------|---------|--------|---------|
| **P1 — Stabiliser & qualifier** | Quick wins client + formation tests minimale viable | 8 sem. | 4 | ~52 SP | **78 720 €** |
| **P2 — Modulariser, tester & livrer** *(recommandée)* | US Haute + Moyenne, DoD standard dès S2 | 10 sem. | 5 | ~63 SP | **98 400 €** |
| **P3 — Industrialiser & scaler** | Backlog intégral 75 SP + excellence technique | 12 sem. | 6 | 75 SP | **118 080 €** + AWS |

**Formule de projection :**

- Durée (semaines) = SP restants ÷ 10 SP/semaine
- Coût mensuel équipe complète = 42 480 € HT (18 j/mois × 4 profils)

#### Détail budget P1 — Stabiliser & qualifier (78 720 € HT)

| Poste | Durée | Coût estimé |
|-------|-------|-------------|
| Sprint 1 (12 SP, calibrage) | 2 semaines | 18 820 € HT |
| Sprint 2 (ajusté ~14 SP) | 2 semaines | 19 500 € HT |
| Sprint 3 (~14 SP) | 2 semaines | 20 200 € HT |
| Sprint 4 (~14 SP) | 2 semaines | 20 200 € HT |
| **TOTAL P1** | **4 sprints / 8 semaines** | **78 720 € HT** |

#### Détail budget P2 — Modulariser, tester & livrer (98 400 € HT)

| Poste | Durée | Coût estimé |
|-------|-------|-------------|
| Sprints 1–2 (socle + formation) | 4 semaines | ~38 320 € HT |
| Sprints 3–4 (pipeline + env test + modularité) | 4 semaines | ~39 400 € HT |
| Sprint 5 (stabilisation + US-9) | 2 semaines | ~20 680 € HT |
| **TOTAL P2** | **5 sprints / 10 semaines** | **98 400 € HT** |

#### Détail budget P3 — Industrialiser & scaler (118 080 € HT+)

| Poste | Durée | Coût estimé |
|-------|-------|-------------|
| Sprints 1–2 (socle + formation, identique P2) | 4 semaines | ~38 320 € HT |
| Sprints 3–4 (extraction microservices, US-8/9/10) | 4 semaines | ~39 600 € HT |
| Sprints 5–6 (US-11, PMTiles, gateway) | 4 semaines | ~40 160 € HT |
| **TOTAL P3** | **6 sprints / 12 semaines** | **118 080 € HT** |
| Coûts AWS récurrents | Post-projet | Hors forfait (RE-05) |

---

### 2.4 Risques identifiés

#### Risques transverses prioritaires

| ID | Risque | Criticité (P×I) | Traitement selon proposition |
|----|--------|-----------------|------------------------------|
| **RS-03** | Absence CI/CD → régressions en production | **Critique (20)** | P2/P3 : pipeline complète ; P1 : partiel (report US7-T2/US-8) |
| **RS-11** | Lacune compétences tests automatisés | **Élevée (16)** | Formation obligatoire S1–S2 (toutes propositions) |
| **RE-01** | Insatisfaction clients / churn | **Élevée (16)** | Quick wins UX S1 (P1/P2/P3) |
| **RS-01** | Lenteurs carte non résolues | **Élevée (16)** | P3 complet ; P2 partiel US-9 ; P1 faible |
| **RG-06 / RS-05** | Surcharge Rachida (DevOps + back) | **Élevée (16)** | P3 risque élevé ; P2 modéré ; P1 limité au périmètre réduit |

#### Risques par proposition

| Proposition | Risques mitigés | Risques résiduels / élevés |
|-------------|-----------------|---------------------------|
| **P1 — Stabiliser & qualifier** | RS-11 (formation S2), RE-01 (clients), RS-08 (A11Y) | RS-03 partiel (pipeline sans tests auto), RS-01 (perf carte) |
| **P2 — Modulariser, tester & livrer** | RS-03, RS-11, RS-04, RS-07, RG-10, RE-01 | RS-01 partiel (via US-9), RS-05 modéré (surcharge Rachida) |
| **P3 — Industrialiser & scaler** | RS-01 (perf carte), RE-02 (compétitivité long terme) | RS-02, RS-05, RG-06, RG-11 — surcharge équipe et courbe d'apprentissage |

#### Points d'attention contractuels

- **P1 :** acceptation explicite du report env test (US-8) et tests pipeline (US7-T2/T3) ; risque RS-03 partiel jusqu'à S4.
- **P2 :** meilleur équilibre risque/livraison — sécurité de livraison complète (US7-T2 + US-8).
- **P3 :** ante-mortem obligatoire avant S4 ; renfort Rachida ou pair Dimitry recommandé sur front géo.

*Registre complet : [risque.md](risque.md).*

---

### 2.5 Définition des objectifs de performance

#### Vélocité et capacité

| Indicateur | Valeur cible |
|------------|--------------|
| Vélocité S1 | 12 SP dev + hors SP (formation, PROC-T2) |
| Vélocité S2 | 12 SP dev confirmés + marge 2 SP (cible 14 SP) |
| Coût mensuel équipe | 42 480 € HT |
| Backlog total | 75 SP |

#### Definition of Done par sprint (toutes propositions)

| Sprint | Definition of Done |
|--------|-------------------|
| **S1** | Tests **manuels documentés** (PROC-T2) — exception validée en comité |
| **S2+** | Tests automatisés obligatoires (unitaires + intégration selon US) |
| **S3+** | Tests E2E Cypress sur parcours critiques (TEST-T3) |

#### Formation tests obligatoire — modules et critères « Certified »

| Module | Profil | Durée | Sprint | Critère « Certified » |
|--------|--------|-------|--------|----------------------|
| **FORM-T0** | Dimitry + Rachida | 2 h | S1 | Compte-rendu atelier |
| **T-EX1** | Expert | 0,5 j | S1–S2 | Document stratégie tests partagé |
| **T-DI1** | Dimitry | 1 j | S2 | 3 tests Angular passants (TEST-T1) |
| **T-RA1** | Rachida | 1 j | S2 | 3 tests JUnit passants (TEST-T2) |
| **T-RA2** | Rachida | 0,5 j | S2 | Tests intégration Testcontainers en CI |
| **T-ALL1** | Dimitry + Rachida | 0,5 j | S2 | 1 feature en TDD validée en pair |
| **T-DI2** | Dimitry | 1 j | S2–S3 | 1 scénario Cypress vert |
| **T-JO1** | Jorge + Dimitry | 0,5 j | S2 | Scénarios E2E documentés |

Formation **hors SP** (label `formation`, `sp:0`) — n'impacte pas la vélocité mesurée.

#### Indicateurs de livraison par proposition

| Indicateur | P1 | P2 | P3 |
|------------|:--:|:--:|:--:|
| Couverture US Haute (100 %) | oui | oui | oui |
| Couverture US Moyenne | — | oui | oui |
| Pipeline CI avec tests auto | partiel (S4) | oui (S2+) | oui |
| Environnement de test isolé | — | oui | oui |
| Tests E2E Cypress | partiel (S3) | oui (S3+) | oui |
| Formation tests certifiante | S1–S2 | S1–S3 | S1–S3 + archi |

---

## 3. Synthèse

### Tableau comparatif des 3 propositions

| Proposition | Durée | Coût HT | Score / 5 | Couverture US | Formation tests | Message client |
|-------------|-------|---------|-----------|---------------|-----------------|----------------|
| **P1 — Base** | 8 sem. | 78 720 € | 3,85 | Haute 100 % | Obligatoire S1–S2 | Stabilisation rapide ; tests manuels S1 puis auto S2 |
| **P2 — Recommandée** | 10 sem. | 98 400 € | **4,25** | Haute + Moyenne | Complète S1–S3 | Évolution durable, livraison industrielle |
| **P3 — Premium** | 12 sem. | 118 080 €+ | 3,65 | Intégral (75 SP) | Complète + archi | Transformation complète, perf maximale |

### Scores pondérés (7 critères)

| Critère | Poids | P1 | P2 | P3 |
|---------|-------|:--:|:--:|:--:|
| Qualité | 20 % | 3 | **4** | 5 |
| Sécurité applicative | 10 % | 3 | **4** | 5 |
| Sécurité de livraison | 15 % | 3 | **5** | **5** |
| Coût | 15 % | **5** | 4 | 2 |
| Temps | 15 % | **5** | 4 | 2 |
| Risque | 15 % | **4** | **4** | 2 |
| Priorité US | 10 % | 4 | **5** | **5** |
| **Score global / 5** | | **3,85** | **4,25** | **3,65** |

### Classement

| Rang | Proposition | Score / 5 | Profil |
|------|-------------|-----------|--------|
| **1er** | **P2 — Modulariser, tester & livrer** | **4,25** | Meilleur équilibre qualité / livraison / priorité US |
| 2e | P1 — Stabiliser & qualifier | 3,85 | Rapidité et coût ; sécurité livraison partielle |
| 3e | P3 — Industrialiser & scaler | 3,65 | Excellence technique au prix du risque et du coût |

### Recommandation : Proposition 2 — « Modulariser, tester & livrer »

**Meilleur équilibre (4,25/5)** pour CATASTERRE :

- Seule proposition couvrant **Haute + Moyenne** avec **sécurité de livraison complète** (US7-T2 + US-8)
- Formation tests **intégrée et certifiante** — DoD standard dès S2
- Alignée sur la veille : monolithe modulaire **avant** microservices
- Budget maîtrisé (~98 k€ HT) sur **10 semaines**

**Séquence proposée :** S1 socle + formation amorce → S2 tests auto + CI build → S3 pipeline complète + env test → S4 préparation modulaire + US-9 → décision extraction microservices en comité.

---

### Alternative budget serré : Proposition 1

**Si** plafond **78 720 € HT** et **8 semaines** non négociables :

- Livrables démontrables : CSS, erreurs, Docker, A11Y, CI build
- Formation tests **obligatoire** dès S1–S2
- **Risque RS-03 partiel** à accepter : pipeline sans tests automatisés jusqu'à S4
- US-6/8/9/10/11 reportées en phase 2 contractuelle

---

### Option premium : Proposition 3

**Si** budget étendu **> 118 k€ HT** et horizon **12 semaines** :

- Backlog intégral 75 SP, différenciation technique maximale (PMTiles, API Gateway, microservices)
- Formation tests + parcours architecture complet
- Nécessite renfort Rachida ou allègement parallèle
- Ante-mortem obligatoire avant S4

---

### Paramètres communs aux 3 propositions

| Paramètre | Valeur |
|-----------|--------|
| Équipe | 4 profils × 40 h/semaine |
| Coût mensuel équipe | 42 480 € HT |
| Coût Sprint 1 | 18 820 € HT |
| Vélocité S1 | 12 SP dev (+ hors SP formation) |
| Formation tests | Obligatoire (non négociable) |

---

*Document rédigé en juin 2026 — Projet 10 CATASTERRE (OpenClassrooms). Analyse détaillée : [comparaison_projets_2.md](comparaison_projets_2.md).*
