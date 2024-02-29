import secrets
import string
import random


class Generation:
    LONGEUR_MIN_MDP = 12
    LONGEUR_MAX_MDP = 21
    LONGEUR_MIN_CHOIX = 1
    LONGEUR_MAX_CHOIX = 4
    CHIFFRE_MIN_MDP = 3
    SYMBOLE_MIN_MDP = 3

    lettre_min = ''
    lettre_maj = ''
    chiffres = ''
    symboles = ''
    longeur_mdp = 0
    alphabet = ''
    nbr_chiffre_obligatoire = 0
    nbr_symbole_obligatoire = 0

    def __init__(self):
        self.lettre_min = string.ascii_lowercase
        self.lettre_maj = string.ascii_uppercase
        self.chiffres = string.digits
        self.symboles = string.punctuation

    def longeur_valide(self, longeur_mdp: int) -> bool:
        """
            Teste la validité de la longeur du mot de passe choisit
            entrer par l'utilisateur

            Test si la longeur du mot de passe est bien comprise
            entre 12 et 21. Si oui assigne le nombre entré par
            l'utilisateur à la varible de la classe.
            Sinon retourn False

            :param longeur_mdp: nombre entrer par l'utilisateur
            :type longeur_mdp: int
            :return: Choix valide ou non
            :rtype: bool
        """
        valide = True
        if longeur_mdp < self.LONGEUR_MIN_MDP or longeur_mdp > self.LONGEUR_MAX_MDP:
            print("La longeur du mot de passe n'est pas valide")
            valide = False
        else:
            self.longeur_mdp = longeur_mdp
        return valide

    def choix_alphabet_valide(self, choix: list[int]) -> bool:
        """
            Teste la validité des choix entrer par l'utilisateur

            Teste en premier la taille de la liste des choix,
            s'il y a plus de 4 choix alors il y a une erreur dans la liste
            soit un choix est supérieur à 4 soit un choix est entrer
            plusieurs fois dans la liste.
            Ensuite, on teste la validité des choix dans la liste
            si le nombre est compris entre 1 et 4 alors le choix est valide.

            :param choix: Liste entrer par l'utilisateur
            :type choix: list[int]
            :return: Choix valide ou non
            :rtype: bool
        """
        valide = True
        if len(choix) < self.LONGEUR_MIN_CHOIX or len(choix) > self.LONGEUR_MAX_CHOIX:
            print("Il y as trop de paramètre choisit le max est 4")
            valide = False

        for i in choix:
            if not self.LONGEUR_MIN_CHOIX <= i <= self.LONGEUR_MAX_CHOIX:
                print("Une des valeurs entré n'est pas valide (choix de 1 à 4)")
                valide = False
        return valide

    def choix_utilisateur(self, charactere_voulue: list[int]):
        """
            Crée un alphabet personnalisé selon les choix entré par l'utilisateur.

            Prend en paramètre une liste d'entiers représentant les types de caractères
            à inclure dans l'alphabet souhaité. Les entiers sont définis comme suit dans le dictionnaire
            conditions:

            1 : Lettres minuscules
            2 : Lettres majuscules
            3 : Chiffres
            4 : Symboles

            Par exemple, pour créer un alphabet contenant des lettres minuscules et des chiffres,
            l'utilisateur doit fournir la liste [1, 3].

            :param charactere_voulue: Liste d'entiers représentant les types de caractères à inclure.
            :type charactere_voulue: list[int]
        """
        conditions = {
            1: self.lettre_min,
            2: self.lettre_maj,
            3: self.chiffres,
            4: self.symboles
        }

        alphabet = ''
        if self.choix_alphabet_valide(charactere_voulue):
            for condition in charactere_voulue:
                alphabet += conditions[condition]
            self.alphabet = alphabet

            if any(chiffre in self.chiffres for chiffre in self.alphabet):
                self.nbr_chiffre_obligatoire = self.CHIFFRE_MIN_MDP
            if any(symbole in self.symboles for symbole in self.alphabet):
                self.nbr_symbole_obligatoire = self.SYMBOLE_MIN_MDP
        else:
            return "L'alphabet n'est pas valide"

    def generation_mdp(self) -> str:
        mot_de_passe = ''
        chiffre_generer = 0
        symbole_generer = 0

        longeur_mdp = self.longeur_mdp - self.nbr_chiffre_obligatoire - self.nbr_symbole_obligatoire
        for i in range(longeur_mdp):
            mot_de_passe += ''.join(secrets.choice(self.alphabet))

        while chiffre_generer < self.nbr_chiffre_obligatoire or symbole_generer < self.nbr_symbole_obligatoire:
            if chiffre_generer < self.nbr_chiffre_obligatoire and self.chiffres:
                mot_de_passe += ''.join(secrets.choice(self.chiffres))
                chiffre_generer += 1

            if symbole_generer < self.nbr_symbole_obligatoire and self.symboles:
                mot_de_passe += ''.join(secrets.choice(self.symboles))
                symbole_generer += 1

        """mélanger du mot de passe"""
        liste_mot_de_passe = list(mot_de_passe)
        random.shuffle(liste_mot_de_passe)
        mot_de_passe = ''.join(liste_mot_de_passe)
        return mot_de_passe


if __name__ == "__main__":
    test = Generation()
    test.longeur_valide(13)
    test.choix_utilisateur([1, 2, 3])
    print(test.generation_mdp())
