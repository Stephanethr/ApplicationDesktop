from src import requetes_sql
from src import Connexion_db
from src import Chiffrement


class PassController:
    def __init__(self):
        self.user_inputs = []
        self.chiffrement = Chiffrement.Chiffrement()

    def generate_password(self, answers):
        # enregistre les entrées de l'utilisateur dans une liste
        self.user_inputs.append(answers)

    def print_user_inputs(self):
        print(self.user_inputs)

    def create_user(self, username, password):
        conn = Connexion_db.ConnexionDB()
        conn.connect_db()
        requetes_sql.create_user_bdd(conn.cursor, username, password)
        conn.commit()
        conn.close()

    def get_user(self, username, password):
        conn = Connexion_db.ConnexionDB()
        conn.connect_db()
        user = requetes_sql.get_user_bdd(conn.cursor, username, password)
        conn.close()
        return user
