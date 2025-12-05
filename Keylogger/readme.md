# Keylogger

Ce script implémente un keylogger minimaliste utilisant la bibliothèque `pynput`.
Dans le cadre d’un projet pédagogique, il permet de comprendre comment fonctionnent la capture d’événements clavier, la gestion d’écouteurs système et les fondamentaux de la surveillance d’entrée utilisateur — **exclusivement dans un contexte légal et autorisé**.

---

## Objectif du script

* Apprendre à utiliser `pynput` pour écouter les touches pressées.
* Comprendre le fonctionnement d’un *listener* clavier.
* Enregistrer les frappes dans un fichier local pour analyse.
* Illustrer les risques et dérives possibles afin de sensibiliser aux bonnes pratiques en cybersécurité.

Ce script **n’a pas vocation à être utilisé à des fins malveillantes**. Il sert uniquement pour l’apprentissage et la démonstration contrôlée sur une machine personnelle ou un environnement de test.

## Fonctionnement

### 1. Capture des touches

La méthode `on_press()` est appelée à chaque pression d’une touche.
Elle récupère :

* le caractère réel si c’est une touche imprimable,
* sinon une représentation textuelle (ex. : `Key.space`, `Key.enter`).

Le résultat est immédiatement écrit dans un fichier texte.

### 2. Enregistrement dans un fichier

Chaque frappe est ajoutée au fichier configuré dans `filename` (par défaut : `keylogs.txt`).

```python
with open(self.filename, 'a') as logs:
    logs.write(self.get_char(key))
```

### 3. Lancement du listener

La méthode `main()` démarre un écouteur asynchrone :

```python
listener = keyboard.Listener(on_press=self.on_press)
listener.start()
```

Le script reste actif jusqu’à ce que l’utilisateur appuie sur Entrée.

## Structure du code

* `__init__()` : définit le fichier où enregistrer les frappes.
* `get_char(key)` : transforme les événements clavier (`pynput.keyboard.Key`) en texte.
* `on_press(key)` : enregistre chaque touche pressée.
* `main()` : crée et démarre l’écouteur clavier.
* Exécution en tant que script → instancie le keylogger et lance l’écoute.

---

## Lancer le script

Assure-toi d’avoir installé `pynput` :

```bash
pip install pynput
```

Puis exécute :

```bash
python keylogger.py
```

Le keylogger commencera à enregistrer les frappes dans `keylogs.txt`.

## Avertissement légal & éthique

Ce programme est un outil **strictement pédagogique**.
L’utilisation d’un keylogger sans consentement explicite est **illégale** et pénalement répréhensible.

Utilise ce script uniquement :

* sur ta propre machine,
* dans un environnement de test