import os
import sqlite3
from src.createDB import create_db
def connect_db():
    # Construire le chemin absolu vers la base de données
    print("avant creation de base")
    database_path = os.path.join("..", "database", "passGuardian.db")

    # Vérifier si la base de données existe
    if not os.path.exists(database_path):
        print("dans le if")
        # Si la base de données n'existe pas, créer la base de données et la structure de table
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        print(create_db())
        c.execute('''CREATE TABLE IF NOT EXISTS password (id INTEGER PRIMARY KEY, value TEXT, category INTEGER, FOREIGN KEY(category) REFERENCES category(id)); CREATE TABLE IF NOT EXISTS category (id INTEGER PRIMARY KEY, name TEXT); CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username TEXT, master_password TEXT);''')
        conn.commit()
        conn.close()

    # Connexion à la base de données
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    return conn, c

def close_db(conn):
    # Fermer la connexion à la base de données
    conn.close()

if __name__ == "__main__":
    conn, c = connect_db()
    close_db(conn)
    print(os.path.join("..", "database", "passGuardian.db"))


