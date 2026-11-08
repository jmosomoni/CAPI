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

## Bilan (à compléter en séance 4, 3 lignes)

- Nombre d'entrées et de propositions rejetées ou corrigées :
- Tâches où l'IA a fait gagner du temps :
- Tâches où l'IA a fait perdre du temps :
