import random
import string

def generer_mot_de_passe(longueur, inclure_majuscules=True, inclure_minuscules=True, inclure_chiffres=True, inclure_speciaux=True):
    # Création de la liste de caractères possibles selon les options choisies
    caracteres = ""
    
    if inclure_majuscules:
        caracteres += string.ascii_uppercase  # Lettres majuscules (A-Z)
    if inclure_minuscules:
        caracteres += string.ascii_lowercase  # Lettres minuscules (a-z)
    if inclure_chiffres:
        caracteres += string.digits           # Chiffres (0-9)
    if inclure_speciaux:
        caracteres += string.punctuation      # Caractères spéciaux (!, @, #, etc.)
    
    if not caracteres:
        raise ValueError("Vous devez sélectionner au moins une option de caractères !")
    
    # Générer un mot de passe aléatoire
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

# Saisie utilisateur
def demande_informations():
    try:
        longueur = int(input("Entrez la longueur souhaitée du mot de passe : "))
        if longueur <= 0:
            raise ValueError("La longueur doit être un nombre positif.")
        
        # Demander les options pour les caractères à inclure
        inclure_majuscules = input("Inclure des majuscules (A-Z) ? (y/n) : ").lower() == 'y'
        inclure_minuscules = input("Inclure des minuscules (a-z) ? (y/n) : ").lower() == 'y'
        inclure_chiffres = input("Inclure des chiffres (0-9) ? (y/n) : ").lower() == 'y'
        inclure_speciaux = input("Inclure des caractères spéciaux (!, @, #, etc.) ? (y/n) : ").lower() == 'y'
        
        # Générer et afficher le mot de passe
        mot_de_passe = generer_mot_de_passe(longueur, inclure_majuscules, inclure_minuscules, inclure_chiffres, inclure_speciaux)
        print(f"Mot de passe généré : {mot_de_passe}")
    
    except ValueError as e:
        print(f"Erreur : {e}")

# Exécuter le programme
if __name__ == "__main__":
    demande_informations()
