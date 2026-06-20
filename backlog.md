# Product Backlog — CATASTERRE

> Source : [Formez et encadrez une équipe de développement Full-Stack ‒ Product Backlog](https://www.notion.so/Formez-et-encadrez-une-quipe-de-d-veloppement-Full-Stack-Product-Backlog-4ed8890fef3582f786c68119bc830c64) (OpenClassrooms — Projet 10)

---

## Avertissement (page Notion)

N'oubliez pas de **dupliquer cette page** dans votre espace personnel afin de pouvoir faire des modifications. Vous devez ensuite la rendre **publiquement accessible** pour votre soutenance.

---

## Votre mission

Votre mission sera de créer les **Sprint Backlog**.

- Définir les **objectifs de sprint** en fonction des principaux objectifs définis dans le document d'introduction au projet.
- **Découper les user stories** en tâches techniques.
- **Associer à chaque tâche technique** des points de complexité.
- La vélocité de l'équipe n'est pas connue : capacité maximum proposée de **15 points par sprint**.
- Vous pouvez lire plus d'informations sur certaines User Stories en les ouvrant dans Notion.

---

## Structure du backlog

| Colonne | Description | Valeurs possibles |
|---------|-------------|-------------------|
| **User Story** | Intitulé de la fonctionnalité ou du besoin | — |
| **État** | Statut d'avancement | Backlog, A faire, En cours, Terminé |
| **Priorité** | Niveau de priorité métier | Haute, Moyenne, Basse, Luxueuse |
| **Estimation en SP** | Story Points (Fibonacci) | 1, 2, 3, 5, 8, 13 |
| **Objectif de Sprint** | Regroupement par objectif de sprint | Ex. : *Afficher les zones d'inondation dans des zones côtières* |

---

## Product Backlog — User Stories

| # | User Story | Priorité | État | Estimation (SP) | Sprint cible |
|---|------------|----------|------|-----------------|--------------|
| 1 | Amélioration du style CSS | Haute | Backlog | 5 | Sprint 1 |
| 2 | Meilleure gestion des messages d'erreur | Haute | Backlog | 5 | Sprint 1 |
| 3 | Améliorer l'accessibilité (A11Y) | Haute | Backlog | 8 | Sprint 2 |
| 4 | Créer un nouveau thème | Basse | Backlog | 5 | Reporté |
| 5 | Encapsuler l'application | Haute | Backlog | 5 | Sprint 1 |
| 6 | Implémentation d'une architecture en micro-services | Moyenne | Backlog | 13 | Sprint 4+ |
| 7 | Créer une pipeline d'intégration continue | Haute | Backlog | 8 | Sprint 2 |
| 8 | Mise en place d'un environnement de test | Moyenne | Backlog | 8 | Sprint 3 |
| 9 | Améliorer le calcul du risque d'inondation | Luxueuse | Backlog | 8 | Sprint 4+ |
| 10 | Problème de compatibilité avec les navigateurs | Moyenne | Backlog | 5 | Sprint 3 |
| 11 | Améliorer l'exportation des données | Luxueuse | Backlog | 5 | Sprint 4+ |
| | **Total backlog** | | | **75 SP** | ~5-6 sprints |

---

## Synthèse — assignation principale par US

| US | Titre | Total SP | Assigné principal |
|----|-------|----------|-------------------|
| 1 | Style CSS | 5 | Dimitry |
| 2 | Messages d'erreur | 5 | Dimitry |
| 3 | Accessibilité | 8 | Dimitry + Jorge |
| 4 | Nouveau thème | 5 | Jorge + Dimitry |
| 5 | Docker | 5 | Rachida |
| 6 | Micro-services | 13 | Expert + Rachida |
| 7 | CI/CD | 8 | Rachida |
| 8 | Env. de test | 8 | Rachida |
| 9 | Risque inondation | 8 | Rachida + Dimitry |
| 10 | Compatibilité navigateurs | 5 | Dimitry + Jorge |
| 11 | Export données | 5 | Rachida + Dimitry |

---

## Tâches techniques par User Story

### US-1 — Amélioration du style CSS (5 SP)

| ID | Tâche technique | Assigné | SP | Critère de succès |
|----|-----------------|---------|-----|-------------------|
| US1-T1 | Auditer les feuilles de style et recenser les anomalies (fontes, contrastes, débordements) sur les pages principales | Dimitry | 1 | Liste d'anomalies documentée avec captures et pages concernées |
| US1-T2 | Corriger le chargement et la visibilité des polices (fallback, `@font-face`, variables CSS) | Dimitry | 2 | Toutes les polices s'affichent correctement sur Chrome et Firefox |
| US1-T3 | Harmoniser la typographie et les espacements via variables/thème CSS existant | Dimitry | 1 | Styles cohérents sur les 3 pages principales, sans régression visuelle |
| US1-T4 | Revue visuelle des corrections avec Jorge | Jorge | 1 | Validation UX formalisée (commentaires Figma ou checklist) |

### US-2 — Meilleure gestion des messages d'erreur (5 SP)

| ID | Tâche technique | Assigné | SP | Critère de succès |
|----|-----------------|---------|-----|-------------------|
| US2-T1 | Cartographier les flux d'erreur front (HTTP, validation, runtime) et back (exceptions Spring) | Expert | 1 | Schéma des flux d'erreur partagé avec l'équipe |
| US2-T2 | Créer/standardiser un composant Angular de notification d'erreur réutilisable | Dimitry | 2 | Composant intégré sur au moins 2 pages ; **tests unitaires en S2** (TEST-T1) |
| US2-T3 | Mapper les codes HTTP et exceptions métier vers des messages utilisateur clairs | Dimitry + Rachida | 2 | Messages compréhensibles pour les 5 cas d'erreur les plus fréquents |

### US-3 — Améliorer l'accessibilité A11Y (8 SP)

| ID | Tâche technique | Assigné | SP | Critère de succès |
|----|-----------------|---------|-----|-------------------|
| US3-T1 | Audit accessibilité des parcours critiques (formulaire recherche, résultats, navigation) | Jorge | 2 | Rapport d'audit avec points bloquants et recommandations |
| US3-T2 | Corriger la navigation clavier et le focus visible sur les composants interactifs | Dimitry | 2 | Parcours complet réalisable au clavier sans piège de focus |
| US3-T3 | Ajouter attributs ARIA, labels et textes alternatifs manquants | Dimitry | 2 | Formulaires et boutons conformes aux bonnes pratiques ARIA |
| US3-T4 | Corriger les ratios de contraste couleur signalés par l'audit | Dimitry | 2 | Contrastes conformes WCAG AA sur les éléments audités |

### US-4 — Créer un nouveau thème (5 SP — reportée)

Priorité basse ; dark theme déjà implémenté ([projet.md](projet.md)). Hors Sprint 1-3.

| ID | Tâche technique | Assigné | SP | Critère de succès |
|----|-----------------|---------|-----|-------------------|
| US4-T1 | Atelier UX : recueil des besoins thème alternatif | Jorge | 1 | Synthèse des besoins validée par le Product Owner |
| US4-T2 | Maquettes Figma du nouveau thème | Jorge | 2 | Maquettes desktop + mobile des pages principales |
| US4-T3 | Implémentation du thème via variables CSS / Angular theming | Dimitry | 2 | Thème activable sans régression sur le dark theme existant |

### US-5 — Encapsuler l'application (5 SP)

| ID | Tâche technique | Assigné | SP | Critère de succès |
|----|-----------------|---------|-----|-------------------|
| US5-T1 | Rédiger le `Dockerfile` front-end (build Angular + nginx ou node) | Rachida | 2 | Image front buildée et démarrée en local |
| US5-T2 | Rédiger le `Dockerfile` back-end (Spring Boot) | Rachida | 2 | Image back buildée, API accessible en local |
| US5-T3 | Créer `docker-compose.yml` et documenter le lancement local | Rachida | 1 | `docker compose up` démarre l'application complète, README à jour |

### US-6 — Architecture micro-services (13 SP — phase 2)

Aligné sur [projet.md](projet.md) étape B. À planifier après stabilisation Docker/CI.

| ID | Tâche technique | Assigné | SP | Critère de succès |
|----|-----------------|---------|-----|-------------------|
| US6-T1 | Analyser le monolithe et identifier les bounded contexts (images, risques, auth, API) | Expert | 2 | Document d'analyse avec domaines identifiés |
| US6-T2 | Rédiger le document d'architecture cible (diagramme services + APIs) | Expert | 3 | Diagramme validé par l'équipe, contrats d'API définis |
| US6-T3 | Extraire le premier service (ex. service de calcul des risques) | Rachida | 5 | Service déployable indépendamment, tests passants |
| US6-T4 | Mettre en place la communication inter-services (REST ou messaging) | Rachida | 3 | Appels inter-services fonctionnels avec gestion d'erreurs |

### US-7 — Pipeline d'intégration continue (8 SP)

| ID | Tâche technique | Assigné | SP | Critère de succès |
|----|-----------------|---------|-----|-------------------|
| US7-T1 | Configurer workflow GitHub Actions : build front + back | Rachida | 3 | Pipeline verte sur push et pull request |
| US7-T2 | Intégrer lint et tests unitaires dans la pipeline | Rachida | 3 | Échec de build si lint ou tests en erreur |
| US7-T3 | Publier l'image Docker en artefact / registry à chaque merge | Rachida | 2 | Image disponible après merge sur branche principale |

### US-8 — Environnement de test (8 SP)

| ID | Tâche technique | Assigné | SP | Critère de succès |
|----|-----------------|---------|-----|-------------------|
| US8-T1 | Provisionner l'environnement de test (Docker/AWS, séparé de prod) | Rachida | 3 | Env de test accessible, isolé de la production |
| US8-T2 | Externaliser la configuration (profils Spring `test`, variables d'env) | Rachida | 2 | Config prod/test séparée, aucun secret en dur |
| US8-T3 | Ajouter un job de déploiement automatique vers l'env de test | Rachida | 2 | Déploiement auto déclenché après merge validé |
| US8-T4 | Rédiger les tests de smoke post-déploiement | Expert | 1 | Checklist smoke exécutée avec succès après chaque déploiement |

### US-9 — Calcul du risque d'inondation (8 SP — luxueuse)

| ID | Tâche technique | Assigné | SP | Critère de succès |
|----|-----------------|---------|-----|-------------------|
| US9-T1 | Profiler les performances de l'algorithme de calcul actuel | Rachida | 2 | Rapport de profiling avec goulots identifiés |
| US9-T2 | Optimiser la requête/traitement back-end (cache, index DB) | Rachida | 3 | Temps de réponse réduit d'au moins 30 % sur jeu de test |
| US9-T3 | Améliorer l'affichage des zones côtières inondables côté front | Dimitry | 2 | Zones affichées correctement sur la carte, UX fluide |
| US9-T4 | Valider la précision des résultats sur un jeu de données de référence | Expert | 1 | Résultats conformes aux attentes métier sur 10 cas de test |

### US-10 — Compatibilité navigateurs (5 SP)

| ID | Tâche technique | Assigné | SP | Critère de succès |
|----|-----------------|---------|-----|-------------------|
| US10-T1 | Établir la matrice de compatibilité cible (Chrome, Firefox, Safari, Edge) | Jorge | 1 | Matrice documentée avec versions minimales supportées |
| US10-T2 | Corriger les incompatibilités CSS/JS identifiées (polyfills si besoin) | Dimitry | 3 | Rendu identique sur les 4 navigateurs cibles |
| US10-T3 | Campagne de tests manuels cross-browser et rapport | Dimitry | 1 | Rapport de tests sans bloquant sur navigateurs cibles |

### US-11 — Exportation des données (5 SP — luxueuse)

| ID | Tâche technique | Assigné | SP | Critère de succès |
|----|-----------------|---------|-----|-------------------|
| US11-T1 | Spécifier le format d'export (CSV/PDF/GeoJSON) avec les parties prenantes | Jorge + Expert | 1 | Spécification validée (format, champs, limites) |
| US11-T2 | Implémenter l'endpoint d'export back-end Spring Boot | Rachida | 3 | API retourne un fichier valide pour un jeu de données test |
| US11-T3 | Ajouter l'action d'export dans l'interface Angular | Dimitry | 1 | Bouton d'export fonctionnel, téléchargement du fichier |

---

## Sprint Backlog 1 — 12 SP (ajusté)

**Objectif de sprint :** Stabiliser l'UX et poser les fondations DevOps (quick wins front-end + containerisation).

**Durée :** 2 semaines | **Capacité max :** 15 SP | **Engagement initial :** 14 SP → **ajusté 12 SP**

> **Point bloquant Daily Scrum (Rachida) :** l'équipe ne peut pas développer et tester simultanément — l'Expert pilote le projet sans bande passante pour les tests ; Dimitry et Rachida n'ont pas encore les compétences pour écrire et implémenter des tests automatisés. Voir [comite-projet.md](comite-projet.md) et [formation.md](formation.md) (section tests).

| ID | Tâche | SP | Assigné | US parente |
|----|-------|-----|---------|------------|
| US1-T1 | Audit CSS des pages principales | 1 | Dimitry | US-1 |
| US1-T2 | Corriger le chargement des polices | 2 | Dimitry | US-1 |
| US2-T2 | Composant Angular de notification d'erreur *(sans tests unitaires S1)* | 2 | Dimitry | US-2 |
| US2-T3 | Mapper messages d'erreur HTTP/métier | 2 | Dimitry + Rachida | US-2 |
| US5-T1 | Dockerfile front-end | 2 | Rachida | US-5 |
| US5-T2 | Dockerfile back-end | 2 | Rachida | US-5 |
| US5-T3 | docker-compose.yml + documentation | 1 | Rachida | US-5 |
| PROC-T1 | Conventions Git et stratégie de branches | 0 | Expert | — |
| | **Total Sprint 1** | **12 SP** | | |

**Retiré du S1 (reporté S2) :** US1-T3 (1 SP), tests unitaires US2-T2 (1 SP → TEST-T1).

**Hors SP (en parallèle) :** Jorge — audit accessibilité (US3-T1) ; **PROC-T2** checklist tests manuels (Jorge + Dimitry) ; **FORM-T0** aperçu formation tests (Dimitry + Rachida).

**Stories partiellement couvertes en S1 :** US-1 (3/5 SP), US-2 (4/5 SP hors tests auto), US-5 (5/5 SP).

**DoD Sprint 1 adaptée :** tests **manuels documentés** (PROC-T2) à la place des tests automatisés — DoD standard à partir de S2.

**Règle d'ajustement Sprint 2 :** vélocité S1 + 2 à 4 SP selon livraison réelle ; intégrer formation tests (TEST-T1 à T3).

---

## Sprint Backlog 2 — 14 SP (prévisionnel)

**Objectif de sprint :** Accessibilité (début), CI/CD (build), **montée en compétence tests** et rattrapage qualité S1.

| ID | Tâche | SP | Assigné | US parente |
|----|-------|-----|---------|------------|
| US1-T3 | Harmoniser typographie et espacements | 1 | Dimitry | US-1 |
| US2-T1 | Cartographier les flux d'erreur front/back | 1 | Expert | US-2 |
| TEST-T1 | Tests unitaires composant erreur (Jasmine/Vitest) | 1 | Dimitry | US-2 |
| TEST-T2 | Tests unitaires back-end (JUnit + Mockito) | 2 | Rachida + Dimitry | US-2 |
| US3-T1 | Audit accessibilité parcours critiques | 2 | Jorge | US-3 |
| US3-T2 | Navigation clavier et focus visible | 2 | Dimitry | US-3 |
| US7-T1 | Workflow GitHub Actions build front + back | 3 | Rachida | US-7 |
| | **Total Sprint 2** | **12 SP** | | |

> **Engagement cible S2 :** 14 SP (règle S1 + 2 SP) — les 12 SP ci-dessus sont le périmètre dev confirmé ; marge de 2 SP pour refinement ou imprévus.

**Hors SP (formation, parallèle) :** T-DI1, T-RA1, T-RA2, T-ALL1, T-JO1 — voir [formation.md](formation.md) et issues GitHub label `formation`.

**Reporté Sprint 3 :** US3-T3/T4, TEST-T3, US7-T2/T3 (dépendent formation tests terminée).

---

## Critères de succès globaux (Definition of Done)

### DoD standard (à partir du Sprint 2)

Une tâche est **Terminée** lorsque :

- Le code est **revu** par au moins un pair et **mergé** sur la branche principale.
- Les **tests automatisés** associés passent (unitaires minimum ; E2E si parcours critique).
- Aucune **régression** sur les parcours critiques (recherche, affichage carte, authentification).
- La **documentation** est mise à jour si nécessaire (README Docker, conventions Git, API).
- Le livrable est **démontrable** en fin de sprint (Sprint Review).

Une User Story est **Terminée** lorsque toutes ses tâches sont Done et que les critères de succès de chaque tâche sont validés.

### DoD Sprint 1 — exception tests (point bloquant Rachida)

En Sprint 1 uniquement, les tests **manuels documentés** (PROC-T2) remplacent les tests automatisés. Voir [comite-projet.md](comite-projet.md).

---

## Regroupement par priorité

### Haute priorité
1. Amélioration du style CSS
2. Meilleure gestion des messages d'erreur
3. Améliorer l'accessibilité (A11Y)
5. Encapsuler l'application
7. Créer une pipeline d'intégration continue

### Moyenne priorité
6. Implémentation d'une architecture en micro-services
8. Mise en place d'un environnement de test
10. Problème de compatibilité avec les navigateurs

### Basse priorité
4. Créer un nouveau thème *(non prioritaire selon le cahier des charges — dark theme déjà implémenté)*

### Luxueuse
9. Améliorer le calcul du risque d'inondation
11. Améliorer l'exportation des données

---

## Objectif de sprint (exemple fourni dans Notion)

- **Afficher les zones d'inondation dans des zones côtières** *(cible Sprint 4+, via US-9)*

---

## Vues Notion

La page contient deux vues de base de données :

1. **Product Backlog** — liste complète des user stories
2. **Sprint Backlog** — même base, organisée par objectif de sprint (à compléter)

---

## Alignement avec le cahier des charges ([projet.md](projet.md))

| Epic cahier des charges | User stories associées |
|-------------------------|----------------------|
| Améliorer l'expérience utilisateur | 1, 2, 3, 4, 10 |
| Disponibilité / maintenabilité | 5, 6, 7, 8 |
| Fiabiliser le développement (CI/CD, tests) | 7, 8 |
| Fonctionnalités métier (risques, export) | 9, 11 |

---

## GitHub Project

Backlog importé dans le GitHub Project **[Projet10 backlog](https://github.com/users/laurentcoufinal/projects/4)** :

- **63 issues** dans [laurentcoufinal/projet10](https://github.com/laurentcoufinal/projet10/issues) (#2–#51 existantes + FORM + formation/tests)
- **12 User Stories** + **1 epic formation (FORM)** + **8 modules formation** + **42 tâches techniques**
- Labels : `formation` (hors SP), `sp:0`…`sp:13`, `sprint:1`…`sprint:4plus`
- **Vélocité GitHub (tasks) :** Sprint 1 = **12 SP** dev · Sprint 2 = **12 SP** dev (engagement cible 14 SP = S1 + 2)
- Script de sync : `scripts/import-backlog-to-github.sh --sync`

## Veille technologique

Voir [veille.md](veille.md) — veille sur architectures, performances, dette technique et bonnes pratiques Full-Stack (juin 2026).

## Plans de formation

Voir [formation.md](formation.md) — parcours modulaires par profil, **formation tests (JUnit, Cypress, TDD)**.

## Comité projet

Voir [comite-projet.md](comite-projet.md) — point bloquant tests Rachida, Sprint 1 ajusté (12 SP).

## Analyse des risques

Voir [risque.md](risque.md) — analyse spectre 7D, risques spécifiques CATASTERRE, matrice P×I et plan de prévention (juin 2026).

## Analyse comparative des solutions

Voir [choix.md](choix.md) — classement de 3 solutions selon qualité, sécurité, temps, coût et risque (juin 2026).

Voir [comparaison_projets_2.md](comparaison_projets_2.md) — 3 propositions sur 7 critères (sécurité applicative, sécurité de livraison, priorité US) avec formation tests obligatoire.

## Comité projet

Voir [comite-projet.md](comite-projet.md) — point bloquant tests, adaptation Sprint 1, plan de formation et support de présentation.

---

*Document mis à jour le 13/06/2026 — Sprint Backlog 1 ajusté (12 SP) suite point bloquant tests.*
