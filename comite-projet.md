# Support comité projet — CATASTERRE

> Présentation de fin de sprint / point d'avancement — juin 2026

**Documents associés :** [backlog.md](backlog.md) · [formation.md](formation.md) · [risque.md](risque.md) · [projet.md](projet.md)

---

## 1. Avancement Sprint 1

| Indicateur | Valeur |
|------------|--------|
| Objectif sprint | Stabiliser l'UX et poser les fondations DevOps |
| Engagement initial | 14 SP |
| **Engagement ajusté** | **12 SP** (voir section 3) |
| Équipe | Expert, Dimitry, Rachida, Jorge — 4 × 40 h/semaine |

---

## 2. Point bloquant identifié — Daily Scrum

### Constat (Rachida)

> « Nous ne pouvons pas développer et tester en même temps. Tu n'as pas le temps de les réaliser — tu fais actuellement la gestion du projet en plus de développement, et le reste de notre équipe n'a pas les compétences nécessaires pour écrire et implémenter des tests. C'est un problème bloquant, car il manque les tests pour valider la qualité de l'incrément réalisé ! »

### Analyse

| Cause | Détail |
|-------|--------|
| **Capacité Expert** | Pilotage agile (backlog, refinements, comités) + développement ponctuel — **pas de bande passante** pour écrire la stratégie de tests et les implémenter |
| **Compétences équipe** | Dimitry : pas de pratique formalisée des tests Angular (Jasmine/Vitest, Cypress) ; Rachida : DevOps/back mais seule sur trop de fronts ; Jorge : UX, pas développeur |
| **Dette process** | Application brownfield **sans couverture de tests** existante ; DoD exige des tests mais l'équipe ne peut pas les produire au rythme du développement |
| **Risque associé** | RS-11 ([risque.md](risque.md)) — lacune compétences tests ; renforce RS-03 (CI/CD sans tests = pipeline incomplète) |

### Impacts sur le projet

| Impact | Gravité | Conséquence si non traité |
|--------|---------|---------------------------|
| **Qualité incrément** | Élevé | Livrables S1 non validés automatiquement ; régressions non détectées |
| **Definition of Done** | Élevé | Stories bloquées en « presque Done » — vélocité S1 faussement basse ou DoD contournée |
| **US-7 (CI/CD)** | Moyen | US7-T2 (tests en pipeline) impossible sans tests écrits au préalable |
| **Vélocité S2** | Moyen | Surcorrection si l'équipe tente rattrapage tests + nouvelles US simultanément |
| **Soutenance / comité** | Moyen | Incrément non démontrable avec critères qualité crédibles |

---

## 3. Adaptation du Sprint Backlog 1

### Principe de déblocage

1. **Ne pas bloquer le sprint** — livrer les quick wins UX et Docker avec **tests manuels documentés** (PROC-T2).
2. **Reporter les tests automatisés** — formation + écriture de tests dès **Sprint 2**.
3. **Réduire l'engagement S1** de 14 à **12 SP** — retirer les tâches non critiques et découpler développement / tests.

### Sprint Backlog 1 ajusté — 12 SP

| ID | Tâche | SP | Assigné | Changement |
|----|-------|-----|---------|------------|
| US1-T1 | Audit CSS des pages principales | 1 | Dimitry | — |
| US1-T2 | Corriger le chargement des polices | 2 | Dimitry | — |
| US2-T2 | Composant Angular de notification d'erreur | 2 | Dimitry | Critère S1 : **sans tests unitaires** (reportés S2) |
| US2-T3 | Mapper messages d'erreur HTTP/métier | 2 | Dimitry + Rachida | — |
| US5-T1 | Dockerfile front-end | 2 | Rachida | — |
| US5-T2 | Dockerfile back-end | 2 | Rachida | — |
| US5-T3 | docker-compose.yml + documentation | 1 | Rachida | — |
| PROC-T1 | Conventions Git et stratégie de branches | 1 | Expert | — |
| | **Total Sprint 1** | **12 SP** | | **-2 SP** |

### Reporté au Sprint 2

| ID | Tâche | SP | Raison |
|----|-------|-----|--------|
| US1-T3 | Harmoniser typographie et espacements | 1 | Libère capacité ; non bloquant client |
| US2-T2b | Tests unitaires composant erreur | 1 | Nécessite formation TEST-T1 |
| US2-T1 | Cartographie flux d'erreur | 1 | Expert — peut être S2 |

### Hors SP (parallèle Sprint 1)

| ID | Tâche | Assigné | Livrable |
|----|-------|---------|----------|
| PROC-T2 | Checklist tests manuels parcours critiques | Jorge + Dimitry | Procédure documentée, exécutée en fin S1 |
| FORM-T0 | Démarrage formation tests (aperçu 2 h) | Dimitry + Rachida | Compte-rendu atelier |

### Definition of Done — Sprint 1 (adaptée)

Une tâche est **Terminée** en Sprint 1 lorsque :

- Code revu par un pair et mergé sur la branche principale.
- **Tests manuels documentés** selon PROC-T2 (à la place des tests automatisés).
- Aucune régression sur les parcours critiques (recherche, carte, auth).
- Documentation mise à jour si nécessaire.
- Livrable démontrable en Sprint Review.

> Les tests automatisés redeviennent **obligatoires** à partir du Sprint 2 (DoD standard).

---

## 4. Plan de formation tests

Voir le détail complet dans [formation.md](formation.md) — section **Formation tests (priorité bloquante)**.

### Synthèse pour le comité

| Module | Profil | Outils / pratiques | Durée | Sprint |
|--------|--------|-------------------|-------|--------|
| **T-DI1** | Dimitry | Jasmine / Vitest — tests unitaires Angular | 1j | S2 |
| **T-DI2** | Dimitry | Cypress — tests E2E parcours critiques | 1j | S2-S3 |
| **T-RA1** | Rachida → équipe | JUnit 5 + Mockito — tests unitaires Spring Boot | 1j | S2 |
| **T-RA2** | Rachida | Testcontainers — tests intégration DB en CI | 0,5j | S2 |
| **T-ALL1** | Tous devs | TDD : Red-Green-Refactor, tests avant code | 0,5j | S2 |
| **T-EX1** | Expert | Stratégie tests (pyramide), facilitation — **pas rédacteur unique** | 0,5j | S1-S2 |
| **T-JO1** | Jorge | Scénarios E2E métier (données de test, parcours) | 0,5j | S2 |

### Principes TDD adoptés

1. **Red** — écrire un test qui échoue avant le code de production.
2. **Green** — implémenter le minimum pour faire passer le test.
3. **Refactor** — améliorer le code en gardant les tests verts.
4. **Pyramide de tests** — nombreux tests unitaires, moins d'intégration, peu d'E2E (Cypress sur 3 parcours critiques).

### Charge formation estimée

| Profil | Jours formation tests | Période |
|--------|----------------------|---------|
| Dimitry | 2,5j | S2-S3 |
| Rachida | 1,5j (formateur) + pratique | S2 |
| Expert | 0,5j (stratégie, pas implémentation solo) | S1-S2 |
| Jorge | 0,5j | S2 |

---

## 5. Plan d'action et échéances

| Action | Responsable | Échéance | Statut |
|--------|-------------|----------|--------|
| Ajuster Sprint Backlog 1 (12 SP) | Expert | Immédiat | Fait |
| PROC-T2 checklist tests manuels S1 | Jorge + Dimitry | Fin S1 | En cours |
| Atelier formation tests (FORM-T0) | Rachida + Expert | Semaine 2 S1 | Planifié |
| Modules T-DI1, T-RA1, T-ALL1 | Dimitry + Rachida | Sprint 2 | Planifié |
| TEST-T1 à T3 dans backlog S2 | Expert | Refinement S2 | Planifié |
| US7-T2 pipeline avec tests | Rachida | Sprint 2 | Dépend formation S2 |
| Révision registre risques RS-11 | Expert | Comité projet | Fait |

---

## 6. Risques et mitigation

| Risque | Niveau | Mitigation |
|--------|--------|------------|
| RS-11 — Lacune compétences tests | Élevé | Plan formation §4 |
| RS-03 — CI/CD sans tests | Critique | US7-T2 reporté S2 après formation |
| RG-06 — Surcharge Rachida | Élevé | Rachida **forme** l'équipe ; Expert ne porte plus seul les tests |
| Régressions S1 | Moyen | PROC-T2 tests manuels obligatoires |

---

## 7. Décisions attendues du comité

1. **Valider** l'engagement Sprint 1 réduit à **12 SP** et la DoD adaptée (tests manuels).
2. **Allouer 0,5j/sprint** de capacité formation à partir de S2 (hors vélocité features).
3. **Confirmer** le report US7-T2 (tests en CI) au Sprint 2 — après montée en compétence.

---

*Document rédigé le 13/06/2026 — Projet 10 CATASTERRE (OpenClassrooms).*
