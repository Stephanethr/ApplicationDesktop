import os
import sqlite3
from src.createDB import create_db
def connect_db():
    # Construire le chemin absolu vers la base de données
    print("avant creation de base")
    database_folder = "../database"
    database_path = os.path.join(database_folder, "passGuardian.db")

    # Vérifier si le dossier database existe, sinon le créer
    if not os.path.exists(database_folder):
        os.makedirs(database_folder)


    # Vérifier si la base de données existe sinon la créer
    if not os.path.exists(database_path):
        # Si la base de données n'existe pas, créer la base de données et la structure de table
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.executescript(create_db())
        conn.commit()
        conn.close()

    # Connexion à la base de données
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    return conn, cursor

def close_db(conn):
    # Fermer la connexion à la base de données
    conn.close()

if __name__ == "__main__":
    conn, c = connect_db()
    close_db(conn)
    print(os.path.join("..", "database", "passGuardian.db"))


