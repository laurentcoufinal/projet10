# Veille technologique CATASTERRE — Présentation Mermaid

> Résumé de [veille.md](../veille.md) · juin 2026 · Export OpenOffice

## Export OpenOffice

| Méthode | Fichier | Action |
|---------|---------|--------|
| **Writer / Impress** | `veille-openoffice.html` | Fichier → Ouvrir dans LibreOffice/OpenOffice → Enregistrer sous `.odt` ou `.odp` |
| **Images vectorielles** | `svg/*.svg` | Insertion → Image → choisir chaque SVG (10 diagrammes) |
| **Source Mermaid** | `diagrams/*.mmd` | Éditer et régénérer via `scripts/generate-veille-mermaid.sh` |
| **Markdown** | Ce fichier | Copier les blocs ```mermaid dans un outil compatible |

---

## 1. Contexte projet

```mermaid
flowchart TB
    subgraph app [CATASTERRE]
        A[Visualisation catastrophes naturelles]
        B[Imagerie satellite]
        C[Notaires et immobilier]
    end
    subgraph stack [Stack]
        D[Angular front]
        E[Spring Boot back]
        F[MySQL]
    end
    subgraph equipe [Equipe]
        G[Dimitry front]
        H[Rachida DevOps back]
        I[Jorge UX]
        J[Expert agile]
    end
    subgraph contraintes [Contraintes brownfield]
        K[Lenteurs client]
        L[Erreurs frequentes]
        M[Roadmap Docker puis microservices]
    end
    app --> stack
    equipe --> app
    contraintes --> app
```

| Dimension | Constat |
|-----------|---------|
| Maturité | Brownfield < 1 an |
| Stack | Angular · Spring Boot · MySQL |
| Roadmap | Docker → microservices |
| Backlog | 11 US · 75 SP |

---

## 2. Quatre axes de veille

```mermaid
mindmap
  root((Veille CATASTERRE))
    Architecture
      Monolithe modulaire
      Strangler Fig
      ACL
      Geo COG PMTiles STAC
      OpenAPI
    Performance
      Angular zoneless OnPush defer
      Spring JPA N+1 cache
      GeoJSON vs tuiles
      Metriques LCP CLS INP
    Dette technique
      Pas big bang
      Audit structural
      TIME MoSCoW
      Parallel run US-8
    Full-Stack
      Docker multi-stage CI/CD
      Trivy Semgrep
      WCAG AA tests
      DoD veille retro
```

---

## 3. Architecture — Roadmap

```mermaid
flowchart LR
    subgraph etapeA [Etape A Sprint 1-3]
        A1[Docker US-5]
        A2[CI build US-7-T1]
        A3[Modules internes]
    end
    subgraph etapeB [Etape B Sprint 4+]
        B1[Monolithe modulaire]
        B2[Strangler Fig]
        B3[Premier service RiskCalculation ou ImageIngestion]
    end
    subgraph cible [Cible long terme]
        C1[API Gateway]
        C2[PMTiles CDN]
        C3[Microservices US-6]
    end
    etapeA --> etapeB --> cible
```

### Strangler Fig

```mermaid
flowchart TB
    L[Legacy monolithe] --> F[Facade API Gateway]
    F --> S1[Phase Shadow 0 pct trafic]
    S1 --> S2[Phase Canary 5 a 50 pct]
    S2 --> S3[Phase Cutover 100 pct]
    S3 --> NS[Nouveau service extrait]
    ACL[Anti-Corruption Layer] -.-> F
    ACL -.-> NS
```

### Bounded contexts

```mermaid
flowchart TB
    subgraph contexts [Bounded contexts a valider]
        IC[ImageIngestion]
        RC[RiskCalculation US-9]
        UA[UserAccess auth]
        EX[Export US-11]
        PR[Presentation US-1 US-2 US-3 US-10]
    end
    MONO[Monolithe Spring Boot] --> IC
    MONO --> RC
    MONO --> UA
    MONO --> EX
    MONO --> PR
    ANG[Angular] --> PR
```

---

## 4. Performance

```mermaid
flowchart TB
    subgraph front [Front Angular Dimitry]
        F1[Zoneless Signals]
        F2[OnPush et defer carte]
        F3[NgOptimizedImage satellite]
    end
    subgraph back [Back Spring Rachida]
        B1[N+1 OSIV false]
        B2[Cache Caffeine Redis]
        B3[Virtual threads Java 21]
        B4[Batch JDBC export]
    end
    subgraph geo [Geo spatial]
        G1[GeoJSON massif 700k polygones]
        G2[Tuiles PMTiles MVT]
        G3[Index spatial MySQL]
        G4[CDN tuiles]
    end
    G1 -->|probleme| LENT[Lenteurs carte]
    G2 -->|solution| RAPIDE[Charge divisee 10 a 25]
    front --> LENT
    back --> US9[US-9 profiling]
```

| Métrique | Seuil indicatif |
|----------|-----------------|
| LCP | ≤ 2,5 s |
| CLS | ≤ 0,1 |
| INP | ≤ 200 ms |

---

## 5. Dette technique

```mermaid
flowchart LR
    subgraph haute [Dette haute S1-S2]
        D1[UX US-1 US-2 US-3]
        D2[Deploy US-5]
        D3[Process US-7 US-8]
    end
    subgraph moyenne [Dette moyenne S4+]
        D4[Structure US-6]
    end
    subgraph luxueuse [Dette luxueuse S4+]
        D5[Metier US-9 US-11]
        D6[Reportee US-4 theme]
    end
    PRIN[Pas de big bang] --> haute
    PRIN --> moyenne
    AUDIT[Audit structural -30 pct] --> D4
    ENV[Parallel run US-8] --> D3
```

---

## 6. Full-Stack DevOps

```mermaid
flowchart TB
    DEV[Developpement] --> CI[GitHub Actions US-7]
    CI --> LINT[Lint front back]
    CI --> TEST[Tests unitaires integration]
    CI --> SCAN[Trivy Semgrep]
    CI --> BUILD[Build Docker US-5]
    BUILD --> STG[Env staging US-8]
    STG --> SMOKE[Smoke tests US8-T4]
    SMOKE --> PROD[Production]
    FORM[Formation tests S2] -.-> TEST
```

---

## 7. Veille × Sprints

```mermaid
gantt
    title Veille x Sprints CATASTERRE
    dateFormat YYYY-MM-DD
    axisFormat %d/%m
    section Sprint1
    US-1 US-2 US-5           :s1, 2026-06-01, 14d
    FORM-T0 PROC-T2          :s1f, 2026-06-01, 14d
    section Sprint2
    US-3 US-7 TEST-T1 T2     :s2, 2026-06-15, 14d
    Formation T-DI1 T-RA1    :s2f, 2026-06-15, 14d
    section Sprint3
    US-8 US-10 TEST-T3       :s3, 2026-06-29, 14d
    section Sprint4plus
    US-6 US-9 US-11          :s4, 2026-07-13, 28d
```

---

## 8. Matrice User Stories × axes

| US | Titre | Architecture | Performance | Dette | Full-Stack |
|----|-------|-------------|-------------|-------|------------|
| US-1 | Style CSS | — | OnPush, NgOptimizedImage | Dette UX | Lint, revue Jorge |
| US-2 | Messages erreur | Contrat API | — | Dette UX | Composant + mapping |
| US-3 | Accessibilité | — | — | Dette UX | WCAG AA |
| US-5 | Docker | Conteneurisation | — | Dette deploy | Multi-stage |
| US-6 | Microservices | Strangler, ACL | — | Dette structurelle | OpenAPI |
| US-7 | CI/CD | — | Anti-régression | Dette process | GH Actions, scans |
| US-8 | Env. test | — | — | Parallel run | Smoke tests |
| US-9 | Risque inondation | RiskCalculation | JPA, tuiles | — | Profiling |
| US-10 | Compatibilité | — | @defer | — | Matrice navigateurs |
| US-11 | Export | Export | Batch JDBC | Luxueuse | API + UI |

---

## Questions comité

1. Audit code + perf + données géo avant Sprint 3 ?
2. Monolithe modulaire prérequis explicite avant US-6 ?
3. Indicateurs dette suivis en rétrospective ?

---

*Source : veille.md · Projet 10 CATASTERRE · juin 2026*
