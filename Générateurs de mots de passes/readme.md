# Générateur de Mots de Passe

Ce script propose un générateur de mots de passe personnalisable, permettant de créer facilement des mots de passe robustes selon les critères choisis par l’utilisateur.
L’objectif est de comprendre les bonnes pratiques liées à la création de mots de passe et d’expérimenter la génération aléatoire sécurisée.

## Objectif du script

* Générer des mots de passe aléatoires et robustes.
* Permettre à l’utilisateur de définir les types de caractères à inclure.
* Illustrer les notions d’entropie et de diversité des caractères.
* Offrir un outil simple, interactif et modulable.

## Fonctionnalités principales

### **1. Fonction `generer_mot_de_passe`**

Génère un mot de passe en fonction des paramètres choisis :

* **longueur** du mot de passe,
* inclusion ou non :

  * des majuscules,
  * des minuscules,
  * des chiffres,
  * des caractères spéciaux.

Le mot de passe est construit en sélectionnant aléatoirement des caractères parmi les catégories activées.

Si aucune catégorie n’est sélectionnée, une erreur explicite est renvoyée.

### 2. Fonction `demande_informations`

Interface interactive permettant :

* de saisir la longueur du mot de passe,
* de choisir les types de caractères à inclure (via questions *y/n*),
* d’obtenir immédiatement un mot de passe généré.

Inclut une gestion des erreurs :

* longueur négative ou invalide,
* absence totale de catégories sélectionnées.

## Exemple d’utilisation

**Entrées :**

* Longueur : 14
* Inclure majuscules : oui
* Inclure minuscules : oui
* Inclure chiffres : oui
* Inclure caractères spéciaux : non

**Sortie :**

```
Mot de passe généré : Ab9fKD72hjPLqw
```

## ️ Bonnes pratiques

Ce générateur illustre l’importance :

* de varier les catégories de caractères,
* d’utiliser une longueur suffisante,
* d’éviter les schémas prévisibles.