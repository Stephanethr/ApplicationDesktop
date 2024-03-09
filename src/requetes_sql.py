def create_db(cursor):
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS password (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT, categoryName TEXT, siteName TEXT, userID INTEGER, FOREIGN KEY(userID) REFERENCES user(id));
    CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, master_password TEXT);
    """)


def save_password(cursor, password, categoryName, siteName, userID):
    cursor.execute("""
    INSERT INTO password (password, categoryName, siteName, userID) VALUES (? , ? , ? , ?);
    """, (password, categoryName, siteName, userID))


def create_user_bdd(cursor, username, password):
    cursor.execute("""
    INSERT INTO user (username, master_password) VALUES (?, ?);
    """, (username, password))


def get_user_bdd(cursor, username, password):
    cursor.execute("""
    SELECT id,username FROM user WHERE username = ? AND master_password = ?;
    """, (username, password))
    return cursor.fetchone()

def get_passwords(cursor, userID):
    cursor.execute("""
    SELECT * FROM password WHERE userID = ?;
    """, (userID,))
    return cursor.fetchone()

def delete_password(cursor, password_id):
    cursor.execute("""
    DELETE FROM password WHERE id = ?;
    """, (password_id,))
