import sqlite3
import os
import base64
import secrets
import string
import pyperclip
from cryptography.fernet import Fernet
from getpass import getpass

# === Génération de la clé de chiffrement et initialisation ===
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("secret.key"):
        generate_key()
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# === Chiffrement et déchiffrement ===
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# === Base de données pour stocker les mots de passe ===
def init_db():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def store_password(service, username, password, key):
    encrypted_password = encrypt_password(password, key)
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
                   (service, username, encrypted_password))
    conn.commit()
    conn.close()

def get_password(service, key):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM passwords WHERE service=?", (service,))
    result = cursor.fetchone()
    conn.close()
    if result:
        username, encrypted_password = result
        decrypted_password = decrypt_password(encrypted_password, key)
        return username, decrypted_password
    else:
        return None

# === Génération de mots de passe sécurisés ===
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for i in range(length))

# === Interface utilisateur ===
def main():
    key = load_key()
    init_db()

    while True:
        print("\n=== Gestionnaire de mots de passe ===")
        print("1. Ajouter un nouveau mot de passe")
        print("2. Rechercher un mot de passe")
        print("3. Générer un mot de passe sécurisé")
        print("4. Quitter")
        choice = input("Choisissez une option: ")

        if choice == "1":
            service = input("Nom du service: ")
            username = input("Nom d'utilisateur: ")
            password = getpass("Mot de passe (laisser vide pour générer un mot de passe sécurisé): ")
            if not password:
                password = generate_password()
                print(f"Mot de passe généré : {password}")
            store_password(service, username, password, key)
            print(f"Mot de passe pour {service} enregistré avec succès !")

        elif choice == "2":
            service = input("Nom du service à rechercher: ")
            result = get_password(service, key)
            if result:
                username, password = result
                print(f"Nom d'utilisateur: {username}")
                print(f"Mot de passe: {password}")
                copy_choice = input("Voulez-vous copier le mot de passe dans le presse-papier ? (y/n): ")
                if copy_choice.lower() == 'y':
                    pyperclip.copy(password)
                    print("Mot de passe copié dans le presse-papier.")
            else:
                print(f"Aucun mot de passe trouvé pour {service}.")

        elif choice == "3":
            length = int(input("Longueur du mot de passe : "))
            generated_password = generate_password(length)
            print(f"Mot de passe généré : {generated_password}")
            copy_choice = input("Voulez-vous copier le mot de passe dans le presse-papier ? (y/n): ")
            if copy_choice.lower() == 'y':
                pyperclip.copy(generated_password)
                print("Mot de passe copié dans le presse-papier.")

        elif choice == "4":
            print("Au revoir!")
            break

        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
