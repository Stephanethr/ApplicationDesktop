import base64
from cryptography.fernet import Fernet

class Chiffrement:
    def __init__(self, key):
        if not isinstance(key, bytes):
            raise TypeError("La clé doit être de type bytes.")
        self.key = base64.urlsafe_b64encode(key)

    def encrypt_password(self, password):
        f = Fernet(self.key)
        cipher_text = f.encrypt(password.encode())
        return cipher_text

    def decrypt(self, cipher_text):
        f = Fernet(self.key)
        plain_text = f.decrypt(cipher_text).decode()
        return plain_text
