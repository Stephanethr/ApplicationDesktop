from PassController import PassController


class Main:
    def __init__(self):
        self.controller = PassController()
        self.user_id = None

    def run(self):
        running = True
        while running:
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
                self.controller.create_user(username)
                self.user_id = self.controller.get_user(username)
            else:
                username = input("Nom d'utilisateur : ")
                password = input("Mot de passe : ")
                self.user_id = self.controller.get_user(username)
            print(self.user_id)
            choices = set()
            choice = None
            while choice != "5":
                print("\n" + "=" * 30)
                print("Créer votre mot de passe avec :")
                print("=" * 30)
                print("1. Des chiffres [123...]")
                print("2. Des lettres minuscules [abc...]")
                print("3. Des lettres majuscules [ABC...]")
                print("4. Des caractères spéciaux")
                print("5. Terminer la sélection")
                print("6. Retirer un choix")
                print("7. Quitter l'application")
                print("Choix actuels : ", choices if choices else "Aucun")
                choice = input("Entrez le numéro de votre choix : ")

                if choice == "7":
                    return
                elif choice == "6":
                    remove_choice = input("Entrez le numéro du choix à retirer : ")
                    choices.discard(remove_choice)
                elif choice != "5":
                    choices.add(choice)

            if choices:
                password_length = input("Nombre de caractères : ")
                password_count = input("Nombre de mots de passe : ")

                answers = {
                    'password_options': list(choices),
                    'password_length': password_length,
                    'password_count': password_count,
                }

                self.controller.generate_password(answers)
                self.controller.print_user_inputs()


if __name__ == "__main__":
    app = Main()
    app.run()