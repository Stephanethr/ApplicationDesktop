import random
import threading
import time


class NombreAleatoire:
    def __init__(self):
        self.valeur_1 = 0
        self.valeur_2 = 0
        self.valeur_3 = 0
        self.valeur_4 = 0
        # Lorsque le thread est démaré il exécutera la méthode "generation_nbr_aleatoire"
        self.thread = threading.Thread(target=self.generation_nbr_aleatoire)
        # Permet d'exécuter le thread en arrière plan
        self.thread.daemon = True

    def generation_nbr_aleatoire(self):
        """
            Génère des nombres aléatoires pour les valeurs 1 à 4.

            Les valeurs générées sont des entiers aléatoires entre 3 et 5.
        """
        while True:
            self.valeur_1 = random.randint(3, 5)
            self.valeur_2 = random.randint(3, 5)
            self.valeur_3 = random.randint(3, 5)
            self.valeur_4 = random.randint(3, 5)
            time.sleep(2)

    def start(self):
        """
            Démarre le thread pour générer des nombres aléatoires.
        """
        self.thread.start()

    def get_nbr_aleatoire(self) -> tuple:
        """
        Récupère les valeurs aléatoires générées.

        :return: Les valeurs aléatoires pour les valeurs 1 à 4.
        :rtype: tuple
        """
        return self.valeur_1, self.valeur_2, self.valeur_3, self.valeur_4
