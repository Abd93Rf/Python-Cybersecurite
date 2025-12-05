import string
import random

# --- Classe Utilisateur ---
class Utilisateur:
    """
    Classe représentant un utilisateur avec un nom et un mot de passe.
    """
    def __init__(self, nom, mot_de_passe):
        self.nom = nom
        self.mot_de_passe = mot_de_passe


# --- Classe Analyseur ---
class Analyseur:
    """
    Classe contenant des méthodes pour analyser la robustesse d'un mot de passe
    et vérifier s'il est compromis.
    """
    @staticmethod
    def evaluer_robustesse(mot_de_passe):
        """
        Évalue la robustesse d'un mot de passe en fonction de plusieurs critères.
        Retourne un tuple (niveau, score).
        """
        score = 0

        # Longueur du mot de passe
        if len(mot_de_passe) >= 12:
            score += 2
        elif len(mot_de_passe) >= 8:
            score += 1

        # Contient des chiffres
        if any(char.isdigit() for char in mot_de_passe):
            score += 1

        # Contient des caractères spéciaux
        if any(char in string.punctuation for char in mot_de_passe):
            score += 1

        # Contient des majuscules et des minuscules
        if any(char.isupper() for char in mot_de_passe) and any(char.islower() for char in mot_de_passe):
            score += 1

        # Retourne le niveau basé sur le score
        if score < 3:
            return "Faible", score
        elif score < 5:
            return "Moyen", score
        else:
            return "Fort", score

    @staticmethod
    def est_compromis(mot_de_passe, liste_compromis):
        """
        Vérifie si le mot de passe est dans une liste de mots de passe compromis.
        """
        return mot_de_passe in liste_compromis


# --- Classe GestionnaireMotDePasse ---
class GestionnaireMotDePasse:
    """
    Classe pour gérer une liste d'utilisateurs et analyser leurs mots de passe.
    """
    def __init__(self):
        self.utilisateurs = []  # Liste des utilisateurs
        self.liste_compromis = set()  # Ensemble des mots de passe compromis

    def ajouter_utilisateur(self, nom, mot_de_passe):
        """
        Ajoute un utilisateur à la liste.
        """
        utilisateur = Utilisateur(nom, mot_de_passe)
        self.utilisateurs.append(utilisateur)

    def analyser_tous(self):
        """
        Analyse les mots de passe de tous les utilisateurs et affiche les résultats.
        """
        for utilisateur in self.utilisateurs:
            niveau, score = Analyseur.evaluer_robustesse(utilisateur.mot_de_passe)
            compromis = Analyseur.est_compromis(utilisateur.mot_de_passe, self.liste_compromis)
            print(f"Utilisateur: {utilisateur.nom}")
            print(f"Mot de passe: {utilisateur.mot_de_passe}")
            print(f"Niveau de sécurité: {niveau} (Score: {score})")
            if compromis:
                print("⚠️ Ce mot de passe est compromis!")
            print("-" * 30)

    @staticmethod
    def generer_mot_de_passe(longueur=12):
        """
        Génère un mot de passe sécurisé avec une longueur spécifiée.
        """
        caracteres = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(caracteres) for _ in range(longueur))


# --- Programme principal ---
def main():
    gestionnaire = GestionnaireMotDePasse()

    # Ajouter des utilisateurs via le terminal
    print("Ajout des utilisateurs :")
    while True:
        nom = input("Entrez le nom de l'utilisateur (ou 'q' pour quitter) : ")
        if nom.lower() == 'q':
            break
        mot_de_passe = input(f"Entrez le mot de passe pour {nom} : ")
        gestionnaire.ajouter_utilisateur(nom, mot_de_passe)

    # Analyser les mots de passe des utilisateurs
    print("\nAnalyse des mots de passe des utilisateurs :")
    gestionnaire.analyser_tous()

    # Générer un mot de passe sécurisé
    print("\nGénération d'un mot de passe sécurisé :")
    mot_de_passe_genere = GestionnaireMotDePasse.generer_mot_de_passe()
    print(f"Mot de passe généré : {mot_de_passe_genere}")


# --- Lancer le programme principal ---
if __name__ == "__main__":
    main()