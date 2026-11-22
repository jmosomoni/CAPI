# Usage de l'IA : interface écrite avec l'aide de l'IA (Claude), avec l'autorisation de l'enseignant. Voir AI_LOG.md.
"""Moteur de règles : décide si un tour de vote valide la fonctionnalité. Aucune entrée/sortie console."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Resultat:
    valide: bool               # True : fonctionnalité validée ; False : il faut revoter
    valeur: str | None = None  # carte retenue si validée (ex. "5"), sinon None


def evaluer_votes(votes: list[str], regle: str, tour: int) -> Resultat:
    """votes : cartes révélées (ex. ["3", "5", "8"]) ; regle : "strict" ou "mediane" ; tour : 1, 2, 3..."""
    raise NotImplementedError("Moteur de règles pas encore implémenté.")
