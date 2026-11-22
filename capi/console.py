# Usage de l'IA : code écrit avec l'aide de l'IA (Claude), avec l'autorisation de l'enseignant. Voir AI_LOG.md.
"""Interface console. Elle appelle la logique de capi.partie / capi.backlog / capi.regles, sans en contenir."""
import getpass
import sys

from capi.backlog import BacklogInvalide, charger_backlog
from capi.partie import CARTES, Partie, SaisieInvalide, creer_joueurs, valider_nb_joueurs
from capi.regles import REGLES

CHEMIN_PAR_DEFAUT = "exemples/backlog-bibliotheque.json"


def demander_nb_joueurs() -> int:
    while True:
        try:
            return valider_nb_joueurs(int(input("Nombre de joueurs (2 à 10) : ")))
        except ValueError:
            print("  -> Entrez un nombre entier.")
        except SaisieInvalide as e:
            print(f"  -> {e}")


def demander_joueurs():
    nb = demander_nb_joueurs()
    while True:
        pseudos = [input(f"Pseudo du joueur {i} : ") for i in range(1, nb + 1)]
        try:
            return creer_joueurs(pseudos)
        except SaisieInvalide as e:
            print(f"  -> {e} Recommençons la saisie des pseudos.")


def demander_regle() -> str:
    choix = " / ".join(REGLES)
    while True:
        regle = input(f"Règle de validation à partir du 2e tour ({choix}) : ").strip().lower()
        if regle in REGLES:
            return regle
        print(f"  -> Règle inconnue. Choisissez parmi : {choix}.")


def demander_backlog(chemin_argument: str | None):
    chemin = chemin_argument
    while True:
        if chemin is None:
            chemin = input(f"Fichier backlog JSON [{CHEMIN_PAR_DEFAUT}] : ").strip() or CHEMIN_PAR_DEFAUT
        try:
            return charger_backlog(chemin)
        except BacklogInvalide as e:
            print(f"  -> {e}")
            chemin = None


def tour_de_vote(partie: Partie) -> None:
    print(f"\nCartes : {' '.join(CARTES)}")
    print("Chaque joueur tape sa carte en secret, puis passe le clavier au suivant.")
    for joueur in partie.joueurs:
        while True:
            # getpass masque la saisie : les autres joueurs ne voient pas la carte
            carte = getpass.getpass(f"{joueur.pseudo}, votre carte (saisie masquée) : ").strip()
            try:
                partie.voter(joueur.pseudo, carte)
                break
            except SaisieInvalide as e:
                print(f"  -> {e}")
    print("\nTous les joueurs ont voté. Révélation :")
    for pseudo, carte in partie.reveler().items():
        print(f"  {pseudo:<15} {carte}")


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    print("=== CAPI : planning poker ===\n")
    joueurs = demander_joueurs()
    regle = demander_regle()
    backlog = demander_backlog(argv[0] if argv else None)
    partie = Partie(joueurs, backlog, regle)

    print(f"\nProjet : {backlog.projet} ({len(backlog.fonctionnalites)} fonctionnalités)")
    print(f"Joueurs : {', '.join(j.pseudo for j in joueurs)} ; règle : {regle}")

    while not partie.est_terminee():
        f = partie.fonctionnalite_courante
        print(f"\n--- [{f.id}] {f.titre} : tour {partie.tour} ---")
        if partie.tour == 1:
            print("(Premier tour : il faut l'unanimité.)")
        tour_de_vote(partie)
        resultat = partie.cloturer_tour()
        if resultat.valide:
            print(f"\n=> Validé : {f.id} estimée à {resultat.valeur}.")
        else:
            print("\n=> Pas d'accord : les joueurs aux votes extrêmes s'expliquent, puis on revote.")

    print("\n=== Toutes les fonctionnalités sont estimées ===")
    for f in backlog.fonctionnalites:
        print(f"  [{f.id}] {f.titre} : {f.estimation}")
    print("\n(L'export JSON et la carte café arrivent dans un prochain sprint.)")
    return 0
