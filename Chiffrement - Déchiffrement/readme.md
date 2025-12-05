# Chiffrement & Déchiffrement — Méthodes de César et Vigenère

Ce script propose une mise en pratique simple mais essentielle de deux méthodes historiques de cryptographie symétrique : le chiffrement de **César** et celui de **Vigenère**.
L’objectif est de comprendre le fonctionnement de ces algorithmes, leurs limites, et la logique du décalage alphabétique.

Le script inclut un menu interactif permettant de chiffrer ou déchiffrer un message selon la méthode choisie.

## Objectif du script

* Illustrer le fonctionnement de deux algorithmes cryptographiques fondamentaux.
* Manipuler les concepts de **décalage**, **clé**, **casse**, et **caractères non alphabétiques**.
* Proposer une pratique concrète du chiffrement symétrique historique.

## Fonctionnalités principales

### **1. Chiffrement de César**

Le chiffrement de César consiste à décaler chaque lettre du message d’un certain nombre de positions dans l’alphabet.

#### • `chiffrement_cesar(message, cle)`

* Déplace chaque lettre selon un décalage fixe (`cle`).
* Respecte la casse (majuscule / minuscule).
* Conserve les caractères non alphabétiques.

#### • `dechiffrement_cesar(message, cle)`

* Déchiffre en appliquant l’inverse du décalage (clé négative).

### **2. Chiffrement de Vigenère**

Méthode plus complexe où chaque lettre est décalée en fonction d’une **clé textuelle**.
Chaque caractère de la clé définit un décalage différent.

#### • `chiffrement_vigenere(message, cle)`

* Utilise une clé alphabétique répétée sur tout le message.
* Applique un décalage dépendant de chaque lettre de la clé.
* Respecte la casse.

#### • `dechiffrement_vigenere(message, cle)`

* Inverse le décalage pour chaque caractère de la clé.

## Menu interactif

La fonction `menu()` permet :

1. De choisir la méthode (César ou Vigenère).
2. D’entrer un message.
3. De fournir une clé (nombre pour César, mot pour Vigenère).
4. De choisir entre chiffrement ou déchiffrement.

## Exemple rapide

### César

* Message : `Bonjour`
Clé : `3`
→ Résultat : `Erqmrxu`

### Vigenère

* Message : `HELLO`
Clé : `key`
→ Résultat : `RIJVS`

## Remarque pédagogique

Ces méthodes sont aujourd’hui considérées comme **non sécurisées** et ne doivent pas être utilisées dans un contexte réel de protection de données.
Elles servent ici uniquement à illustrer les mécanismes fondamentaux de la cryptographie.
