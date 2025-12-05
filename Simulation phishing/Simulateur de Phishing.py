import tkinter as tk
from tkinter import messagebox

# Fonction pour simuler l'envoi d'un faux e-mail de phishing
def simulate_phishing_email():
    email_content = """Cher utilisateur,

Nous avons détecté une activité inhabituelle sur votre compte. Veuillez vous connecter immédiatement pour vérifier vos informations.

[FAUSSE LIEN DE CONNEXION]

Cordialement,
Équipe de Sécurité"""
    
    messagebox.showinfo("Simulation d'e-mail de phishing", email_content)

# Fonction pour afficher les conseils de prévention
def show_prevention_tips():
    tips = """
    Conseils pour éviter le phishing :
    
    1. Vérifiez toujours l'adresse de l'expéditeur. Méfiez-vous des adresses suspectes.
    2. Ne cliquez pas sur des liens provenant de sources non fiables.
    3. Regardez les fautes d'orthographe dans le message, elles sont souvent révélatrices.
    4. Activez l'authentification à deux facteurs sur vos comptes importants.
    5. Utilisez des solutions anti-phishing et tenez à jour vos logiciels de sécurité.
    """
    messagebox.showinfo("Conseils de prévention", tips)

# Fonction pour simuler une fausse page de connexion
def simulate_fake_login_page():
    fake_page = """--- FAUSSE PAGE DE CONNEXION ---
    
    Entrez votre nom d'utilisateur et mot de passe :
    
    [Nom d'utilisateur] : _____________
    [Mot de passe]      : _____________
    
    -----------------------------------
    
    Attention ! Vous avez soumis vos informations à une fausse page !
    """
    messagebox.showinfo("Simulation de page de connexion de phishing", fake_page)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Simulateur de Phishing - Sensibilisation à la Cybersécurité")
root.geometry("400x300")

# Titre
title_label = tk.Label(root, text="Simulateur de Phishing", font=("Helvetica", 16))
title_label.pack(pady=10)

# Description
desc_label = tk.Label(root, text="Sélectionnez une simulation pour apprendre les techniques de phishing :")
desc_label.pack(pady=5)

# Bouton pour simuler un e-mail de phishing
email_button = tk.Button(root, text="Simuler un faux e-mail", command=simulate_phishing_email)
email_button.pack(pady=10)

# Bouton pour simuler une fausse page de connexion
login_button = tk.Button(root, text="Simuler une fausse page de connexion", command=simulate_fake_login_page)
login_button.pack(pady=10)

# Bouton pour afficher des conseils de prévention
prevention_button = tk.Button(root, text="Conseils de prévention", command=show_prevention_tips)
prevention_button.pack(pady=10)

# Exécuter la fenêtre Tkinter
root.mainloop()
