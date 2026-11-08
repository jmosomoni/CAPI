# CAPI : planning poker

Application console de planning poker.

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
  "projet": "CAPI : poker",
  "fonctionnalites": [
    { "id": "US-01", "titre": "Saisir le nombre de joueurs et leurs pseudos" },
    { "id": "US-02", "titre": "Charger un backlog JSON et afficher la première fonctionnalité" },
    { "id": "US-04", "titre": "Voter en secret puis révéler les votes" }
  ]
}
```

- `projet` : facultatif ; le nom du projet dont on estime le backlog.
- `fonctionnalites` : obligatoire, liste non vide ; chaque élément a un `id` unique et un `titre`.
- `estimation` : facultatif ; c'est la difficulté retenue après le vote (par exemple `"2"`). Absente au départ, elle sera ajoutée par l'application quand la fonctionnalité aura été estimée.




## Cartes

`0 1/2 1 2 3 5 8 13 20 40 100 ? cafe`

## Organisation du code

```
capi/backlog.py   logique : chargement et validation du backlog
capi/partie.py    logique : joueurs, votes cachés, révélation
capi/console.py   interface console (seul fichier qui fait des input/print)
main.py           point d'entrée
```
