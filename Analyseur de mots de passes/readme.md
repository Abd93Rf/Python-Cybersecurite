# Analyseur de Mots de Passe

Cet outil a été conçu dans le cadre d’un projet visant à comprendre les critères fondamentaux d’un mot de passe robuste, à analyser des mots de passe utilisateurs et à illustrer comment détecter ceux considérés comme compromis.
Il s’agit d’un module pédagogique permettant de manipuler des critères de robustesse, de gérer des utilisateurs et de générer des mots de passe sécurisés.

## Objectif du script

L’analyseur permet de :

* Évaluer automatiquement le niveau de sécurité d’un mot de passe.
* Vérifier si un mot de passe fait partie d’une liste compromise.
* Gérer une liste d’utilisateurs et analyser leurs mots de passe.
* Générer un mot de passe aléatoire et sécurisé.

L’ensemble est pensé pour offrir une vision claire des bases de la gestion et de l’évaluation de mots de passe en cybersécurité.

## Fonctionnalités principales

### **1. Classe `Utilisateur`**

Représente un utilisateur contenant :

* un nom d'utilisateur,
* un mot de passe associé.

Elle sert de structure de base pour les analyses.

### **2. Classe `Analyseur`**

Regroupe les méthodes liées à l’analyse pure d’un mot de passe.

#### • `evaluer_robustesse(mot_de_passe)`

Évalue la force du mot de passe selon plusieurs critères :

* longueur,
* présence de chiffres,
* caractères spéciaux,
* mélange de majuscules/minuscules.

Retour :
→ un niveau (**Faible**, **Moyen**, **Fort**)
→ un score associé.

#### • `est_compromis(mot_de_passe, liste_compromis)`

Vérifie si le mot de passe figure dans une liste de mots de passe compromis fournie par l’utilisateur.

### **3. Classe `GestionnaireMotDePasse`**

Gère les utilisateurs et centralise les analyses.

Fonctionnalités :

* **ajout d’utilisateurs,**
* **analyse en série de tous les mots de passe**, avec affichage détaillé,
* stockage d’une liste de mots de passe compromis,
* génération d’un mot de passe sécurisé via `generer_mot_de_passe(longueur)`.

### **4. Programme principal (`main`)**

Le script permet :

1. d’ajouter des utilisateurs via le terminal,
2. d’analyser leurs mots de passe,
3. de générer un mot de passe fort automatiquement.

Ce comportement interactif facilite les tests et la compréhension du fonctionnement de l’analyse.

## Exemple d’utilisation

Le programme propose alors :

* d’ajouter des utilisateurs,
* d’obtenir un diagnostic immédiat de leur mot de passe,
* de générer un mot de passe sécurisé.

## AVERTISSEMENT ETHIQUE

Cet outil est conçu **strictement à des fins éducatives** dans un environnement contrôlé.
Il ne doit en aucun cas être utilisé pour analyser ou récupérer les mots de passe de tiers sans autorisation explicite.


