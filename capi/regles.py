# Usage de l'IA : moteur écrit avec l'aide de l'IA (Claude), avec l'autorisation de l'enseignant. Voir AI_LOG.md.
"""Moteur de règles : décide si un tour de vote valide la fonctionnalité. Aucune entrée/sortie console.

Pour ajouter une règle (moyenne, majorité...) : écrire une fonction votes -> Resultat
et l'ajouter au dictionnaire REGLES. Les règles existantes ne changent pas.
"""
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Resultat:
    valide: bool               # True : fonctionnalité validée ; False : il faut revoter
    valeur: str | None = None  # carte retenue si validée (ex. "5"), sinon None


REVOTE = Resultat(valide=False)

# Cartes qui portent un nombre, dans l'ordre croissant, avec leur valeur.
VALEURS = {
    "0": 0.0, "1/2": 0.5, "1": 1.0, "2": 2.0, "3": 3.0, "5": 5.0,
    "8": 8.0, "13": 13.0, "20": 20.0, "40": 40.0, "100": 100.0,
}


def unanimite(votes: list[str]) -> Resultat:
    """Validé seulement si tous les joueurs ont posé la même carte."""
    if len(set(votes)) == 1:
        return Resultat(valide=True, valeur=votes[0])
    return REVOTE


def carte_la_plus_proche_au_dessus(valeur: float) -> str:
    """Renvoie la plus petite carte dont la valeur est >= valeur (ex. 4 -> "5")."""
    for carte, v in VALEURS.items():  # parcours dans l'ordre croissant
        if v >= valeur:
            return carte
    return "100"


def mediane(votes: list[str]) -> Resultat:
    """Valeur du milieu ; nombre pair : moyenne des deux du milieu, arrondie à la carte au-dessus."""
    valeurs = sorted(VALEURS[v] for v in votes)
    n = len(valeurs)
    if n % 2 == 1:
        milieu = valeurs[n // 2]
    else:
        milieu = (valeurs[n // 2 - 1] + valeurs[n // 2]) / 2
    return Resultat(valide=True, valeur=carte_la_plus_proche_au_dessus(milieu))


# Règle appliquée à partir du 2e tour. Ajouter une règle = ajouter une ligne ici.
REGLES: dict[str, Callable[[list[str]], Resultat]] = {
    "strict": unanimite,
    "mediane": mediane,
}


def evaluer_votes(votes: list[str], regle: str, tour: int) -> Resultat:
    """votes : cartes révélées (ex. ["3", "5", "8"]) ; regle : "strict" ou "mediane" ; tour : 1, 2, 3..."""
    if not votes:
        raise ValueError("Aucun vote à évaluer.")
    if regle not in REGLES:
        raise ValueError(f"Règle inconnue : {regle}")

    # « ? » ou « cafe » : pas de nombre à retenir, on revote (table de décision, ligne 9).
    if any(v not in VALEURS for v in votes):
        return REVOTE

    # Premier tour : unanimité, quelle que soit la règle choisie.
    if tour == 1:
        return unanimite(votes)

    return REGLES[regle](votes)
