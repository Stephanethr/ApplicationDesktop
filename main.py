import tkinter as tk
from tkinter import ttk
from PassController import PassController
import hashlib


class Main:
    def __init__(self):
        self.controller = PassController()
        self.user = None
        self.running = True
        self.error_label = None  # Variable pour stocker la référence à l'étiquette d'erreur

    def connect_menu(self):
        self.root = tk.Tk()
        self.root.title("PassGuardian")

        # Frame pour le menu de connexion
        self.connect_frame = ttk.Frame(self.root, padding="20")
        self.connect_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Label et champs pour le nom d'utilisateur
        self.username_label = ttk.Label(self.connect_frame, text="Nom d'utilisateur:")
        self.username_label.grid(row=0, column=0, sticky=tk.W)
        self.username_entry = ttk.Entry(self.connect_frame)
        self.username_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        # Label et champs pour le mot de passe
        self.password_label = ttk.Label(self.connect_frame, text="Mot de passe:")
        self.password_label.grid(row=1, column=0, sticky=tk.W)
        self.password_entry = ttk.Entry(self.connect_frame, show="*")
        self.password_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Bouton de connexion
        self.login_button = ttk.Button(self.connect_frame, text="Se connecter", command=self.login)
        self.login_button.grid(row=2, columnspan=2, pady=10)

        # Bouton pour passer à la page d'enregistrement
        self.register_button = ttk.Button(self.connect_frame, text="S'enregistrer", command=self.close_connect_menu)
        self.register_button.grid(row=3, columnspan=2, pady=10)

        self.root.mainloop()

    def close_connect_menu(self):
        # Cacher la fenêtre de connexion
        self.root.withdraw()
        # Ouvrir la page d'enregistrement
        self.register_page()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.user = self.controller.get_user(username, password)
        if self.user:
            self.connect_frame.destroy()  # Supprimer les widgets de connexion
            self.root.destroy()  # Fermer la fenêtre de connexion
        else:
            # Afficher un message d'erreur si la connexion échoue
            if self.error_label:
                self.error_label.destroy()  # Supprimer le message d'erreur précédent s'il existe
            self.error_label = ttk.Label(self.connect_frame, text="Nom d'utilisateur ou mot de passe incorrect",
                                         foreground="red")
            self.error_label.grid(row=4, columnspan=2)

    def register_page(self):
        # Création d'une nouvelle fenêtre pour la page d'enregistrement
        self.register_window = tk.Toplevel(self.root)
        self.register_window.title("Enregistrement")

        # Frame pour la page d'enregistrement
        self.register_frame = ttk.Frame(self.register_window, padding="20")
        self.register_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Label et champs pour le nom d'utilisateur
        self.new_username_label = ttk.Label(self.register_frame, text="Votre nom d'utilisateur:")
        self.new_username_label.grid(row=0, column=0, sticky=tk.W)
        self.new_username_entry = ttk.Entry(self.register_frame)
        self.new_username_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        # Label et champs pour le mot de passe
        self.new_password_label = ttk.Label(self.register_frame, text="Votre mot de passe:")
        self.new_password_label.grid(row=1, column=0, sticky=tk.W)
        self.new_password_entry = ttk.Entry(self.register_frame, show="*")
        self.new_password_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Bouton pour valider l'enregistrement
        self.register_button = ttk.Button(self.register_frame, text="S'enregistrer", command=self.register)
        self.register_button.grid(row=2, columnspan=2, pady=10)

        # Bouton pour retourner à la page de connexion
        self.return_button = ttk.Button(self.register_frame, text="Retour à la page de connexion",
                                        command=self.close_register_page)
        self.return_button.grid(row=3, columnspan=2, pady=10)

    def register(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()
        new_password = hashlib.sha256(new_password.encode('utf-8')).hexdigest()
        self.user = self.controller.create_user(new_username, new_password)

        if self.user:
            if self.register_window:
                self.register_window.destroy()  # Vérifier si la fenêtre existe avant de la détruire
            self.root.destroy()  # Fermer la fenêtre de connexion
        else:
            # self.user vaut 1 car un utilisateur ayant le même login à été trouvé
            # TODO afficher un message d'erreur
            print("Un utilisateur ayant ce login existe déjà")
            return

    def close_register_page(self):
        # Fermer la fenêtre d'enregistrement
        self.register_window.destroy()
        # Afficher à nouveau la fenêtre principale
        self.root.deiconify()

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
                login = input("Entrez le login : ")
                password = input("Entrez le mot de passe : ")
                categoryName = input("Entrez la catégorie : ")
                siteName = input("Entrez le nom du site : ")
                self.controller.save_password(login, password, categoryName, siteName, self.user[0])
            elif choice == "3":
                print(self.controller.get_passwords(self.user[0]))
            elif choice == "4":
                print(self.controller.get_passwords(self.user[0]))
                password_id = int(input("Entrez l'id du mot de passe à supprimer : "))
                self.controller.delete_password(password_id)
            elif choice == "5":
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
            print("Connecté en tant que", self.user)
            self.main_menu()


if __name__ == "__main__":
    app = Main()
    app.run()
