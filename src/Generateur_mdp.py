import secrets
import string


class Generation:
    LONGEUR_MIN = 12
    LONGEUR_MAX = 21
    lettre_min = ''
    lettre_maj = ''
    chiffres = ''
    symboles = ''
    longeur_mdp = 0

    def __init__(self, longeur_mdp):
        self.lettre_min = string.ascii_lowercase
        self.lettre_maj = string.ascii_uppercase
        self.chiffres = string.digits
        self.symboles = string.punctuation
        self.longeur_mdp = longeur_mdp

    def longeur_valide(self):
        valide = True
        if self.longeur_mdp < self.LONGEUR_MIN or self.longeur_mdp > self.LONGEUR_MAX:
            print("La longeur du mot de passe n'est pas valide")
            valide = False
        return valide

    def generation_mdp_lettres_chiffres(self):
        alphabet_lettres_chiffres = self.chiffres + self.lettre_maj + self.chiffres
        mdp_validation = True
        while mdp_validation:
            mot_de_passe = ''
            for i in range(self.longeur_mdp):
                mot_de_passe += ''.join(secrets.choice(alphabet_lettres_chiffres))

            if sum(i in self.chiffres for i in mot_de_passe) >= 2:
                mdp_validation = False


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