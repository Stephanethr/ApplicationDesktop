from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class Chiffrement:
    def __init__(self, key):
        self.key = key

    def encrypt_password(self, password):
        cipher = AES.new(self.key, AES.MODE_CBC)
        texte_padded = pad(password.encode(), AES.block_size)
        cipher_text = cipher.encrypt(texte_padded)
        return cipher.iv, cipher_text

    def decrypt(self, iv, cypher_text):
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = unpad(cipher.decrypt(cypher_text), AES.block_size)
        return plain_text.decode()
