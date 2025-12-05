import hashlib
import requests
from plyer import notification

# Fonction pour vérifier si un mot de passe a été compromis
def check_password_breach(password):
    # Hachage du mot de passe avec SHA-1
    sha1_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_pass[:5], sha1_pass[5:]

    # Requête à l'API de Have I Been Pwned
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"Erreur dans la requête à l'API : {response.status_code}")

    # Vérifier si le suffixe du hachage est dans la liste des hachages compromis
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)  # Retourne le nombre de fois où le mot de passe a été compromis

    return 0  # Mot de passe non trouvé dans les fuites

# Fonction pour notifier l'utilisateur
def notify_user(message):
    notification.notify(
        title="Violation de Mot de Passe",
        message=message,
        app_name="Password Monitor",
        timeout=10
    )

# Fonction principale pour entrer le mot de passe et vérifier
def monitor_passwords():
    while True:
        password = input("Entrez un mot de passe à vérifier (ou 'exit' pour quitter) : ")
        if password.lower() == 'exit':
            break

        count = check_password_breach(password)
        if count > 0:
            notify_user(f"Le mot de passe a été compromis {count} fois !")
            print(f"Alerte : Le mot de passe a été trouvé {count} fois dans les violations de données.")
        else:
            print("Le mot de passe n'a pas été trouvé dans les fuites de données.")

if __name__ == "__main__":
    monitor_passwords()
