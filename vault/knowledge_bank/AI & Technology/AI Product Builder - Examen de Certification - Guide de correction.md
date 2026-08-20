---
type: notion-import
notion-id: 3758924af01480e18311ffa29cf6c4a8
source-url: https://app.notion.com/p/lewagon/AI-Product-Builder-Examen-de-Certification-Guide-de-correction-3758924af01480e18311ffa29cf6c4a8
imported: 2026-07-23
---
# AI Product Builder - Examen de Certification - Guide de correction
> 🎯 Ce guide est à usage exclusif des correcteurs de l'examen **AI Product Builder** (RNCP39261BC01). Il détaille, pour chaque bloc de compétences, quelles questions/livrables sont à évaluer et les critères d'attribution de la note.
---
# 🔑 Fonctionnement de la correction sur Kitt
La correction s'effectue **bloc de compétence par bloc de compétence**. Pour chaque bloc, Kitt affiche les livrables soumis par le candidat, et vous devez attribuer une note parmi trois choix :
NotationSignificationDeniedLa compétence n'est pas démontrée. Les livrables sont absents, insuffisants ou hors-sujet.In process of acquisitionLa compétence est partiellement démontrée. Des éléments pertinents sont présents mais incomplets ou maladroits.AcquiredLa compétence est pleinement démontrée. Les livrables répondent aux attendus avec suffisamment de rigueur et de cohérence.
> ⚠️ Si un livrable **n'a pas été soumis**, Kitt affiche *"No submissions for [nom du livrable]"*.
---
## ⚠️ Livrables de projet éliminatoires
Les livrables de la **Partie 1 — Réflexion sur le projet** (vidéo de démo et la capture d’écran de leur app) sont **éliminatoires** pour tous les blocs auxquels ils sont rattachés.
Si le PRD, la vidéo de démo ou la capture d'écran est **absent(e) ou inaccessible**, tout bloc dépendant de ce livrable doit être noté **🔴 Denied**, sans exception, quelles que soient les autres réponses du candidat.
---
# 📋 Structure de l'examen — rappel rapide
- **Partie 1 — Réflexion sur le projet** (30 min) : vidéo de démo, PRD, roadmap, capture d'écran de l'application
- **Partie 2 — Quiz** (30 min) : 20 questions QCM sur les 5 modules du programme
- **Partie 3 — Case Study** (30 min) : 9 questions sur un brief e-commerce fictif
> **Brief du case study :** *Une PME e-commerce (~50 000 commandes/mois) souhaite automatiser son support client. Équipe de 5 agents, ~300 tickets/jour. 70 % de demandes répétitives (suivi de commande, retours, disponibilité produit). L'entreprise veut un assistant AI capable de répondre aux demandes simples, d'accéder à l'historique commandes/catalogue, et d'escalader les cas complexes vers un agent humain.*
---
# 🧩 Blocs de compétences — Guide de correction
## C1 — Organiser et conduire des réunions de cadrage
> *Organiser et conduire des réunions de cadrage avec les clients et/ou les utilisateurs potentiels de l'application pour identifier et documenter précisément leurs besoins et les problématiques à résoudre, en utilisant des techniques de questionnement et d'écoute active, afin de garantir une compréhension complète des attentes.*
**Livrables évalués :** PRD · CS Problème & parties prenantes · CS KPI principal
🔴 **Denied** : Le PRD est absent ou inaccessible ; **ou** le candidat ne parvient pas à identifier les parties prenantes (au moins 1 identifiée) et le problème dans le case study ; **ou** le KPI proposé est absent, vague ou non-mesurable.
🟢 **Acquired** : Le PRD contient un problème utilisateur clairement formulé et au moins un persona identifié. Dans le case study, le candidat identifie le problème (volume de tickets répétitifs) et au moins une partie prenante (agents support, clients, managers), et propose un KPI mesurable avec un moyen de le suivre.
---
## C2 — Analyser la pertinence des demandes clients
> *Analyser la pertinence des demandes clients en évaluant leur faisabilité technique et leur impact sur le projet grâce à des critères d'analyse spécifiques pour faire ressortir les besoins implicites et proposer des alternatives optimisées.*
**Livrables évalués :** PRD · CS Problème & parties prenantes · CS Contraintes techniques de la stack · CS Roadmap V2
🔴 **Denied** : Le PRD est absent ou inaccessible (éliminatoire) ; **ou** le scope MVP est absent du PRD ; **ou** le candidat ne cite aucune contrainte technique pertinente dans le case study ; **ou** la roadmap V2 est absente.
🟢 **Acquired** : Le PRD contient un scope MVP priorisé avec justification des choix. Dans le case study, au moins 3 contraintes techniques pertinentes sont identifiées (volume, latence, budget, intégrations existantes), et la roadmap V2 propose 2 améliorations concrètes avec estimation d'effort (S/M/L) et justification articulant valeur utilisateur et faisabilité technique.
---
## C3 — Réaliser une maquette de l'application web
> *Réaliser une maquette de l'application web à l'aide d'un outil de prototypage et en intégrant les principes d'UX/UI design afin de tester le fonctionnement de l'application auprès de l'équipe technique et du client.*
**Livrables évalués :** Vidéo de démo · PRD · Capture d'écran de l'application · CS Solution low-code préconisée
🔴 **Denied** : La vidéo de démo est absente ou inaccessible - si la vidéo est absente, se référer au screenshot (vidéo ou screenshot manquant = éliminatoire) ; **ou** la capture d'écran est absente (éliminatoire) ; **ou** la solution low-code proposée dans le case study est absente ou ne décrit pas le flux email/chat → IA → réponse.
🟢 **Acquired** : La vidéo est accessible, dure max 5 min, et montre le flux utilisateur complet avec au moins une feature IA fonctionnelle en production. La capture d'écran montre une interface de l'application déployée. Le PRD décrit clairement la solution IA principale. Dans le case study, un outil low-code est préconisé, le flux automatisé est décrit, et le choix est justifié.
---
## C4 — Intégrer les pratiques d'accessibilité et d'éco-conception
> *Intégrer les pratiques d'accessibilité (directives WCAG), d'éco-conception et de responsive design lors de la conception des maquettes en prenant en compte les retours des utilisateurs et/ou des clients pour optimiser l'expérience utilisateur de tous les publics, y compris les personnes en situation de handicap.*
**Livrable évalué :** CS Accessibilité & WCAG
🔴 **Denied** : La réponse est absente ; **ou** les critères cités sont génériques, hors-sujet, ou en nombre insuffisant (moins de 3).
🟢 **Acquired** : Le candidat identifie **3 critères WCAG pertinents** pour une interface web utilisée par des agents support et des clients (ex. contraste suffisant AA, navigation entièrement au clavier, textes alternatifs sur les images, libellés de champs de formulaire, messages d'erreur explicites, compatibilité avec les lecteurs d'écran).
---
## C5 — Concevoir le schéma de la base de données
> *Concevoir le schéma de la base de données relationnelle, en définissant les tables, les colonnes, et les relations entre elles, en utilisant des outils de modélisation comme MySQL Workbench ou ER Studio, pour structurer efficacement les données nécessaires au parcours utilisateur.*
**Livrables évalués : **Schéma de BDD (Google Slides)
🔴 **Denied** : Le lien est absent ou inaccessible ; **ou** le schéma de base de données n'est pas complété dans le template.
🟢 **Acquired** : Le lien est accessible publiquement. Le schéma de BDD est complété avec des tables cohérentes avec le brief (ex. commandes, clients, tickets, produits), et les colonnes et relations entre tables sont définies de manière logique.
---
## C6 — Créer un cahier des charges détaillé
> *Créer un cahier des charges détaillé (spécificité technique, budget, délai) et un prototype en utilisant un outil collaboratif comme Notion et un logiciel de prototypage comme Figma afin d'obtenir une validation finale des clients avant de démarrer le développement de l'application web.*
**Livrables évalués :** PRD · CS Solution low-code préconisée · CS Contraintes techniques de la stack
🔴 **Denied** : Le PRD est absent ou inaccessible (éliminatoire) ; **ou** le PRD ne couvre que superficiellement le projet (moins de 3 éléments structurants présents) ; **ou** ni la solution low-code ni les contraintes de stack ne sont traitées dans le case study.
🟢 **Acquired** : Le PRD couvre au minimum ces 5 éléments : problème utilisateur, persona(s), solution IA principale, KPIs mesurables, scope MVP priorisé. Dans le case study, la solution proposée est structurée et argumentée, et les contraintes de stack guident le choix de manière logique.
---
## C7 — Identifier les évolutions clés du développement web et de l'IA
> *Identifier les évolutions clés du développement web et de l'IA en analysant des sources d'information spécialisées pour alimenter et challenger la conception de l'application web.*
**Livrables évalués :** Quiz AI Product Builder · CS Choix du modèle IA · CS Optimisation tokens
🔴 **Denied** : Le quiz n'est pas complété ou le score est insuffisant (<50% de bonnes réponses) ; **ou** le candidat ne cite aucun modèle LLM ou aucune technique d'optimisation pertinente dans le case study.
🟢 **Acquired** : Score satisfaisant au quiz (>50%). Dans le case study, un modèle LLM est préconisé avec au moins 2 critères de choix pertinents (coût, taille de contexte, multilinguisme, latence, confidentialité). Une technique d'optimisation de tokens concrète est proposée et expliquée (ex. RAG, cache sémantique, compression de prompt, chunking).
---
## C8 — Vérifier la conformité RGPD et les standards de sécurité
> *Vérifier que le projet respecte les standards de sécurité et de respect du RGPD, d'accessibilité web, et d'éco-conception en utilisant des checklists de conformité et des sessions de formation pour l'équipe de développement, afin de garantir que l'application respecte les exigences légales et éthiques tout au long de son cycle de développement.*
**Livrables évalués :** Quiz AI Product Builder · CS Template RGPD
🔴 **Denied** : Le quiz n'est pas complété ou le score est insuffisant (<50%) ; **ou** le lien vers le template est absent ou inaccessible ; **ou** la section RGPD du template est vide ou ne cite que des risques génériques sans mesures associées.
🟢 **Acquired** : Score satisfaisant au quiz sur les questions RGPD/sécurité/guardrails (>50%). Le template est accessible et la section RGPD identifie au moins 3 risques spécifiques au brief (données personnelles clients, historique de commandes, logs de conversations) avec des mesures de protection concrètes (anonymisation, minimisation des données, droit à l'effacement, sécurisation des API, gestion du consentement).
---
# 🗺️ Tableau récapitulatif — Livrables par compétence
BlocLivrables évaluésLivrables éliminatoiresC1PRD · CS Problème & parties prenantes · CS KPI principalC2PRD · CS Problème & parties prenantes · CS Contraintes stack · CS Roadmap V2C3Vidéo de démo · PRD · D. Capture d'écran · CS Solution low-codeVidéo de démo, ou Capture d'écran absent(e)C4CS Accessibilité & WCAG—C5CS Template RGPD et Schéma de BDD—C6PRD · CS Solution low-code · CS Contraintes stackC7Quiz · CS Choix du modèle IA · CS Optimisation tokens—C8Quiz · CS Template RGPD et Schéma de BDD—
---
# ✅ Bonnes pratiques de correction
- **Évaluer l'ensemble des livrables** d'un bloc avant de noter.
- Si un livrable éliminatoire (vidéo de démo ou capture d'écran) est absent ou inaccessible, noter **🔴 Denied immédiatement** pour tous les blocs concernés.
- En cas de livrable non-éliminatoire absent, évaluer la compétence à partir des autres livrables du bloc.
## Related
- [[AI Product Builder]]
