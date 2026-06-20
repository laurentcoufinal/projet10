# Veille technologique — Projet CATASTERRE

> Document de veille pour alimenter la **prise de décision** de l'équipe.  
> Il ne propose pas de solution clé en main, mais des constats sectoriels croisés avec le contexte du projet.

**Date de consultation :** juin 2026  
**Sources :** articles techniques, documentation officielle et retours d'expérience publiés entre 2023 et 2026.

**Documents de référence projet :** [projet.md](projet.md) · [backlog.md](backlog.md) · [GitHub Project Projet10 backlog](https://github.com/users/laurentcoufinal/projects/4)

---

## Contexte et périmètre de la veille

CATASTERRE est une application web de **visualisation de catastrophes naturelles** via imagerie satellite, destinée aux notaires, agences immobilières et professionnels de l'immobilier. L'application permet d'évaluer les risques associés à des propriétés.

### Contraintes identifiées ([projet.md](projet.md))

| Dimension | Constat |
|-----------|---------|
| Maturité | Application **brownfield** lancée il y a moins d'un an |
| Problèmes clients | Lenteurs, erreurs fréquentes, instabilités |
| Stack technique | **Angular** (front) · **Spring Boot / Spring Security / Spring Data** (back) · **MySQL** |
| Roadmap architecture | Étape A : **Docker** → Étape B : **microservices** |
| DevOps cible | **GitHub Actions**, environnement de test séparé, **k8s / AWS** |
| Équipe | Dimitry (front Angular) · Rachida (DevOps + back Java) · Jorge (UX) · Expert (pilotage agile) |

### Périmètre de cette veille

La veille couvre quatre axes demandés dans le cadre du projet :

1. Architectures applicatives
2. Performances de l'application
3. Gestion de la dette technique
4. Bonnes pratiques Full-Stack

Chaque section se termine par des **questions ouvertes** à traiter en comité projet, refinement ou rétrospective.

---

## Méthodologie et sources

### Méthode

1. Identification des tendances et bonnes pratiques publiées en 2025-2026 sur chaque axe.
2. Croisement avec le **Product Backlog** (11 User Stories, 75 SP) et la roadmap [projet.md](projet.md).
3. Formulation de **questions de décision** — pas de recommandation unique imposée.
4. Priorisation implicite alignée sur les sprints planifiés (Sprint 1 : stabilisation UX + Docker).

### Critères de sélection des sources

- Pertinence directe avec la stack Angular + Spring Boot
- Applicabilité au contexte **géospatial** / imagerie satellite
- Focus sur la **modernisation incrémentale** (brownfield), pas greenfield
- Sources récentes et vérifiables (documentation éditeur, architecture centers, retours terrain)

---

## 1. Architectures applicatives

### 1.1 Monolithe modulaire avant microservices

**Constat secteur :** Le consensus 2025-2026 ne recommande plus le « big-bang » vers microservices. Les équipes passent d'abord par un **monolithe modulaire** (bounded contexts internes, APIs entre modules) avant toute extraction réseau. Cela valide les frontières métier à moindre coût.

**Lien CATASTERRE :** Aligné avec l'étape A de [projet.md](projet.md) (Docker d'abord) et l'US-6 (microservices, Sprint 4+).

**Questions de décision :**
- Faut-il structurer le monolithe en modules internes (`images`, `risques`, `auth`, `export`) **avant** d'extraire le premier service ?
- Qui porte la responsabilité de définir les bounded contexts : Expert, Rachida, ou atelier collectif ?

**Sources :** [knowledgelib.io — Monolith to Microservices](https://knowledgelib.io/software/migrations/monolith-to-microservices/2026) · [DEV Community — Migration patterns](https://dev.to/sepehr/from-monolith-to-modular-monolith-to-microservices-realistic-migration-patterns-36f2)

---

### 1.2 Pattern Strangler Fig

**Constat secteur :** Le pattern [Strangler Fig](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) permet une migration incrémentale : une façade intercepte le trafic et le redirige progressivement du legacy vers les nouveaux services. Les phases recommandées sont **shadow** (0 % trafic) → **canary** (5-50 %) → **cutover** (100 %).

**Lien CATASTERRE :** Cohérent avec l'étape B de [projet.md](projet.md) et l'US-6 (13 SP). Le calcul des risques d'inondation (US-9) et le traitement d'images sont des candidats naturels à l'extraction.

**Questions de décision :**
- Quel **premier bounded context** extraire : `RiskCalculation` ou `ImageIngestion` ?
- Une API Gateway (Spring Cloud Gateway, Traefik) est-elle envisageable dans l'infra actuelle (AWS/k8s) ?

**Sources :** [Microsoft Learn — Strangler Fig](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) · [microservices.io — Refactoring](https://microservices.io/refactoring/) · [Trinity Logic — Strangler Fig Spring Boot](https://www.trinitylogic.co.uk/blog/strangler-fig-pattern-spring-boot/)

---

### 1.3 Anti-Corruption Layer (ACL)

**Constat secteur :** Lors du découpage, un **Anti-Corruption Layer** traduit les modèles legacy vers les nouveaux services, évitant la propagation de la dette technique dans l'architecture cible.

**Lien CATASTERRE :** Application peu documentée, erreurs fréquentes — risque élevé de fuite de concepts legacy.

**Questions de décision :**
- L'ACL se place-t-il à la **frontière API** (controllers) ou dans une **couche service** dédiée ?
- Faut-il documenter le modèle de domaine actuel avant toute extraction (US6-T1) ?

---

### 1.4 Architecture géospatiale cloud-native

**Constat secteur :** Les plateformes géospatiales modernes s'orientent vers des formats **cloud-native** :

| Format / standard | Rôle |
|-------------------|------|
| **COG** (Cloud Optimized GeoTIFF) | Imagerie raster streamable via HTTP range requests |
| **PMTiles / MVT** | Tuiles vectorielles pré-générées ou dynamiques |
| **STAC** | Catalogue de métadonnées spatio-temporelles |

Ces approches réduisent la dépendance à des serveurs GeoServer lourds et permettent un scaling plus élastique (serverless, CDN).

**Lien CATASTERRE :** US-9 (calcul risque inondation), objectif de sprint « zones d'inondation côtières ». Les lenteurs client pourraient provenir d'un chargement GeoJSON massif plutôt que de tuiles.

**Questions de décision :**
- Quel format utilisent les images satellites aujourd'hui (GeoJSON, TIFF brut, tuiles) ?
- Une migration vers COG/PMTiles est-elle réaliste à court terme ou réservée au Sprint 4+ ?

**Sources :** [Off-Nadir Delta — WebGIS Architecture](https://offnadir-delta.com/blog/webgis-architecture-modern-stack) · [BASF Digital Farming — STAC on EKS](https://noise.getoto.net/2025/10/22/basf-digital-farming-builds-a-stac-based-solution-on-amazon-eks/)

---

### 1.5 Contrat API front/back (OpenAPI)

**Constat secteur :** L'approche **contract-first** avec OpenAPI synchronise le front Angular et le back Spring Boot, réduit les erreurs d'intégration et facilite les tests de contrat.

**Lien CATASTERRE :** Erreurs front/back signalées par les clients (US-2). Pourrait limiter les régressions lors du découpage en services.

**Questions de décision :**
- Introduire OpenAPI dès le Sprint 2 (avec CI/CD) ou après stabilisation Sprint 1 ?
- Génération automatique des clients TypeScript Angular depuis la spec ?

**Source :** [Innovirtuoso — Angular + Spring Boot Guide](https://innovirtuoso.com/full-stack-development/complete-angular-spring-boot-developers-guide-build-scalable-full%e2%80%91stack-apps-that-ship-fast/)

---

### Bounded contexts probables (à valider en atelier)

| Contexte | Responsabilité métier | US associées |
|----------|----------------------|--------------|
| `ImageIngestion` | Récupération et traitement images satellite | — |
| `RiskCalculation` | Calcul risques (inondation, zones côtières) | US-9 |
| `UserAccess` | Authentification, autorisation | — |
| `Export` | Exportation données (CSV, PDF, GeoJSON) | US-11 |
| `Presentation` | UX, accessibilité, affichage carte | US-1, US-2, US-3, US-10 |

---

## 2. Performances de l'application

### 2.1 Front-end Angular (Dimitry)

| Thème | Constat | Lien backlog |
|-------|---------|--------------|
| **Zoneless + Signals** | Stable depuis Angular 20.2, défaut en v21. Supprime Zone.js, réduit les cycles de change detection inutiles, améliore les Core Web Vitals. | US-1, US-10 |
| **OnPush + @defer** | `ChangeDetectionStrategy.OnPush` et blocs `@defer` permettent de ne charger les composants lourds (carte, graphiques) qu'à la demande. | Lenteurs signalées |
| **NgOptimizedImage** | Directive native pour lazy-loading, tailles responsives et réduction du CLS sur les images. | Imagerie satellite |

**Questions de décision :**
- Quelle version d'Angular est en production aujourd'hui ?
- Quels composants cartographiques sont chargés **au démarrage** de l'application ?
- Une migration zoneless progressive est-elle envisageable ou reportée ?

**Sources :** [Zyra UI — Angular v21 Zoneless Guide](https://www.zyraui.dev/blog/angular-v21-zoneless-guide-remove-zonejs-use-signals) · [Angular Skills — Performance](https://tessl.io/registry/skills/github/sickn33/antigravity-awesome-skills/angular)

---

### 2.2 Back-end Spring Boot (Rachida)

| Thème | Constat | Lien backlog |
|-------|---------|--------------|
| **N+1 queries / OSIV** | Le problème N+1 (1 requête + N requêtes lazy) est la cause n°1 de lenteur JPA. `spring.jpa.open-in-view=false` force des stratégies de fetch explicites (JOIN FETCH, @EntityGraph, DTO projections). | US-9 |
| **Cache Caffeine / Redis** | Efficace sur données de référence **stables** ; peu adapté aux listes dynamiques ou résultats de calcul. | US9-T2 |
| **Virtual threads (Java 21+)** | Améliorent le débit sur I/O bloquant (JDBC) si le pool HikariCP est correctement dimensionné. | Scalabilité post-Docker |
| **Batch JDBC** | `hibernate.jdbc.batch_size` accélère les écritures groupées. | US-11 (export) |

**Questions de décision :**
- Un audit Hibernate est-il planifié avant US9-T1 (profiling) ?
- Combien de requêtes SQL par endpoint critique (recherche propriété, affichage carte) ?
- Version Java en production ? Configuration actuelle du pool HikariCP ?

**Sources :** [Devops Monk — Spring Boot JPA Performance](https://blog.devops-monk.com/2026/05/spring-boot-jpa-performance/) · [CodeWiz — 11 JPA Performance Killers](https://codewiz.info/blog/jpa-performance-anti-patterns/) · [EliteDev — Virtual Threads Guide](https://java.elitedev.in/java/complete-virtual-threads-guide-for-spring-boot-32-with-database-connection-pool-optimization/)

---

### 2.3 Spécificités géospatiales

| Thème | Constat | Impact potentiel CATASTERRE |
|-------|---------|----------------------------|
| **GeoJSON massif vs tuiles vectorielles** | 700 000 polygones en GeoJSON (~350-500 Mo) saturent le navigateur. Les tuiles vectorielles (PMTiles/MVT) divisent le volume par 10 à 25 et chargent uniquement la zone visible. | Cause probable des lenteurs carte |
| **Index spatial MySQL** | Requêtes géographiques sans index spatial = full table scan. | US9-T2 |
| **CDN + cache tuiles** | Tuiles immuables = cache CDN longue durée, latence < 50 ms. | Post-Docker, AWS |

**Questions de décision :**
- Les zones de risque sont-elles servies en GeoJSON intégral ou en tuiles ?
- Des index spatiaux existent-ils sur les tables MySQL concernées ?

**Sources :** [agfianf — Optimizing Satellite Maps](https://agfianf.github.io/blog/2025/03/04/optimizing-satellite-maps-efficiently-rendering-700k-object-polygons-and-their-attributes/) · [Off-Nadir Delta — CDN caching](https://offnadir-delta.com/blog/webgis-architecture-modern-stack)

---

### 2.4 Métriques de référence (indicatives)

Ces seuils ne sont pas des objectifs imposés, mais des repères sectoriels pour orienter les discussions :

| Métrique | Seuil indicatif | Outil |
|----------|-----------------|-------|
| LCP (Largest Contentful Paint) | ≤ 2,5 s | Lighthouse, Web Vitals |
| CLS (Cumulative Layout Shift) | ≤ 0,1 | Lighthouse |
| INP (Interaction to Next Paint) | ≤ 200 ms | Lighthouse |
| Temps réponse API (p95) | À définir après profiling | Spring Actuator, Micrometer |

**Principe clé :** mesurer avant d'optimiser (US9-T1 — profiling avant cache/index).

---

## 3. Gestion de la dette technique

### 3.1 Principes de modernisation brownfield

| Thème | Constat | Application CATASTERRE |
|-------|---------|----------------------|
| **Pas de big-bang rewrite** | Réécriture complète = risque élevé de downtime, dépassement budget, échec projet. | Valide l'approche incrémentale du backlog (sprints 1-6) |
| **Audit structural** | Analyse statique du code peut réduire le périmètre de modernisation de ~30 %. | À planifier avant US-6 (microservices) |
| **Modèle TIME / MoSCoW** | Classer chaque module : **T**olerate, **I**nvest, **M**igrate, **E**liminate. | US-4 (thème) = « Won't » · US-9/11 = « Could » |
| **Parallel run** | Le legacy reste autoritaire jusqu'à validation du nouveau module en environnement de test. | US-8 (env test séparé) |
| **Dette visible dans le backlog** | La dette technique doit apparaître comme des stories dédiées, pas uniquement comme des bugs. | US-1, US-2 = dette UX · US-7 = dette process |

**Questions de décision :**
- Quelle dette **bloque la vélocité** (Sprint 1-2) vs dette **structurelle** (Sprint 4+) ?
- Un audit de code est-il prévu avant l'US-6 ? Qui le porte ?

**Sources :** [Javra — Modernizing Legacy Software 2025](https://www.javra.com/modernizing-legacy-software-2025-low-risk-playbook/) · [Pretius — Phased Legacy Modernization](https://pretius.com/blog/phased-legacy-modernization)

---

### 3.2 Cartographie dette / backlog

| Type de dette | User Stories concernées | Priorité backlog |
|---------------|------------------------|------------------|
| Dette UX (styles, erreurs, accessibilité) | US-1, US-2, US-3 | Haute — Sprint 1-2 |
| Dette process (pas de CI/CD, pas d'env test) | US-7, US-8 | Haute — Sprint 2-3 |
| Dette deploy (pas de containerisation) | US-5 | Haute — Sprint 1 |
| Dette structurelle (monolithe non modulaire) | US-6 | Moyenne — Sprint 4+ |
| Dette métier (perf calcul, export) | US-9, US-11 | Basse / Luxueuse — Sprint 4+ |
| Dette reportée (nouveau thème) | US-4 | Basse — reporté ([projet.md](projet.md) L42-43) |

---

### 3.3 Indicateurs de suivi (suggestions)

Ces indicateurs pourraient être suivis en comité projet pour objectiver l'évolution de la dette :

- Ratio **bugs récurrents / nouvelles features** par sprint
- **Couverture de tests** (objectif : progression via US-7-T2)
- **Temps moyen** de build et déploiement
- **Nombre de requêtes SQL** par endpoint critique (après audit Hibernate)
- **Vélocité** mesurée vs engagement (14 SP Sprint 1)

---

## 4. Bonnes pratiques Full-Stack

### 4.1 DevOps et CI/CD (Rachida — US-5, US-7, US-8)

| Pratique | Description | Lien sprint |
|----------|-------------|-------------|
| **Docker multi-stage** | Build Maven/npm dans une étape, runtime minimal (Corretto/Alpine + nginx) dans une autre. Réduit la taille des images et la surface d'attaque. | US-5 |
| **docker-compose** | Orchestration locale front + back + MySQL pour reproductibilité. | US5-T3 |
| **Pipeline GitHub Actions** | Jobs séparés front (lint, test, build) et back (Maven, tests). Quality gates avant merge. | US-7 |
| **Scans sécurité en CI** | Trivy (vulnérabilités images), Semgrep (SAST code). | US-7-T2 |
| **Flyway / Liquibase** | Migrations DB versionnées et automatisées — jamais de SQL manuel en production. | À évaluer |
| **Environnements séparés** | dev → staging (test) → prod, secrets dans GitHub, profils Spring (`application-test.yml`). | US-8 |
| **Smoke tests post-deploy** | Checklist automatisée après chaque déploiement. | US8-T4 |

**Questions de décision :**
- Quels quality gates minimum avant merge sur `main` (lint, tests unitaires, scan image) ?
- Flyway est-il déjà en place ou à introduire ?

**Sources :** [DevOps.dev — Multi-Stage Docker Builds](https://blog.devops.dev/optimizing-java-application-docker-images-with-multi-stage-builds-b50119828840) · [DevSecOps Spring+Angular example](https://github.com/georgesfk/secspringterracloud)

---

### 4.2 Qualité et accessibilité (Dimitry + Jorge — US-2, US-3)

| Pratique | Description | Lien |
|----------|-------------|------|
| Gestion erreurs unifiée | Composant Angular réutilisable + mapping HTTP/métier côté back | US-2 |
| Accessibilité WCAG AA | Contraste, navigation clavier, ARIA, labels | US-3, [projet.md](projet.md) L40-41 |
| Tests front | Vitest (remplace Karma, plus rapide) ou Jasmine + Testing Library | US-7-T2 |
| Tests back | JUnit + Mockito (unitaire), Testcontainers (intégration DB réelle en CI) | US-7-T2, US-8-T4 |
| Revue UX formalisée | Validation Jorge sur corrections visuelles | US1-T4 |

---

### 4.3 Organisation agile (Expert)

| Pratique | Lien projet |
|----------|-------------|
| Definition of Done partagée | [backlog.md](backlog.md) — section DoD |
| Vélocité mesurée et ajustée | 14 SP Sprint 1, règle +2 à +4 SP pour Sprint 2 |
| Veille intégrée aux rétrospectives | 1 tendance par sprint à challenger avec l'équipe |
| Comités projet fin de sprint | Présentation avancement, risques, mise à jour planification ([projet.md](projet.md) L120-124) |

---

## Synthèse — Matrice décisionnelle

Croisement des **4 axes de veille** avec les **11 User Stories** du backlog :

| US | Titre | Architecture | Performance | Dette | Full-Stack |
|----|-------|-------------|-------------|-------|------------|
| US-1 | Style CSS | — | OnPush, NgOptimizedImage | Dette UX | Lint CSS, revue Jorge |
| US-2 | Messages d'erreur | Contrat API | — | Dette UX | Composant unifié, mapping HTTP |
| US-3 | Accessibilité A11Y | — | — | Dette UX | WCAG AA, audit Jorge |
| US-4 | Nouveau thème | — | — | Reportée (Won't) | Angular theming |
| US-5 | Docker | Conteneurisation, prérequis scale | — | Dette deploy | Multi-stage, compose |
| US-6 | Microservices | Strangler, modular monolith, ACL | — | Dette structurelle | Contract tests, OpenAPI |
| US-7 | Pipeline CI/CD | — | Détection régressions | Dette process | GH Actions, Trivy, Semgrep |
| US-8 | Env. de test | — | — | Parallel run | Profils Spring, smoke tests |
| US-9 | Risque inondation | Bounded context `RiskCalculation` | JPA, cache, tuiles, index | — | Profiling d'abord |
| US-10 | Compatibilité navigateurs | — | @defer, polyfills | — | Matrice navigateurs |
| US-11 | Export données | Contexte `Export` | Batch JDBC | Luxueuse | Endpoint Spring + UI |

---

## Liens avec le backlog et les sprints

| Sprint | US prioritaires | Axes de veille les plus pertinents |
|--------|-----------------|-----------------------------------|
| **Sprint 1** (14 SP) | US-1, US-2, US-5 | Performance front (CSS), Full-Stack (Docker), Dette UX |
| **Sprint 2** (~17 SP) | US-3, US-7 | Accessibilité, CI/CD, Dette process |
| **Sprint 3** (~20 SP) | US-8, US-10 | Environnements, compatibilité navigateurs |
| **Sprint 4+** | US-6, US-9, US-11 | Architecture (Strangler), Performance géo, Export |

**GitHub :** les 50 issues (#2 à #51) du [Projet10 backlog](https://github.com/users/laurentcoufinal/projects/4) reflètent ce découpage.

### Questions transverses pour le prochain comité projet

1. L'audit technique (code + perf + format données géo) est-il planifié avant le Sprint 3 ?
2. Le monolithe modulaire est-il un prérequis explicite avant l'US-6 ?
3. Quels indicateurs de dette seront suivis à chaque rétrospective ?

---

## Plans de formation

Voir [formation.md](formation.md) — parcours modulaires par profil, **formation tests (JUnit, Cypress, TDD)** priorité S2.

## Comité projet

Voir [comite-projet.md](comite-projet.md) — point bloquant tests, adaptation Sprint 1, support de présentation.

## Analyse des risques

Voir [risque.md](risque.md) — spectre 7D, risques spécifiques, matrice de criticité et plan de prévention (juin 2026).

## Analyse comparative des solutions

Voir [choix.md](choix.md) — 3 solutions classées selon qualité, sécurité, temps, coût et risque (juin 2026).

---

## Bibliographie

### Architectures applicatives

- [microservices.io — Refactoring a monolith](https://microservices.io/refactoring/)
- [Microsoft Learn — Strangler Fig Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig)
- [knowledgelib.io — Decompose a Monolith into Microservices (2026)](https://knowledgelib.io/software/migrations/monolith-to-microservices/2026)
- [DEV Community — Realistic migration patterns](https://dev.to/sepehr/from-monolith-to-modular-monolith-to-microservices-realistic-migration-patterns-36f2)
- [Off-Nadir Delta — Modern WebGIS Architecture](https://offnadir-delta.com/blog/webgis-architecture-modern-stack)
- [BASF Digital Farming — STAC-based solution on EKS](https://noise.getoto.net/2025/10/22/basf-digital-farming-builds-a-stac-based-solution-on-amazon-eks/)

### Performances

- [Devops Monk — Spring Boot JPA Performance (2026)](https://blog.devops-monk.com/2026/05/spring-boot-jpa-performance/)
- [CodeWiz — 11 JPA Performance Killers](https://codewiz.info/blog/jpa-performance-anti-patterns/)
- [agfianf — Optimizing Satellite Maps (700K polygons)](https://agfianf.github.io/blog/2025/03/04/optimizing-satellite-maps-efficiently-rendering-700k-object-polygons-and-their-attributes/)
- [Zyra UI — Angular v21 Zoneless Guide](https://www.zyraui.dev/blog/angular-v21-zoneless-guide-remove-zonejs-use-signals)
- [EliteDev — Virtual Threads + Connection Pool](https://java.elitedev.in/java/complete-virtual-threads-guide-for-spring-boot-32-with-database-connection-pool-optimization/)

### Dette technique

- [Javra — Modernizing Legacy Software 2025](https://www.javra.com/modernizing-legacy-software-2025-low-risk-playbook/)
- [Pretius — Phased Legacy Modernization](https://pretius.com/blog/phased-legacy-modernization)
- [HTC — Strangler Fig & Micro-frontends](https://www.htcinc.com/blog/growing-out-of-legacy-unleashing-the-strangler-fig-micro-frontends-duo/)

### Bonnes pratiques Full-Stack

- [Innovirtuoso — Angular + Spring Boot Developer Guide](https://innovirtuoso.com/full-stack-development/complete-angular-spring-boot-developers-guide-build-scalable-full%e2%80%91stack-apps-that-ship-fast/)
- [DevOps.dev — Multi-Stage Docker Builds](https://blog.devops.dev/optimizing-java-application-docker-images-with-multi-stage-builds-b50119828840)
- [georgesfk/secspringterracloud — DevSecOps Spring+Angular](https://github.com/georgesfk/secspringterracloud)

---

*Document rédigé le 13/06/2026 dans le cadre du Projet 10 — CATASTERRE (OpenClassrooms).*
