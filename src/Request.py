from src.Connexion_db import ConnexionDB


class Request:
    def __init__(self):
        self.connexion = ConnexionDB()


    def create_db(self):
        self.connexion.cursor.executescript("""
        CREATE TABLE IF NOT EXISTS password (id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, password TEXT, categoryName TEXT, siteName TEXT, userID INTEGER, FOREIGN KEY(userID) REFERENCES user(id));
        CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, master_password TEXT);
        """)
        self.connexion.conn.commit()


    def save_password(self, login, password, categoryName, siteName, userID):
        self.connexion.cursor.execute("""
        INSERT INTO password (login, password, categoryName, siteName, userID) VALUES (? , ? , ? , ? , ?);
        """, (login, password, categoryName, siteName, userID))
        self.connexion.conn.commit()



    def create_user_bdd(self, username, password):
        self.connexion.cursor.execute("""
        INSERT INTO user (username, master_password) VALUES (?, ?);
        """, (username, password))
        self.connexion.conn.commit()



    def get_user_bdd(self, username, password):
        self.connexion.cursor.execute("""
        SELECT id,username FROM user WHERE username = ? AND master_password = ?;
        """, (username, password))
        return self.connexion.cursor.fetchone()

    def get_passwords(self, userID):
        self.connexion.cursor.execute("""
        SELECT id, login, password, categoryName, siteName FROM password WHERE userID = ?;
        """, (userID,))
        return self.connexion.cursor.fetchall()

    def delete_password(self, password_id):
        self.connexion.cursor.execute("""
        DELETE FROM password WHERE id = ?;
        """, (password_id,))
        self.connexion.conn.commit()

