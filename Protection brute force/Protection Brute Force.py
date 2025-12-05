# Mot de passe correct
mot_de_passe_correct = "monMotDePasse123"
# Compteur de tentatives
tentatives_echouees = 0
# Limite de tentatives
limite_tentatives = 5

while tentatives_echouees < limite_tentatives:
    mot_de_passe = input("Entrez le mot de passe : ")

    if mot_de_passe == mot_de_passe_correct:
        print("Accès autorisé.")
        break
    else:
        tentatives_echouees += 1 
        print(f"Mauvais mot de passe. Tentatives echouées : {tentatives_echouees}/{limite_tentatives}")

if tentatives_echouees >= limite_tentatives:
    print("Nombre maximum de tentatives atteint. Possible attaque par force brute détectée.")