"""Chargement du backlog JSON (US-02). Aucune entrée/sortie console ici."""
import json
from dataclasses import dataclass, field
from pathlib import Path


class BacklogInvalide(Exception):
    """Le fichier n'existe pas ou ne respecte pas le format attendu."""


@dataclass
class Fonctionnalite:
    id: str
    titre: str
    estimation: str | None = None  # remplie plus tard (séance 2)


@dataclass
class Backlog:
    projet: str
    fonctionnalites: list[Fonctionnalite] = field(default_factory=list)

    def premiere(self) -> Fonctionnalite:
        if not self.fonctionnalites:
            raise BacklogInvalide("Le backlog ne contient aucune fonctionnalité.")
        return self.fonctionnalites[0]


def charger_backlog(chemin: str | Path) -> Backlog:
    """Lit un fichier JSON {"projet": ..., "fonctionnalites": [{"id", "titre"}, ...]}."""
    chemin = Path(chemin)
    try:
        donnees = json.loads(chemin.read_text(encoding="utf-8"))
    except FileNotFoundError as e:
        raise BacklogInvalide(f"Fichier introuvable : {chemin}") from e
    except json.JSONDecodeError as e:
        raise BacklogInvalide(f"JSON invalide ({e.msg}, ligne {e.lineno})") from e

    if not isinstance(donnees, dict) or "fonctionnalites" not in donnees:
        raise BacklogInvalide('Clé "fonctionnalites" manquante.')
    if not isinstance(donnees["fonctionnalites"], list):
        raise BacklogInvalide('"fonctionnalites" doit être une liste.')

    fonctionnalites = []
    for i, f in enumerate(donnees["fonctionnalites"], start=1):
        if not isinstance(f, dict) or "id" not in f or "titre" not in f:
            raise BacklogInvalide(f'Fonctionnalité n°{i} : "id" et "titre" sont obligatoires.')
        fonctionnalites.append(Fonctionnalite(str(f["id"]), str(f["titre"]), f.get("estimation")))

    backlog = Backlog(str(donnees.get("projet", "Projet sans nom")), fonctionnalites)
    backlog.premiere()  # refuse un backlog vide
    return backlog
