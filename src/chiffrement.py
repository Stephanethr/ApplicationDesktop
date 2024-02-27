from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Fonction pour chiffrer un mot de passe
def encrypt_password(password):
    return cipher_suite.encrypt(password.encode())

# Fonction pour déchiffrer un mot de passe
def decrypt_password(encrypted_password):
    return cipher_suite.decrypt(encrypted_password).decode()