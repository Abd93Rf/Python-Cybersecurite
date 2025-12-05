# Gestionnaire de Mots de Passe 

Ce script implémente un gestionnaire de mots de passe complet : stockage sécurisé, chiffrement, génération de mots de passe et interface interactive en ligne de commande.
Il illustre des concepts essentiels : chiffrement symétrique, base de données locale, gestion sécurisée de clés et automatisation de la protection des identifiants.

## Objectif du script

* Stocker des mots de passe dans une base SQLite **chiffrés** à l’aide de `Fernet` (cryptographie symétrique).
* Générer une clé de chiffrement et la gérer automatiquement.
* Ajouter, rechercher et décrypter des mots de passe via un menu interactif.
* Fournir un générateur de mots de passe robustes en utilisant `secrets`.
* Permettre la copie immédiate dans le presse-papier.

## Fonctionnalités principales

### 1. Gestion de la clé de chiffrement (`Fernet`)

Le système repose sur une clé unique stockée dans un fichier local `secret.key`.

#### • `generate_key()`

Génère une clé Fernet et la sauvegarde dans un fichier.

#### • `load_key()`

Charge la clé existante ou en génère une nouvelle si elle n’existe pas.

Cela garantit que tous les mots de passe stockés restent cohérents et chiffrés avec la même clé.

### 2. Chiffrement / Déchiffrement des mots de passe

#### • `encrypt_password(password, key)`

Chiffre un mot de passe en UTF-8 et renvoie une version encryptée prête à stocker.

#### • `decrypt_password(encrypted_password, key)`

Déchiffre le mot de passe pour l'affichage ou l’utilisation.

Ces deux fonctions garantissent que les données sensibles ne sont jamais stockées en clair dans la base.

### 3. Base de données SQLite

#### • Table `passwords`

| id | service | username | password (chiffré) |
| -- | ------- | -------- | ------------------ |

Fonctions associées :

* `init_db()` : crée la base si nécessaire.
* `store_password(service, username, password, key)` : enregistre un identifiant chiffré.
* `get_password(service, key)` : récupère et déchiffre les données d’un service donné.

### 4. Générateur de mots de passe

#### • `generate_password(length=16)`

Utilise `secrets.choice()` pour produire un mot de passe cryptographiquement robuste composé de :

* lettres majuscules,
* lettres minuscules,
* chiffres,
* caractères spéciaux.

### 5. Interface utilisateur (menu interactif)

Le menu permet :

1. **Ajouter un mot de passe**

   * Saisir manuellement ou générer automatiquement.
   * Chiffrement automatique avant stockage.

2. **Rechercher un mot de passe**

   * Déchiffrement et affichage sécurisés.
   * Option pour copier dans le presse-papier.

3. **Générer un mot de passe sécurisé**

   * Personnalisation de la longueur.
   * Option de copie instantanée.

4. **Quitter**

## Exemple d'utilisation

### Ajouter un mot de passe :

```
1. Ajouter un nouveau mot de passe
Nom du service: Gmail
Nom d'utilisateur: user@gmail.com
Mot de passe (laisser vide pour générer un mot de passe sécurisé):
Mot de passe généré : 8$Jsd!kP*Z1eL%
Mot de passe pour Gmail enregistré avec succès !
```

### Rechercher un mot de passe :

```
2. Rechercher un mot de passe
Nom du service à rechercher: Gmail
Nom d'utilisateur: user@gmail.com
Mot de passe: 8$Jsd!kP*Z1eL%
```

## Avertissement éthique & sécurité

Ce gestionnaire est pédagogique :

* Il ne doit pas être utilisé en production ou pour des données sensibles réelles.
* La clé locale n’est pas protégée par mot de passe.
* Pour un usage professionnel, utiliser des solutions éprouvées (Bitwarden, KeePass, etc.).