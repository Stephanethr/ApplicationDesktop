import string
import secrets
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







print(generation())