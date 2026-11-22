# Usage de l'IA : code écrit avec l'aide de l'IA (Claude), avec l'autorisation de l'enseignant. Voir AI_LOG.md.
"""Partie, joueurs et votes (US-01, US-04), tours de vote (US-05 à US-08). Aucune entrée/sortie console ici."""
from dataclasses import dataclass, field

from capi.backlog import Backlog, Fonctionnalite
from capi.regles import REGLES, Resultat, evaluer_votes

CARTES = ("0", "1/2", "1", "2", "3", "5", "8", "13", "20", "40", "100", "?", "cafe")
NB_JOUEURS_MIN = 2
NB_JOUEURS_MAX = 10


class SaisieInvalide(Exception):
    """Donnée de partie refusée (nombre de joueurs, pseudo, carte, règle...)."""


@dataclass
class Joueur:
    pseudo: str


@dataclass
class Partie:
    joueurs: list[Joueur]
    backlog: Backlog
    regle: str = "strict"
    index_courant: int = 0
    tour: int = 1
    _votes: dict[str, str] = field(default_factory=dict)

    def __post_init__(self):
        if self.regle not in REGLES:
            raise SaisieInvalide(f"Règle inconnue : {self.regle}")

    @property
    def fonctionnalite_courante(self) -> Fonctionnalite | None:
        """La fonctionnalité en cours d'estimation, ou None quand tout le backlog est estimé."""
        if self.est_terminee():
            return None
        return self.backlog.fonctionnalites[self.index_courant]

    def est_terminee(self) -> bool:
        return self.index_courant >= len(self.backlog.fonctionnalites)

    def voter(self, pseudo: str, carte: str) -> None:
        if pseudo not in {j.pseudo for j in self.joueurs}:
            raise SaisieInvalide(f"Joueur inconnu : {pseudo}")
        if pseudo in self._votes:
            raise SaisieInvalide(f"{pseudo} a déjà voté pour ce tour.")
        if carte not in CARTES:
            raise SaisieInvalide(f"Carte inconnue : {carte}")
        self._votes[pseudo] = carte

    def tous_ont_vote(self) -> bool:
        return len(self._votes) == len(self.joueurs)

    def reveler(self) -> dict[str, str]:
        """Rend les votes dans l'ordre des joueurs ; interdit tant qu'un joueur n'a pas voté."""
        if not self.tous_ont_vote():
            raise SaisieInvalide("Tous les joueurs n'ont pas encore voté.")
        return {j.pseudo: self._votes[j.pseudo] for j in self.joueurs}

    def nouveau_tour(self) -> None:
        self._votes.clear()

    def cloturer_tour(self) -> Resultat:
        """Applique le moteur de règles aux votes révélés.

        Validé : l'estimation est enregistrée et on passe à la fonctionnalité suivante (tour 1).
        Revote : on reste sur la même fonctionnalité, au tour suivant.
        """
        resultat = evaluer_votes(list(self.reveler().values()), self.regle, self.tour)
        if resultat.valide:
            self.fonctionnalite_courante.estimation = resultat.valeur
            self.index_courant += 1
            self.tour = 1
        else:
            self.tour += 1
        self.nouveau_tour()
        return resultat


def valider_nb_joueurs(nb: int) -> int:
    if not NB_JOUEURS_MIN <= nb <= NB_JOUEURS_MAX:
        raise SaisieInvalide(f"Le nombre de joueurs doit être entre {NB_JOUEURS_MIN} et {NB_JOUEURS_MAX}.")
    return nb


def creer_joueurs(pseudos: list[str]) -> list[Joueur]:
    """Refuse les pseudos vides et les doublons (insensible à la casse)."""
    joueurs, vus = [], set()
    for brut in pseudos:
        pseudo = brut.strip()
        if not pseudo:
            raise SaisieInvalide("Un pseudo ne peut pas être vide.")
        if pseudo.lower() in vus:
            raise SaisieInvalide(f"Pseudo déjà pris : {pseudo}")
        vus.add(pseudo.lower())
        joueurs.append(Joueur(pseudo))
    valider_nb_joueurs(len(joueurs))
    return joueurs
