import string
import random


class Generateur:
    LONGUEUR_MIN_MDP = 12
    LONGUEUR_MAX_MDP = 21
    longueur_mdp = 0
    lettre_min = ''
    lettre_maj = ''
    chiffres = ''
    symboles = ''

    def __init__(self):
        self.lettre_min = string.ascii_lowercase
        self.lettre_maj = string.ascii_uppercase
        self.chiffres = string.digits
        self.symboles = string.punctuation

    def set_longueur_mdp(self, longueur_mdp: int):
        self.longueur_mdp = longueur_mdp

    def generation(self, caractere_voulu: list[int]) -> str:
        """"
        Génère un mot de passe basé sur les caractères spécifiés.

        Méthode génère un mot de passe en fonction des caractères spécifiés.
        Pour chaque type de caractère spécifié dans la liste 'caractere_voulu', cette méthode sélectionne
        un nombre aléatoire de ces caractères et les combine pour former un mot de passe.

        :param caractere_voulu: Liste d'entiers représentant les types de caractères souhaités.
            1 pour les lettres minuscules, 2 pour les lettres majuscules, 3 pour les chiffres, 4 pour les symboles.
        :type caractere_voulu: list[int]
        :return: Le mot de passe généré.
        :rtype: str

        """
        conditions = {
            1: self.lettre_min,
            2: self.lettre_maj,
            3: self.chiffres,
            4: self.symboles
        }

        mot_de_passe = ''
        resultats = self.nombre_aleatoire(caractere_voulu)

        for i, nombre in enumerate(resultats):
            caracteres_possibles = conditions[caractere_voulu[i]]
            mot_de_passe += ''.join(random.choices(caracteres_possibles, k=nombre))

        liste_mot_de_passe = list(mot_de_passe)
        random.shuffle(liste_mot_de_passe)
        mot_de_passe = ''.join(liste_mot_de_passe)

        return mot_de_passe

    def nombre_aleatoire(self, choix_utilisateur: list[int]) -> list[int]:
        nombres_aleatoires = []
        reste_iterations = len(choix_utilisateur) - 1
        longueur_restante = self.longueur_mdp - reste_iterations

        for _ in range(len(choix_utilisateur)):
            valeur_aleatoire = random.randint(1, longueur_restante)
            nombres_aleatoires.append(valeur_aleatoire)
            reste_iterations -= 1
            reste = self.longueur_mdp - sum(nombres_aleatoires)
            longueur_restante = reste - reste_iterations

        if sum(nombres_aleatoires) < self.longueur_mdp:
            value = random.choice(nombres_aleatoires)
            index = nombres_aleatoires.index(value)
            nombres_aleatoires[index] = value + (self.longueur_mdp - sum(nombres_aleatoires))

        random.shuffle(nombres_aleatoires)
        return nombres_aleatoires
