from src.Request import Request
from src.Chiffrement import Chiffrement
from src.Generateur_mdp import Generateur


class Controller:
    MAX_LONGUEUR_MDP = 30
    MIN_LONGUEUR_MDP = 8

    def __init__(self):
        self.generation = Generateur()
        self.chiffrement = None
        self.request_db = Request()

    def generate_password(self, answers: dict) -> str or bool:
        """
        Génère un mot de passe en fonction des réponses fournies.

        Teste la validité de la longueur du mot de passe spécifiée par l'utilisateur.
        Si la longueur spécifiée n'est pas comprise entre les valeurs minimale et maximale définies dans la classe,
        retourne False. Sinon, utilise la classe Generation pour générer un mot de passe.

        :param answers: Dictionnaire contenant les réponses de l'utilisateur, notamment la longueur et les options du mot de passe.
        :type answers: dict
        :return: Mot de passe généré ou False si la longueur spécifiée est invalide.
        :rtype: str or bool
        """
        if answers['password_length'] < self.MIN_LONGUEUR_MDP or answers['password_length'] > self.MAX_LONGUEUR_MDP:
            mdp_genere = False
        else:
            self.generation.set_longueur_mdp(answers['password_length'])
            mdp_genere = self.generation.generation(answers['password_options'])
        return mdp_genere

    def create_user(self, username, master_password):
        """
            Cette méthode crée un nouvel utilisateur dans la base de données.

            Args :
                username (str) : Le nom d'utilisateur pour le nouvel utilisateur.
                master_password (str) : Le mot de passe pour le nouvel utilisateur.

            Returns :
                User : L'utilisateur créé, ou None si un utilisateur avec le même nom d'utilisateur existe déjà.

        """
        already_exist = self.request_db.verify_user_exist(username)
        if already_exist:
            return None
        else:
            if self.chiffrement is None:
                self.createChiffrement(master_password)
            self.request_db.create_user_bdd(username, master_password)
            return self.request_db.get_user_bdd(username, master_password)

    def get_user(self, username, master_password):
        """
            Cette méthode récupère un utilisateur de la base de données.

            Elle crée d'abord un chiffrement avec la clé fourni et ensuite un nouvel utilisateur.

            Args:
                username (str): Le nom d'utilisateur de l'utilisateur à récupérer.
                master_password (str): Le mot de passe de l'utilisateur à récupérer.

            Returns:
                User: L'utilisateur récupéré de la base de données, ou None si aucun utilisateur ne correspond aux identifiants fournis.
            """
        if self.chiffrement is None:
            self.createChiffrement(master_password)
        user = self.request_db.get_user_bdd(username, master_password)
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
        password_bytes = password.encode('utf-8')  # ou 'latin-1' selon l'encodage de votre choix
        if self.chiffrement is None:
            print("Pas d'objet chiffrement instancié")
        iv, cipher, tag = self.chiffrement.encrypt_password(password_bytes)
        self.request_db.save_password(login, cipher, categoryName, siteName, userID, iv, tag)

    def get_passwords(self, userID):
        """
        Récupère les mots de passe d'un utilisateur spécifique de la base de données.
        Les mots de passe récupérés sont déchiffrés avant d'être renvoyés.

        Args:
            userID (int): L'ID de l'utilisateur pour lequel récupérer les mots de passe.

        Returns:
            list: Une liste de tuples, chaque tuple contenant les détails d'un mot de passe.
                  Les détails incluent l'ID du mot de passe, le nom du site, le mot de passe déchiffré,
                  le nom d'utilisateur et l'URL du site.
        """
        # Récupérer les données chiffrées depuis la base de données
        res = self.request_db.get_passwords(userID)

        # Extraire les textes chiffrés, IVs et tags
        ciphers = [elt[2] for elt in res]
        ivs = [elt[5] for elt in res]
        tags = [elt[6] for elt in res]

        # Déchiffrer les mots de passe
        for i in range(len(ciphers)):
            decrypted_password = self.chiffrement.decrypt(ivs[i], ciphers[i], tags[i])
            res[i] = (res[i][0], res[i][1], decrypted_password.decode('utf-8'), res[i][3], res[i][4])
        return res

    def delete_password(self, password_id):
        """
            Cette méthode supprime un mot de passe spécifique de la base de données.

            Args:
                password_id (int): L'ID du mot de passe à supprimer.
        """
        self.request_db.delete_password(password_id)

    def createChiffrement(self, master_password):
        """
            Cette méthode crée un objet de chiffrement avec le mot de passe fourni.

            L'objet de chiffrement est utilisé pour chiffrer et déchiffrer les données.

            Args:
                master_password (str): Le mot de passe utilisé pour créer l'objet de chiffrement.
        """
        self.chiffrement = Chiffrement(master_password)
