# Usage de l'IA : tests écrits avec l'aide de l'IA (Claude), avec l'autorisation de l'enseignant. Voir AI_LOG.md.
"""Tests du moteur de règles : un test par ligne de la table de décision (rendus/R2.md)."""
import unittest

from capi.regles import Resultat, evaluer_votes


class TestReglesStrict(unittest.TestCase):

    def test_CA_06_2_strict_tour1_votes_identiques(self):
        # Préparer
        votes = ["5", "5", "5"]
        # Agir
        resultat = evaluer_votes(votes, "strict", 1)
        # Vérifier
        self.assertEqual(resultat, Resultat(valide=True, valeur="5"))

    def test_CA_06_3_strict_tour1_un_vote_different(self):
        # Préparer
        votes = ["5", "5", "8"]
        # Agir
        resultat = evaluer_votes(votes, "strict", 1)
        # Vérifier
        self.assertEqual(resultat, Resultat(valide=False))

    def test_CA_06_1_strict_tour2_majorite_ne_suffit_pas(self):
        # Pourquoi ce cas compte : en strict, même une large majorité au tour 2 ne valide pas.
        # Préparer
        votes = ["3", "3", "3", "5"]
        # Agir
        resultat = evaluer_votes(votes, "strict", 2)
        # Vérifier
        self.assertEqual(resultat, Resultat(valide=False))

    def test_CA_06_4_strict_tour2_votes_identiques(self):
        # Préparer
        votes = ["8", "8", "8"]
        # Agir
        resultat = evaluer_votes(votes, "strict", 2)
        # Vérifier
        self.assertEqual(resultat, Resultat(valide=True, valeur="8"))


class TestReglesPremierTour(unittest.TestCase):

    def test_CA_05_1_mediane_tour1_majorite_ne_suffit_pas(self):
        # Préparer
        votes = ["5", "8", "8"]
        # Agir
        resultat = evaluer_votes(votes, "mediane", 1)
        # Vérifier
        self.assertEqual(resultat, Resultat(valide=False))

    def test_CA_05_2_mediane_tour1_votes_identiques(self):
        # Préparer
        votes = ["3", "3", "3"]
        # Agir
        resultat = evaluer_votes(votes, "mediane", 1)
        # Vérifier
        self.assertEqual(resultat, Resultat(valide=True, valeur="3"))


class TestReglesMediane(unittest.TestCase):

    def test_CA_07_2_mediane_tour2_nombre_impair(self):
        # Préparer
        votes = ["3", "5", "8"]
        # Agir
        resultat = evaluer_votes(votes, "mediane", 2)
        # Vérifier
        self.assertEqual(resultat, Resultat(valide=True, valeur="5"))

    def test_CA_07_1_mediane_tour2_nombre_pair_arrondi_superieur(self):
        # Pourquoi ce cas compte : la moyenne des deux votes centraux (4) n'est pas une carte.
        # Préparer
        votes = ["2", "3", "5", "8"]
        # Agir
        resultat = evaluer_votes(votes, "mediane", 2)
        # Vérifier
        self.assertEqual(resultat, Resultat(valide=True, valeur="5"))

    def test_CA_07_3_mediane_tour2_carte_interrogation_revote(self):
        # Pourquoi ce cas compte : « ? » n'est pas un nombre, et un joueur qui ne sait pas doit être entendu.
        # Préparer
        votes = ["3", "5", "?"]
        # Agir
        resultat = evaluer_votes(votes, "mediane", 2)
        # Vérifier
        self.assertEqual(resultat, Resultat(valide=False))

    def test_CA_07_4_mediane_tour2_egalite(self):
        # Préparer
        votes = ["3", "3", "8", "8"]
        # Agir
        resultat = evaluer_votes(votes, "mediane", 2)
        # Vérifier
        self.assertEqual(resultat, Resultat(valide=True, valeur="8"))


if __name__ == "__main__":
    unittest.main()
