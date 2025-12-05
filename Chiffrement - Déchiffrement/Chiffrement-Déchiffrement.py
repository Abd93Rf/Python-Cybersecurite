def chiffrement_cesar(message, cle):
    resultat = ""
    # Parcours de chaque caractère dans le message
    for caractere in message:
        if caractere.isalpha():
            # Garde la casse (majuscule ou minuscule)
            code_base = ord('A') if caractere.isupper() else ord('a')
            # Décalage des lettres selon la clé
            resultat += chr((ord(caractere) - code_base + cle) % 26 + code_base)
        else:
            # Si ce n'est pas une lettre, on ne le modifie pas
            resultat += caractere
    return resultat

def dechiffrement_cesar(message, cle):
    # Pour déchiffrer, on utilise simplement la clé inverse
    return chiffrement_cesar(message, -cle)

def chiffrement_vigenere(message, cle):
    resultat = ""
    cle = cle.lower()
    index_cle = 0

    for caractere in message:
        if caractere.isalpha():
            code_base = ord('A') if caractere.isupper() else ord('a')
            decalage = ord(cle[index_cle % len(cle)]) - ord('a')
            resultat += chr((ord(caractere) - code_base + decalage) % 26 + code_base)
            index_cle += 1
        else:
            resultat += caractere
    return resultat

def dechiffrement_vigenere(message, cle):
    resultat = ""
    cle = cle.lower()
    index_cle = 0

    for caractere in message:
        if caractere.isalpha():
            code_base = ord('A') if caractere.isupper() else ord('a')
            decalage = ord(cle[index_cle % len(cle)]) - ord('a')
            resultat += chr((ord(caractere) - code_base - decalage) % 26 + code_base)
            index_cle += 1
        else:
            resultat += caractere
    return resultat

def menu():
    print("Choisissez une méthode de chiffrement :")
    print("1. Chiffrement de César")
    print("2. Chiffrement de Vigenère")
    choix = input("Entrez votre choix (1 ou 2) : ")

    if choix == "1":
        message = input("Entrez le message : ")
        cle = int(input("Entrez la clé (un nombre entier) : "))
        action = input("Voulez-vous (C)hiffrer ou (D)échiffrer le message ? ").upper()

        if action == 'C':
            print("Message chiffré :", chiffrement_cesar(message, cle))
        elif action == 'D':
            print("Message déchiffré :", dechiffrement_cesar(message, cle))
        else:
            print("Option non valide.")
    
    elif choix == "2":
        message = input("Entrez le message : ")
        cle = input("Entrez la clé (un mot) : ")
        action = input("Voulez-vous (C)hiffrer ou (D)échiffrer le message ? ").upper()

        if action == 'C':
            print("Message chiffré :", chiffrement_vigenere(message, cle))
        elif action == 'D':
            print("Message déchiffré :", dechiffrement_vigenere(message, cle))
        else:
            print("Option non valide.")
    
    else:
        print("Choix non valide.")

if __name__ == "__main__":
    menu()
