from src.Request import Request
from src.Chiffrement import Chiffrement
from src.Generateur_mdp import Generateur


class PassController:
    def __init__(self):
        self.user_inputs = {}
        self.generation = Generateur()
        self.chiffrement = None
        self.request_db = Request()

    def generate_password(self, answers):
        """
            Cette méthode génère un mot de passe en fonction des réponses de l'utilisateur.

            Les réponses de l'utilisateur sont stockées dans une liste. Ensuite, la méthode vérifie si la longueur du mot de passe
            et les options de mot de passe fournies par l'utilisateur sont valides. Si elles sont valides, un mot de passe est généré
            et renvoyé.

            Args:
                answers (dict): Un dictionnaire contenant les réponses de l'utilisateur. Il doit contenir les clés 'password_length',
                'password_options' et 'password_count'.

            Returns:
                str: Le mot de passe généré si les entrées de l'utilisateur sont valides. Sinon, None est renvoyé.
        """
        self.user_inputs = answers
        if (self.generation.longueur_valide(self.user_inputs['password_length']) &
                self.generation.choix_utilisateur(self.user_inputs['password_options'])):

            mdp_genere = self.generation.generation_mdp()
            return mdp_genere

    def create_user(self, username, password):
        """
            Cette méthode crée un nouvel utilisateur dans la base de données.

            Args :
                username (str) : Le nom d'utilisateur pour le nouvel utilisateur.
                password (str) : Le mot de passe pour le nouvel utilisateur.

            Returns :
                User : L'utilisateur créé, ou 1 si un utilisateur avec le même nom d'utilisateur existe déjà.

        """
        already_exist = self.request_db.verify_user_exist(username)
        if already_exist:
            return None
        else:
            if self.chiffrement is None:
                self.createChiffrement(password)
            self.request_db.create_user_bdd(username, password)
            return self.request_db.get_user_bdd(username, password)

    def get_user(self, username, password):
        """
            Cette méthode récupère un utilisateur de la base de données.

            Elle crée d'abord un chiffrement avec la clé fourni et ensuite un nouvel utilisateur.

            Args:
                username (str): Le nom d'utilisateur de l'utilisateur à récupérer.
                password (str): Le mot de passe de l'utilisateur à récupérer.
                key (str): La clé utilisée pour créer le chiffrement.

            Returns:
                User: L'utilisateur récupéré de la base de données, ou None si aucun utilisateur ne correspond aux identifiants fournis.
            """
        if self.chiffrement is None:
            self.createChiffrement(password)
        user = self.request_db.get_user_bdd(username, password)
        return user

    def save_password(self, login, password, categoryName, siteName, userID):
        """
                Cette fonction chiffre le mot de passe fourni à l'aide de l'objet chiffrement de la classe
                actuelle.

            Args:
                self: L'instance de la classe actuelle.
                login (str): Le nom d'utilisateur associé au mot de passe.
                password (str): Le mot de passe non chiffré à enregistrer.
                categoryName (str): Le nom de la catégorie à laquelle le mot de passe appartient.
                siteName (str): Le nom du site ou du service associé au mot de passe.
                userID (str): L'identifiant de l'utilisateur auquel le mot de passe est associé.

        """
        if self.chiffrement is None:
            print("chiffrement is none ptn")
        cipher = self.chiffrement.encrypt_password(password)
        self.request_db.save_password(login, cipher, categoryName, siteName, userID)

    def get_passwords(self, userID):
        """
            Cette méthode récupère les mots de passe d'un utilisateur spécifique de la base de données.
            Les mots de passe récupérés sont déchiffrés avant d'être renvoyés.

            Args:
                userID (int): L'ID de l'utilisateur pour lequel récupérer les mots de passe.

            Returns:
                list: Une liste de tuples, chaque tuple contenant les détails d'un mot de passe. Les détails incluent l'ID du mot de passe,
                le nom du site, le mot de passe déchiffré, le nom d'utilisateur et l'URL du site.
        """
        res = self.request_db.get_passwords(userID)
        encrypted = [elt[2] for elt in res]
        for i in range(len(encrypted)):
            encrypted[i] = self.chiffrement.decrypt(encrypted[i].decode())
            res[i] = (res[i][0], res[i][1], encrypted[i], res[i][3], res[i][4])
        return res

    def delete_password(self, password_id):
        """
            Cette méthode supprime un mot de passe spécifique de la base de données.

            Args:
                password_id (int): L'ID du mot de passe à supprimer.
        """
        self.request_db.delete_password(password_id)

    def createChiffrement(self, password):
        """
            Cette méthode crée un objet de chiffrement avec le mot de passe fourni.

            L'objet de chiffrement est utilisé pour chiffrer et déchiffrer les données.

            Args:
                password (str): Le mot de passe utilisé pour créer l'objet de chiffrement.
        """
        key = bytes.fromhex(password)
        self.chiffrement = Chiffrement(key)
