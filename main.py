from controller import PassController

class Main:
    def __init__(self):
        self.controller = PassController

    def run(self):
        running = True
        while running:
            print("1. Ajouter un mot de passe")
            print("2. Récupérer un mot de passe")
            print("3. Quitter")

            choice = input("Que voulez-vous faire ? ")

            if choice == "1":
                username = input("Nom d'utilisateur : ")
                password = input("Mot de passe : ")
                "self.controller.add_password(username, password)"
            elif choice == "2":
                username = input("Nom d'utilisateur : ")
                "password = self.controller.get_password(username)"
                print("Mot de passe : ", password)
            elif choice == "3":
                running = False
            else:
                print("Choix invalide")

if __name__ == "__main__":
    app = Main()
    app.run()