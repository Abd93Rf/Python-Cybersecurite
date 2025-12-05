# Python & Cybersécurité — Projet d’Étude

Ce dépôt regroupe l’ensemble des outils réalisés dans le cadre d’un projet dédié à la découverte pratique de la cybersécurité à travers Python.
Chaque script illustre un concept essentiel : analyse de sécurité, chiffrement, gestion de mots de passe, détection d’attaques, ingénierie sociale ou encore surveillance pédagogique.

L’objectif général : **apprendre en construisant**, comprendre comment fonctionnent divers mécanismes de sécurité et développer une approche responsable de ces techniques.

## Objectifs du projet

* Approfondir les concepts fondamentaux de la cybersécurité via des implémentations concrètes.
* Explorer différentes pratiques : analyse de robustesse, chiffrement, gestion sécurisée, détection d’attaques, sensibilisation.
* Manipuler Python pour créer des outils pédagogiques représentatifs.
* Développer une conscience éthique dans l’utilisation d’outils offensifs et défensifs.

## Contenu du dépôt

Ce dépôt contient plusieurs modules distincts, chacun pouvant être accompagné de son README dédié.

### 1. Analyseur de mots de passe

Outil permettant :

* d’évaluer automatiquement le niveau de robustesse d’un mot de passe,
* d’identifier s’il fait partie d’une liste de mots de passe compromis,
* d’analyser plusieurs comptes via un gestionnaire interne,
* de générer un mot de passe sécurisé.

Une première approche essentielle sur la qualité des mots de passe et leurs vulnérabilités.

### 2. Chiffrement & Déchiffrement

Implémentation simple et interactive de deux chiffrements classiques :

* **Chiffrement de César**
* **Chiffrement de Vigenère**

Objectif : comprendre le fonctionnement du chiffrement symétrique et ses limites.

### 3. Gestionnaire de mots de passe (Fernet + SQLite)

Un gestionnaire complet comprenant :

* chiffrement/déchiffrement via `Fernet`,
* base de données `SQLite` pour stocker les identifiants chiffrés,
* générateur de mots de passe robustes,
* recherche et copie automatique dans le presse-papier.

Une mise en pratique concrète de la gestion sécurisée de secrets.

### 4. Générateur de mots de passe

Outil permettant de créer des mots de passe :

* aléatoires,
* personnalisés (majuscules, minuscules, chiffres, caractères spéciaux),
* de longueur variable.

Utile pour la création rapide de mots de passe forts.

### 5. Keylogger pédagogique

Un keylogger utilisant `pynput` pour montrer :

* comment les frappes clavier peuvent être interceptées,
* les risques liés à ces outils,
* l’importance de la vigilance et de la protection du poste utilisateur.

(Usage strictement éducatif, évidemment.)

### 6. Protection par brute force

Simulateur simple permettant d’illustrer :

* la limitation de tentatives,
* la détection d’activité suspecte,
* les mécanismes anti-brute-force.

### 7. Simulateur de phishing

Application Tkinter composée de :

* faux e‑mail de phishing,
* fausse page de connexion,
* conseils de prévention.

Outil pédagogique idéal pour comprendre l'ingénierie sociale.

### 8. Vérification de mots de passe compromis

Outil utilisant l’API **Have I Been Pwned** permettant :

* la vérification via hachage SHA‑1 (k‑anonymity),
* la détection de mots de passe présents dans des fuites connues,
* l’envoi de notification locale en cas de compromission.

## Avertissement éthique

Tous les outils présents dans ce projet sont conçus **exclusivement à des fins pédagogiques**, dans un environnement contrôlé.
Toute utilisation hors cadre légal ou sans autorisation est strictement interdite.
L’éthique est votre meilleure protection : comprenez pour mieux sécuriser, jamais pour nuire.
