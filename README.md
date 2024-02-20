# Calculatrice Tkinter

Une simple calculatrice réalisée en utilisant la bibliothèque Tkinter de Python.

## Fonctionnalités

- Les boutons numériques de 0 à 9 permettent de former des nombres dans la formule.
- Les boutons d'opération (+, -) permettent d'ajouter des opérations à la formule.
- Le bouton "effacer" permet de réinitialiser la formule.
- Le bouton "=" permet de calculer le résultat de la formule.

## Comment utiliser

1. Exécutez le script.
2. Utilisez les boutons numériques pour créer la formule souhaitée.
3. Utilisez les boutons d'opération pour ajouter des opérations à la formule.
4. Cliquez sur le bouton "=" pour obtenir le résultat.
5. Le bouton "effacer" réinitialise la formule.

## Exemple d'utilisation du code

```python
from tkinter import *

# ... (le code de la calculatrice)

if __name__ == "__main__":
    master = Tk()
    master.title("Calculatrice")
    master.geometry("460x315")
    equation = StringVar()

    # ... (initialisation des composants Tkinter)

    master.mainloop()
