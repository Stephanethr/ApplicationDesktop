def create_db():
    sqlRequest = ("""
    CREATE TABLE IF NOT EXISTS password (id INTEGER PRIMARY KEY, value TEXT, category integer, FOREIGN KEY(category) REFERENCES category(id));
    CREATE TABLE IF NOT EXISTS category (id INTEGER PRIMARY KEY, name TEXT); 
    CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username TEXT, master_password TEXT);
     """)
    return sqlRequest