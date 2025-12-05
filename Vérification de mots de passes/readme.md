# Vérificateur de Mots de Passe Compromis — Vérification via API (HIBP)

Ce script permet de vérifier si un mot de passe a déjà été exposé dans une fuite de données connue.
Il repose sur le service public **Have I Been Pwned** et applique la méthode sécurisée dite **k-anonymity**, garantissant que le mot de passe n’est jamais envoyé tel quel sur Internet.

L’objectif : sensibiliser aux risques liés aux mots de passe trop utilisés ou compromis, et encourager de meilleures bonnes pratiques.

## Objectif du script

* Vérifier si un mot de passe apparaît dans une fuite de données publique.
* Utiliser un hachage partiel (SHA-1) afin de préserver la confidentialité.
* Alerter l’utilisateur via une notification locale en cas de mot de passe compromis.
* Proposer une interface simple en ligne de commande.

## Fonctionnement général

### 1. Hachage du mot de passe (SHA-1)

Le mot de passe entré est immédiatement haché côté client :

* seuls les **5 premiers caractères** du hachage sont envoyés à l’API,
* le reste est comparé localement parmi la liste retournée.

Ce mécanisme protège l’utilisateur :
le service ne reçoit jamais le mot de passe complet, ni son hachage intégral.

### 2. Requête API “range”

Le script interroge l’endpoint :

```
https://api.pwnedpasswords.com/range/<prefix>
```

L’API renvoie **tous les suffixes possibles** correspondant au préfixe fourni.
Le script compare ensuite le suffixe local avec ceux retournés pour déterminer si :

* le mot de passe a été compromis,
* et *combien de fois* il apparaît dans des fuites.

### 3. Notification de sécurité

En cas de mot de passe compromis, une notification système est envoyée :

* message d’alerte,
* nom de l’application : *Password Monitor*,
* durée d’affichage configurable.

Une alerte est également affichée dans la console.

### 4. Boucle d’utilisation

L’utilisateur peut tester autant de mots de passe qu’il souhaite, jusqu’à taper `exit`.

## Dépendances

* `hashlib` (standard Python)
* `requests`
* `plyer` (pour notifications locales)

Installation des modules externes :

```bash
pip install requests plyer
```

## Intérêt pédagogique

Ce script permet de comprendre :

* comment fonctionnent les fuites de données,
* comment vérifier un mot de passe sans jamais le divulguer,
* pourquoi réutiliser un même mot de passe est dangereux,
* comment sensibiliser aux bonnes pratiques de sécurité.