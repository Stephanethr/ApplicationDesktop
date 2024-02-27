import os
import sqlite3
from src.requetes_sql import *
from src.chiffrement import *

def connect_db():
    # Construire le chemin absolu vers la base de données
    database_folder = "../database"
    database_path_file = os.path.join(database_folder, "passGuardian.db")

    # Vérifier si le dossier database existe, sinon le créer
    if not os.path.exists(database_folder):
        os.makedirs(database_folder)


    # Vérifier si la base de données existe sinon la créer
    if not os.path.exists(database_path_file):
        # Si la base de données n'existe pas, créer la base de données et la structure de table
        conn = sqlite3.connect(database_path_file)
        cursor = conn.cursor()

        # Créer la base de données
        create_db(cursor)

        conn.commit()
        conn.close()

    # Connexion à la base de données
    conn = sqlite3.connect(database_path_file)
    cursor = conn.cursor()
    return conn, cursor

def close_db(conn):
    # Fermer la connexion à la base de données
    conn.close()

if __name__ == "__main__":
    conn, cursor = connect_db()
    create_user(cursor, "admin", encrypt_password("admin"))
    save_password(cursor, encrypt_password("password"), "category", "site", 1)
    conn.commit()
    close_db(conn)



