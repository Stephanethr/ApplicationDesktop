from cryptography.fernet import Fernet
class Chiffrement:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_password(self, password):
        return self.cipher_suite.encrypt(password.encode())

    def decrypt_password(self, encrypted_password):
        return self.cipher_suite.decrypt(encrypted_password).decode()
