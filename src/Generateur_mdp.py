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

    def nombre_aleatoire(self, liste_choix_utilisateur: list[int]) -> list[int]:
        """
        Génère une liste de nombres aléatoires basée sur la taille de la liste de choix de l'utilisateur.

        Méthode qui génère une liste de nombres aléatoires en fonction de la taille de la liste de choix de
        l'utilisateur.
        Les nombres aléatoires générés sont utilisés pour déterminer la répartition des caractères dans le mot de passe.

        :param liste_choix_utilisateur: Liste d'entiers représentant les choix de l'utilisateur.
        :type liste_choix_utilisateur: list[int]
        :return: Liste de nombres aléatoires.
        :rtype: list[int]

        """
        reste_longueur_mdp = self.longueur_mdp
        nbr_aleatoire = []
        nbr_rand = 0
        nbr_valeur = len(liste_choix_utilisateur)

        while len(nbr_aleatoire) < nbr_valeur:
            if reste_longueur_mdp > 1:

                # 'reste_longueur_mdp' est le reste de la place qu'il reste dans le mot de passe pour
                # que le random ensuite ne soit pas trop grand
                nbr_rand = random.randint(1, reste_longueur_mdp)
                nbr_aleatoire.append(nbr_rand)
                reste_longueur_mdp = reste_longueur_mdp - nbr_rand
            else:
                # Évite l'erreur de plage invalide de randint (randint ne peut avoir une plage de 1, 1)
                # on fait une division entière de la valeur max de la liste par un random allant de 2 à max - 1
                # pour éviter que la variable 'nouvelle_valeur' soit égale à elle-même ou à un.
                reste_longueur_mdp += 1
                maxi = max(nbr_aleatoire)
                nouvelle_valeur = maxi // random.randint(2, maxi - 1)

                # Trouve l'index de la valeur max de la liste et soustrait la valeur 'nouvelle_valeur' à
                # maxi puis ajoute la nouvelle valeur à la liste.
                index_maxi = nbr_aleatoire.index(maxi)
                nbr_aleatoire[index_maxi] = maxi - nouvelle_valeur
                nbr_aleatoire.append(nouvelle_valeur)

        # La difference entre la somme de la liste et la longeur du mot de passe pour que le mot de passe ne soit
        # pas supérieur ou inférieur à la taille du mot de passe demandé par l'utilisateur.
        difference = sum(nbr_aleatoire) - self.longueur_mdp
        if difference > 0:
            maxi = max(nbr_aleatoire)
            index_maxi = nbr_aleatoire.index(maxi)
            nbr_aleatoire[index_maxi] = maxi - difference

        elif difference < 0:
            mini = min(nbr_aleatoire)
            index_min = nbr_aleatoire.index(mini)
            nbr_aleatoire[index_min] = mini - difference

        random.shuffle(nbr_aleatoire)
        return nbr_aleatoire
