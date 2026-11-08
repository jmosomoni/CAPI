# CAPI : planning poker

Application console de planning poker (projet M1). Python 3.10+, **aucune dépendance**.

## Lancer l'application

```bash
git clone <URL_DU_DEPOT>
cd <nom-du-depot>
python3 main.py                                  
python3 main.py exemples/backlog-bibliotheque.json
```

Sous Windows : `py main.py`.

L'application :
1. demande le nombre de joueurs (2 à 10) et leurs pseudos (non vides, sans doublon) ;
2. charge un backlog JSON et affiche la première fonctionnalité ;
3. fait voter chaque joueur à tour de rôle avec saisie masquée, puis révèle tous les votes.

La validation des votes (règle stricte, médiane...) arrive au sprint 2.

## Format du backlog JSON

```json
{
  "projet": "Bibliothèque en ligne",
  "fonctionnalites": [
    { "id": "F1", "titre": "Rechercher un livre par titre" }
  ]
}
```

- `fonctionnalites` : liste non vide, obligatoire ; chaque élément a un `id` et un `titre`.
- `projet` : facultatif.
- `estimation` : facultatif, rempli par l'application dans un sprint ultérieur.

Exemples dans `exemples/`.

## Cartes

`0 1/2 1 2 3 5 8 13 20 40 100 ? cafe`

## Organisation du code

```
capi/backlog.py   logique : chargement et validation du backlog
capi/partie.py    logique : joueurs, votes cachés, révélation
capi/console.py   interface console (seul fichier qui fait des input/print)
main.py           point d'entrée
```
