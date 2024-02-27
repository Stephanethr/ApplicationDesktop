class PassController:
    def __init__(self):
        self.passwords = {}

    def add_password(self, username, password):
        self.passwords[username] = password

    def get_password(self, username):
        return self.passwords.get(username, "Nom d'utilisateur non trouvé")