import secrets
import string


class Generation:
    LONGEUR_MIN_MDP = 12
    LONGEUR_MAX_MDP = 21
    LONGEUR_MIN_CHOIX = 1
    LONGEUR_MAX_CHOIX = 4

    lettre_min = ''
    lettre_maj = ''
    chiffres = ''
    symboles = ''
    longeur_mdp = 0
    alphabet = ''

    def __init__(self):
        self.lettre_min = string.ascii_lowercase
        self.lettre_maj = string.ascii_uppercase
        self.chiffres = string.digits
        self.symboles = string.punctuation

    def longeur_valide(self, longeur_mdp: int) -> bool:
        valide = True
        if self.longeur_mdp < self.LONGEUR_MIN_MDP or self.longeur_mdp > self.LONGEUR_MAX_MDP:
            print("La longeur du mot de passe n'est pas valide")
            self.longeur_mdp = longeur_mdp
            valide = False
        return valide

    def choix_alphabet_valide(self, choix: list) -> bool:
        """
                Teste la validité des choix entrer par l'utilisateur

                Teste en premier la taille de la liste des choix,
                s'il y a plus de 4 choix alors il y a une erreur dans la liste
                soit un choix est supérieur à 4 soit un choix est entrer
                plusieurs fois dans la liste.
                Ensuite, on teste la validité des choix dans la liste
                si le nombre est compris entre 1 et 4 alors le choix est valide.

                :param choix: Liste entrer par l'utilisateur
                :type choix: list
                :return: Choix valide ou non
                :rtype: bool
        """
        valide = True
        if len(choix) < self.LONGEUR_MIN_CHOIX or len(choix) > self.LONGEUR_MAX_CHOIX:
            print("Choix trop élévé il y a une erreur")
            valide = False

        for i in choix:
            if not self.LONGEUR_MIN_CHOIX <= i <= self.LONGEUR_MAX_CHOIX:
                valide = False
        return valide

    def choix_utilisateur(self, charactere_voulue: list):
        conditions = {
            1: self.lettre_min,
            2: self.lettre_maj,
            3: self.chiffres,
            4: self.symboles
        }
        alphabet = ''
        for condition in charactere_voulue:
            alphabet += conditions[condition]
        self.alphabet = alphabet


"""
def generation():
    LONGUEUR_MDP = 12
    lettres_maj_min = string.ascii_letters
    chiffres = string.digits
    symboles = string.punctuation
    alphabet = lettres_maj_min + chiffres + symboles

    mdp_validation = True
    while mdp_validation:
        mot_de_passe = ''
        for i in range(LONGUEUR_MDP):
            mot_de_passe += ''.join(secrets.choice(alphabet))

        if (any(i in symboles for i in mot_de_passe) and
                sum(i in chiffres for i in mot_de_passe) >= 2):
            mdp_validation = False

    return mot_de_passe
"""
if __name__ == "__main__":
    test = Generation()
    print(test.choix_alphabet_valide([1]))


