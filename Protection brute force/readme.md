# Tentative de Brute Force 

Ce script illustre une version simplifiée d’un mécanisme de défense contre les attaques par force brute.
Il simule un système d’authentification avec gestion du nombre de tentatives autorisées.
L’objectif est d’aborder de manière pédagogique la logique derrière la prévention des attaques automatisées.

## Objectif du script

* Demander à l’utilisateur un mot de passe et comparer avec une valeur de référence.
* Comptabiliser le nombre d'échecs successifs.
* Bloquer l'accès après un certain nombre de tentatives.
* Afficher un message d’alerte lorsqu’un comportement évoquant une attaque brute force est détecté.

## Fonctionnement du script

### 1. Mot de passe de référence

Le script contient un mot de passe défini dans le code :

```python
mot_de_passe_correct = "monMotDePasse123"
```

Cela permet de simuler un système vérifiant une authentification.

### 2. Système de comptage des tentatives

Un compteur `tentatives_echouees` s’incrémente à chaque mot de passe incorrect.

### 3. Limite de tentatives

Une limite est définie :

```python
limite_tentatives = 5
```

Si elle est atteinte, le système considère qu’une potentielle attaque par force brute est en cours et coupe l’accès.

### 4. Logique d’authentification

* L’utilisateur saisit un mot de passe.
* Si c’est le bon → accès autorisé.
* Sinon → tentative enregistrée et affichée.
* Après 5 échecs → blocage final + message d’alerte.

Ce mécanisme reproduit les protections habituelles d’un système d’authentification rudimentaire.

## Intérêt en cybersécurité

Ce script sensibilise à :

* la vulnérabilité aux attaques par essais multiples ;
* l’importance des limitations d’accès ;
* les mécanismes de verrouillage d’un compte ;
* la nécessité d’implémenter un suivi des tentatives et une réponse défensive.

C’est un exemple clair et concis pour comprendre les bases de la défense contre le brute force.