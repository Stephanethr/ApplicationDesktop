from src.Connexion_db import ConnexionDB


class Request:
    def __init__(self):
        self.connexion = ConnexionDB()

    def save_password(self, login, password, categoryName, siteName, userID):
        self.connexion.get_cursor().execute("""
        INSERT INTO password (login, password, categoryName, siteName, userID) VALUES (? , ? , ? , ? , ?);
        """, (login, password, categoryName, siteName, userID))
        self.connexion.get_conn().commit()

    def create_user_bdd(self, username, password):
        self.connexion.get_cursor().execute("""
        INSERT INTO user (username, master_password) VALUES (?, ?);
        """, (username, password))
        self.connexion.get_conn().commit()

    def get_user_bdd(self, username, password):
        self.connexion.get_cursor().execute("""
        SELECT id, username FROM user WHERE username = ? AND master_password = ?;
        """, (username, password))
        return self.connexion.get_cursor().fetchone()

    def verify_user_exist(self, username):
        self.connexion.get_cursor().execute("""
        SELECT username FROM user WHERE username = ?;
        """, (username,))
        result = self.connexion.get_cursor().fetchone()
        if result is not None:
            if result[0] == username:
                return True
            else:
                return False




    def get_passwords(self, userID):
        self.connexion.get_cursor().execute("""
        SELECT id, login, password, categoryName, siteName FROM password WHERE userID = ?;
        """, (userID,))
        return self.connexion.get_cursor().fetchall()

    def delete_password(self, password_id):
        self.connexion.get_cursor().execute("""
        DELETE FROM password WHERE id = ?;
        """, (password_id,))
        self.connexion.get_conn().commit()
