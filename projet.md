1. Introduction au projet 2
1.1. Contexte de l'entreprise 2
1.2. Problématique actuelle 2
1.3. Objectifs de l’évolution de l’application 2
1.3.1. Améliorer l'expérience utilisateur 2
1.3.2. Garantir la disponibilité et améliorer la maintenabilité et l'évolutivité 3
1.3.3. Fiabiliser l’organisation du développement 3
2. L'équipe 3
2.1. Vous - Expert en développement logiciel 3
2.2. Membres de l'équipe : 3
2.2.1. Dimitry 3
2.2.2. Rachida 4
2.2.3. Jorge 4
3. Objectifs et tâches initiales 5
3.1. Analyse du Product Backlog 5
3.2. Planification et gestion 5
3.3. Suivi du projet 5
1. Introduction au projet
1.1. Contexte de l'entreprise
CATASTERRE est une entreprise innovante spécialisée dans la visualisation de
catastrophes naturelles à l'aide de technologies satellitaires.
L'entreprise fournit des services cruciaux en permettant à des notaires,
agences immobilières et autres professionnels d'accéder à des images
satellites traitées pour évaluer les risques associés à des propriétés
immobilières.
L'application web récemment lancée par CATASTERRE est conçue pour
récupérer, analyser et présenter ces images de manière intuitive et accessible.
1.2. Problématique actuelle
Malgré son lancement il y a moins d'un an, l'application CATASTERRE fait face
à des problèmes importants. Les clients signalent des lenteurs, des erreurs
fréquentes et des instabilités qui entravent leur expérience utilisateur.
Le manque d'évolution et de maintenance adéquate de l'application entraîne
également un risque de perte de compétitivité sur le marché.
1.3. Objectifs de l’évolution de l’application
Le projet d’évolution d’application vise à résoudre ces problèmes en améliorant
l’UX, l’architecture et le DevOps. Les principaux objectifs sont les suivants.
1.3.1. Améliorer l'expérience utilisateur
Nous devons corriger les erreurs fréquentes, comme les erreurs de styles sur
les pages web (fontes non-visibles, etc.), l’affichage des messages d’erreur.
Nous devons aussi améliorer l’UX de nos pages web, pour que le parcours
utilisateur soit fluide, y compris pour les utilisateurs à accessibilité réduite.
L’ajout de nouveau thème n’est cependant pas une priorité pour l’instant, car le
dark theme est déjà implémenté.
1.3.2. Garantir la disponibilité et améliorer la maintenabilité
et l'évolutivité
Il faudrait idéalement séparer notre application en plusieurs services. Nous
procéderons en 2 étapes.
A. D’abord, nous allons encapsuler l’application dans un container docker,
ce qui nous permettra de scaler l’application, et améliorer la disponibilité
du service à court terme.
B. Ensuite, dans un deuxième temps, nous procéderons à la séparation des
responsabilités en différents services, au sein même de l’application.
1.3.3. Fiabiliser l’organisation du développement
Il est important que nous identifions en amont les bugs et les problèmes de
stabilité. Cela passe par la mise en place d’une pipeline d'intégration continue,
et, dans un deuxième temps, d’environnement de tests séparés de
l’environnement de production.
2. L'équipe
2.1. Vous - Expert en développement logiciel
Votre rôle est crucial pour piloter cette transformation. Vous serez responsable
de la mise en œuvre des pratiques agiles, de la coordination entre les équipes,
et de l'amélioration continue des processus.
Vous devrez également vous assurer que les objectifs de performance et de
qualité sont atteints et que les attentes des clients sont satisfaites.
2.2. Membres de l'équipe :
2.2.1. Dimitry
Profil : Développeur front-end
Années d’expérience : 3
Spécialisation : Développement frontend avec une expertise en Angular
Langages de programmation maîtrisés : HTML, CSS, JavaScript
Frameworks de programmation maîtrisés : Angular, RxJS
Outils maîtrisés : Git
Environnement système : Windows, Linux (Debian)
Rôle dans l'équipe : Dimitry contribuera au projet en mettant en œuvre les
améliorations nécessaires au niveau du code front-end. Son expertise en
Angular sera précieuse pour améliorer la performance du front-end.
2.2.2. Rachida
Profil : DevOps
Années d’expérience : 5
Langages de programmation maîtrisés : Java, GoLang
Frameworks de programmation maîtrisés : openshift
Outils maîtrisés : MySQL, Github Action, Jenkins, Travis, AWS, k8s
Environnement système : Linux (Debian), Docker
Rôle dans l'équipe : Rachida contribuera au projet en mettant en œuvre les
améliorations nécessaires au niveau de l'environnement de développement (CI)
et de production (encapsulation de l’application, scalabilité, disponibilité).
Son expertise en Java sera précieuse pour résoudre les problèmes de
performance du back-end en utilisant Spring Boot. Elle travaillera également
sur la sécurisation du back-end et des bases de données en utilisant Spring
Data et Spring Security.
2.2.3. Jorge
Profil : UX Designer
Années d’expérience : 12
Spécialisation : Conception de front-end en créant des wireframes et des
Maquettes avec Figma
Outils maîtrisés : Figma, Miro
Environnement système : Windows
Rôle dans l'équipe : Jorge apportera son expertise en UX design pour évaluer
et améliorer les interfaces utilisateur.
3. Objectifs et tâches initiales
3.1. Analyse du Product Backlog
Objectif : Vous devez examiner les tickets et les besoins des clients pour créer
un backlog technique détaillé. Vous devez également prioriser les tâches en
fonction de leur impact sur la performance et la satisfaction client.
Actions :
● Découpez les tickets en tâches techniques plus petites.
● Définissez les critères de succès pour chaque tâche.
● Établissez un Sprint Backlog clair pour le premier sprint.
3.2. Planification et gestion
Objectif : Vous êtes chargé d’organiser le cadrage du projet, de définir le
périmètre, et d’établir une planification des sprints efficace.
Actions :
● Découpez le projet en macro-tâches (epics).
● Estimez le budget et les charges de travail.
● Planifiez les sprints en fonction des priorités et des capacités de
l'équipe.
3.3. Suivi du projet
Objectif : Vous devez assurer un suivi régulier de l’avancement du projet et de
la performance des sprints.
Actions : Organisez des comités projet à la fin de chaque sprint afin de :
● présenter l’avancement ;
● discuter des risques identifiés ;
● mettre à jour la planification des sprints en fonction des nouvelles
informations.