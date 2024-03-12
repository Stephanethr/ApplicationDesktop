from src import requetes_sql
from src import Connexion_db
from src import Chiffrement
from src import Generateur_mdp


class PassController:
    def __init__(self):
        self.user_inputs = {}
        self.generation = Generateur_mdp.Generation()
        self.chiffrement = None

    def generate_password(self, answers):
        # enregistre les entrées de l'utilisateur dans une liste
        self.user_inputs = answers
        if (self.generation.longueur_valide(self.user_inputs['password_length']) &
                self.generation.choix_utilisateur(self.user_inputs['password_options'])):

            mdp_genere = self.generation.generation_mdp(self.user_inputs['password_count'])
            return mdp_genere

    def print_user_inputs(self):
        print(self.user_inputs)

    def create_user(self, username, password):
        # déplacer conn dans requetes_sql
        conn = Connexion_db.ConnexionDB()
        conn.connect_db()
        requetes_sql.create_user_bdd(conn.cursor, username, password)
        conn.commit()
        conn.close()

    def get_user(self, username, password, key):
        self.createChiffrement(key)
        conn = Connexion_db.ConnexionDB()
        conn.connect_db()
        user = requetes_sql.get_user_bdd(conn.cursor, username, password)
        conn.close()
        return user

    def save_password(self, login, password, categoryName, siteName, userID):
        cipher = self.chiffrement.encrypt_password(password)
        conn = Connexion_db.ConnexionDB()
        conn.connect_db()
        requetes_sql.save_password(conn.cursor, login, cipher, categoryName, siteName, userID)
        conn.commit()
        conn.close()

    def get_passwords(self, userID):
        conn = Connexion_db.ConnexionDB()
        conn.connect_db()
        res = requetes_sql.get_passwords(conn.cursor, userID)
        conn.close()
        encrypted = [elt[2] for elt in res]
        for i in range(len(encrypted)):
            encrypted[i] = self.chiffrement.decrypt(encrypted[i].decode())
            res[i] = (res[i][0], res[i][1], encrypted[i], res[i][3], res[i][4])
        return res

    def delete_password(self, password_id):
        conn = Connexion_db.ConnexionDB()
        conn.connect_db()
        requetes_sql.delete_password(conn.cursor, password_id)
        conn.commit()
        conn.close()

    def createChiffrement(self, password):
        self.chiffrement = Chiffrement.Chiffrement(password)
