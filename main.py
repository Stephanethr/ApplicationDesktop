from PassController import PassController
import hashlib


class Main:
    def __init__(self):
        self.controller = PassController()
        self.user = None
        self.isConnected = False
        self.running = True

    def connect_menu(self):
        print("=" * 30)
        print("PassGuardian")
        print("=" * 30 + "\n")
        choice = input("Se connecter (1), s'enregistrer (2) : ")
        if choice == "2":
            print("=" * 30)
            print("Création de compte")
            print("=" * 30 + "\n")
            username = input("Nom d'utilisateur : ")
            password = input("Mot de passe : ")
            password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            key = bytes.fromhex(password)
            self.controller.create_user(username, password)
            self.user = self.controller.get_user(username, password, key)
        else:
            username = input("Nom d'utilisateur : ")
            password = input("Mot de passe : ")
            password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            key = bytes.fromhex(password)
            self.user = self.controller.get_user(username, password, key)

    def main_menu(self):
        while self.running:
            print("\n" + "=" * 30)
            print("Bienvenue dans PassGuardian")
            print("=" * 30)
            print("1. Générer un mot de passe")
            print("2. Enregistrer un mot de passe")
            print("3. Voir les mots de passe enregistrés")
            print("4. Supprimer un mot de passe")
            print("5. Se déconnecter")
            choice = input("\nEntrez le numéro de votre choix : ")

            if choice == "1":
                self.generate_password_menu()
            elif choice == "2":
                password = input("Entrez le mot de passe : ")
                categoryName = input("Entrez la catégorie : ")
                siteName = input("Entrez le nom du site : ")
                self.controller.save_password(password, categoryName, siteName, self.user[0])
            elif choice == "3":
                print(self.controller.get_passwords(self.user[0]))
            elif choice == "4":
                print(self.controller.get_passwords(self.user[0]))
                password_id = input("Entrez l'id du mot de passe à supprimer : ")
                self.controller.delete_password(password_id)
            elif choice == "5":
                self.isConnected = False
                self.running = False
                return

    def generate_password_menu(self):
        choices = set()
        choice = None
        while choice != "5":
            print("\n" + "=" * 30)
            print("Créer votre mot de passe avec :")
            print("=" * 30)
            print("1. Des lettres minuscules [abc...]")
            print("2. Des lettres majuscules [ABC...]")
            print("3. Des chiffres [123...]")
            print("4. Des caractères spéciaux")
            print("5. Terminer la sélection")
            print("6. Retirer un choix")
            print("7. Retour au menu principal")
            print("Choix actuels : ", choices if choices else "Aucun")
            choice = input("Entrez le numéro de votre choix : ")

            if choice == "7":
                return
            elif choice == "6":
                remove_choice = int(input("Entrez le numéro du choix à retirer : "))
                choices.discard(remove_choice)
            elif choice != "5":
                 choices.add(int(choice))

        if choices:
            password_length = input("Nombre de caractères : ")
            password_count = input("Nombre de mots de passe : ")

            answers = {
                'password_options': list(choices),
                'password_length': int(password_length),
                'password_count': int(password_count),
            }

            print(self.controller.generate_password(answers))
            self.controller.print_user_inputs()

    def run(self):
        self.connect_menu()
        if self.user:
            self.isConnected = True
            print("Connecté en tant que", self.user)
            self.main_menu()


if __name__ == "__main__":
    app = Main()
    app.run()
