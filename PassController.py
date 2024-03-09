from src import requetes_sql
from src import Connexion_db
from src import Chiffrement
from src import Generateur_mdp


class PassController:
    def __init__(self):
        self.user_inputs = {}
        self.mdp_genere = []
        self.chiffrement = Chiffrement.Chiffrement()
        self.generation = Generateur_mdp.Generation()

    def generate_password(self, answers):
        # enregistre les entrées de l'utilisateur dans une liste
        self.user_inputs = answers
        if (self.generation.longeur_valide(self.user_inputs['password_length']) &
                self.generation.choix_utilisateur(self.user_inputs['password_options'])):

            self.mdp_genere.append(self.generation.generation_mdp(self.user_inputs['password_count']))
            print(self.mdp_genere)
            self.mdp_genere.clear()

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
