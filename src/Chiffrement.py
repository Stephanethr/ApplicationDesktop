import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Chiffrement:
    def __init__(self, password):
        """
        Initialise un nouvel objet Chiffrement.

        Args:
            password (str): Le mot de passe utilisé pour générer la clé.
        """
        self.key = self._derive_key(password)

    def _derive_key(self, password):
        """
        Dérive une clé de 32 octets à partir du mot de passe en utilisant SHA-256 et un sel.

        Args:
            password (str): Le mot de passe à partir duquel dériver la clé.

        Returns:
            bytes: La clé dérivée.
        """
        # TODO le sel crée des erreurs lors du déchiffrement puisque la clé est regénérée à chaque
        #  lancement de l'application, il faut alors trouver une solution fiable et sûre pour saler
        #  et réussir a déchiffrer les mdp

        # Génération d'un sel aléatoire
        #salt = os.urandom(16)

        # Concaténation du mot de passe avec le sel
        #password_with_salt = password.encode() + salt

        password_without_salt = password.encode()

        # Hashage du mot de passe avec le sel
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(password_without_salt)
        key = digest.finalize()
        return key

    def encrypt_password(self, plaintext):
        """
        Chiffre un texte donné en utilisant la clé dérivée.

        Args:
            plaintext (bytes): Le texte à chiffrer.

        Returns:
            tuple: Un tuple contenant l'IV (Initialisation Vector), le texte chiffré et le tag.
        """
        iv = os.urandom(16)  # Générer un IV aléatoire
        cipher = Cipher(algorithms.AES(self.key), modes.GCM(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        tag = encryptor.tag
        return iv, ciphertext, tag

    def decrypt(self, iv, ciphertext, tag):
        """
        Déchiffre un texte chiffré donné en utilisant la clé dérivée.

        Args:
            iv (bytes): L'Initialisation Vector.
            ciphertext (bytes): Le texte chiffré.
            tag (bytes): Le tag utilisé pour l'authentification.

        Returns:
            bytes: Le texte déchiffré.
        """
        cipher = Cipher(algorithms.AES(self.key), modes.GCM(iv, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext