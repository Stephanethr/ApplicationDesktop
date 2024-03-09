import os
import sqlite3
from src.requetes_sql import *
from src.Chiffrement import *


class ConnexionDB:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def get_cursor(self):
        return self.cursor

    def get_conn(self):
        return self.conn

    def connect_db(self):
        # Construire le chemin vers la base de données
        database_folder = os.path.join(os.path.dirname(__file__), "../database")
        database_path_file = os.path.join(database_folder, "passGuardian.db")

        # Vérifier si le dossier database existe, sinon le créer
        if not os.path.exists(database_folder):
            os.makedirs(database_folder)

        # Vérifier si la base de données existe sinon la créer
        if not os.path.exists(database_path_file):
            # Si la base de données n'existe pas, créer la base de données et la structure de table
            self.conn = sqlite3.connect(database_path_file)
            self.cursor = self.conn.cursor()

            # Créer la base de données
            create_db(self.cursor)

            self.conn.commit()
            self.conn.close()

        # Connexion à la base de données
        self.conn = sqlite3.connect(database_path_file)
        self.cursor = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    chiffrement = Chiffrement()
    connDB = ConnexionDB()
    connDB.connect_db()

    create_user_bdd(connDB.get_cursor(), "admin", chiffrement.encrypt_password("admin"))
    save_password(connDB.get_cursor(), chiffrement.encrypt_password("password"), "category", "site", 1)
    connDB.commit()
    connDB.close()
