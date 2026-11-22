# AI_LOG.md : journal d'usage de l'IA

> À placer à la racine du dépôt. À remplir **au fil de l'eau**, pas en fin de projet. Une entrée par tâche (pas par message), en 5 lignes.
> Rappel : l'IA est autorisée pour le **code de production** et la **configuration d'outils** uniquement. Qui a fait la demande, les fichiers touchés et les commits se retrouvent dans l'historique Git : ne les recopiez pas.

## Outils utilisés (à remplir une fois)

| Outil | Modèle (si connu) | Mode (autocomplétion, chat, agent) |
|---|---|---|
| Claude (claude.ai) | Claude Opus 5.5 | chat |

Fichier d'instructions pour agent versionné (`CLAUDE.md`, `AGENTS.md`...) : non

## Entrées

### 2026-11-08 : saisie des joueurs et de leurs pseudos (US-01)

- **Demande (résumé fidèle)** : le code qui demande le nombre de joueurs puis leurs pseudos.
- **Résultat** : accepté tel quel
- **Ce que nous avons vérifié** : lancement de l'application avec 3 joueurs, essai d'un pseudo vide et d'un pseudo en double.
- **Ce que nous avons changé ou rejeté, et pourquoi** :  ajout de « (2 à 10) » dans la question du nombre de joueurs, pour connaitre la limite avant de faire une erreur de saisie.

### 2026-11-08 : chargement du backlog JSON (US-02)

- **Demande (résumé fidèle)** : le code qui lit le fichier JSON du backlog et affiche la première fonctionnalité.
- **Résultat** : accepté tel quel
- **Ce que nous avons vérifié** : lancement avec le backlog d'exemple, puis avec un nom de fichier qui n'existe pas.
- **Ce que nous avons changé ou rejeté, et pourquoi** : rien.

### 2026-11-08 : vote caché puis révélation (US-04)

- **Demande (résumé fidèle)** : chaque joueur choisit sa carte sans que les autres la voient, puis tous les votes s'affichent en même temps.
- **Résultat** : accepté tel quel
- **Ce que nous avons vérifié** : essai à la main avec 3 joueurs.
- **Ce que nous avons changé ou rejeté, et pourquoi** : Un joueur pouvait voter deux fois et son second vote écrasait le premier sans prévenir ; j'ai ajouté un refus,

### 2026-11-22 : table de décision et tests du moteur de règles (US-05, US-06, US-07)

- **Demande (résumé fidèle)** : compléter la table de décision à partir de mes règles de R1 et écrire un test par ligne, avant le code. Usage autorisé par l'enseignant par mail.
- **Résultat** : accepté tel quel
- **Ce que nous avons vérifié** : chaque test correspond à une ligne de la table ; les 10 tests échouent avant l'implémentation (commit rouge d5f6bbb).
- **Ce que nous avons changé ou rejeté, et pourquoi** : la carte « ? » entraîne un revote, pour qu'un joueur qui ne sait pas estimer puisse poser ses questions.

### 2026-11-22 : configuration de la CI GitHub Actions (US-06, US-07)

- **Demande (résumé fidèle)** : adapter l'exemple de workflow de la consigne à mon projet, avec les actions épinglées sur un SHA.
- **Résultat** : modifié
- **Ce que nous avons vérifié** : la CI se lance à chaque push et elle est rouge tant que le moteur n'est pas codé.
- **Ce que nous avons changé ou rejeté, et pourquoi** : pas de `requirements.txt` ni de `pytest` comme dans l'exemple, car le projet n'utilise que la bibliothèque standard de Python.

### 2026-11-22 : moteur de règles et branchement dans le jeu (US-03, US-06, US-07)

- **Demande (résumé fidèle)** : implémenter le moteur pour faire passer mes tests, sans les modifier, puis le brancher dans la boucle de vote avec le choix de la règle au lancement.
- **Résultat** : accepté tel quel
- **Ce que nous avons vérifié** : les 10 tests passent sans modification du fichier de tests ; partie complète jouée en règle médiane ; CI verte sur la PR #1.
- **Ce que nous avons changé ou rejeté, et pourquoi** : `tests/test_regles.py` avait été modifié par erreur en local ; je l'ai remis dans l'état du commit rouge avant le commit du moteur.

## Bilan (à compléter en séance 4, 3 lignes)

- Nombre d'entrées et de propositions rejetées ou corrigées :
- Tâches où l'IA a fait gagner du temps :
- Tâches où l'IA a fait perdre du temps :
