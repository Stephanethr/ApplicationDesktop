import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip
from PassController import PassController
import hashlib


class Main:
    def __init__(self):
        self.choices = None
        self.controller = PassController()
        self.user = None
        self.root = tk.Tk()
        self.root.title("PassGuardian")
        self.create_connect_menu()

    def create_connect_menu(self):
        self.connect_frame = ttk.Frame(self.root, padding="20")
        self.connect_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.username_label = ttk.Label(self.connect_frame, text="Nom d'utilisateur:")
        self.username_label.grid(row=0, column=0, sticky=tk.W)
        self.username_entry = ttk.Entry(self.connect_frame)
        self.username_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        self.password_label = ttk.Label(self.connect_frame, text="Mot de passe:")
        self.password_label.grid(row=1, column=0, sticky=tk.W)
        self.password_entry = ttk.Entry(self.connect_frame, show="*")
        self.password_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        self.login_button = ttk.Button(self.connect_frame, text="Se connecter", command=self.login)
        self.login_button.grid(row=2, columnspan=2, pady=10)

        self.register_button = ttk.Button(self.connect_frame, text="S'enregistrer", command=self.open_register_page)
        self.register_button.grid(row=3, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = hashlib.sha256(self.password_entry.get().encode('utf-8')).hexdigest()
        self.user = self.controller.get_user(username, password)
        if self.user:
            self.close_connect_menu()
            self.main_menu_page()
        else:
            messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect")

    def close_connect_menu(self):
        self.connect_frame.destroy()

    def open_register_page(self):
        self.close_connect_menu()
        self.register_page()

    def register_page(self):
        self.register_frame = ttk.Frame(self.root, padding="20")
        self.register_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.new_username_label = ttk.Label(self.register_frame, text="Votre nom d'utilisateur:")
        self.new_username_label.grid(row=0, column=0, sticky=tk.W)
        self.new_username_entry = ttk.Entry(self.register_frame)
        self.new_username_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        self.new_password_label = ttk.Label(self.register_frame, text="Votre mot de passe:")
        self.new_password_label.grid(row=1, column=0, sticky=tk.W)
        self.new_password_entry = ttk.Entry(self.register_frame, show="*")
        self.new_password_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        self.register_button = ttk.Button(self.register_frame, text="S'enregistrer", command=self.register)
        self.register_button.grid(row=2, columnspan=2, pady=10)

        self.return_button = ttk.Button(self.register_frame, text="Retour à la page de connexion",
                                        command=self.close_register_page)
        self.return_button.grid(row=3, columnspan=2, pady=10)

    def register(self):
        self.close_connect_menu()
        new_username = self.new_username_entry.get()
        new_password = hashlib.sha256(self.new_password_entry.get().encode('utf-8')).hexdigest()
        if self.controller.create_user(new_username, new_password):
            messagebox.showinfo("Enregistrement réussi", "Votre compte a bien été créé.")
            self.close_register_page()
        else:
            messagebox.showerror("Erreur d'enregistrement", "Ce nom d'utilisateur existe déjà.")

    def close_register_page(self):
        self.register_frame.destroy()
        self.create_connect_menu()

    def main_menu_page(self):
        self.main_menu_frame = ttk.Frame(self.root, padding="20")
        self.main_menu_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.welcome_label = ttk.Label(self.main_menu_frame, text="Bienvenue dans PassGuardian")
        self.welcome_label.grid(row=0, column=0, columnspan=2)

        self.generate_button = ttk.Button(self.main_menu_frame, text="Générer un mot de passe",
                                          command=self.generate_password_menu)
        self.generate_button.grid(row=1, column=0, pady=5)

        self.logout_password = ttk.Button(self.main_menu_frame, text="Se déconnecter",
                                          command=self.logout_password_func)
        self.logout_password.grid(row=1, column=1, pady=5)

        self.register_password = ttk.Button(self.main_menu_frame, text="Enregistrer un mot de passe",
                                          command=self.register_password_func)
        self.register_password.grid(row=2, column=0, pady=5)

        self.display_password = ttk.Button(self.main_menu_frame, text="Voir les mots de passe enregistrés",
                                            command=self.display_password_func)
        self.display_password.grid(row=3, column=0, pady=5)
        """     TODO

        self.delete_password = ttk.Button(self.main_menu_frame, text="Supprimer un mot de passe",
                                           command=self.delete_password_func)
        self.delete_password.grid(row=4, column=0, pady=5)"""

    def generate_password_menu(self):
        self.generate_frame = ttk.Frame(self.root, padding="20")
        self.generate_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        close_button = ttk.Button(self.generate_frame, text="Retour", command=self.close_generate_password_menu)
        close_button.grid(row=0, column=1, columnspan=2, sticky=tk.E, pady=10)

        # Label pour afficher le résultat
        self.result_label = ttk.Label(self.generate_frame, text="")
        self.result_label.grid(row=1, column=0, pady=10)
        self.copy_button = ttk.Button(self.generate_frame, text="Copier le mot de passe", command=self.copy_password)
        self.copy_button.grid(row=1, column=1, pady=10)

        # Liste des options de choix avec leur nom et leur valeur
        options = [
            {"name": "Des lettres minuscules [abc...]", "value": 1},
            {"name": "Des lettres majuscules [ABC...]", "value": 2},
            {"name": "Des chiffres [123...]", "value": 3},
            {"name": "Des caractères spéciaux", "value": 4}
        ]

        # Définition des variables pour les choix
        self.choices = set()

        def update_choices():
            self.choices.clear()
            for option in options:
                if option["value"] in choice_vars and choice_vars[option["value"]].get() == 1:
                    self.choices.add(option["value"])

        # Variables pour les cases à cocher
        choice_vars = {}
        for i, option in enumerate(options):
            choice_vars[option["value"]] = tk.IntVar()
            ttk.Checkbutton(self.generate_frame, text=option["name"], variable=choice_vars[option["value"]], onvalue=1,
                            offvalue=0, command=update_choices).grid(row=i + 2, column=0, sticky=tk.W, pady=5)

        # Labels et entrées pour la longueur et le nombre de mots de passe
        ttk.Label(self.generate_frame, text="Nombre de caractères:").grid(row=len(options) + 2, column=0, sticky=tk.W)
        self.password_length_entry = ttk.Entry(self.generate_frame)
        self.password_length_entry.grid(row=len(options) + 2, column=1, sticky=tk.W, pady=5)

        # Bouton pour terminer la sélection
        ok_button = ttk.Button(self.generate_frame, text="Confirmer", command=self.selection)
        ok_button.grid(row=len(options) + 3, column=0, columnspan=2, sticky=tk.E, pady=10)

    def selection(self):
        if self.choices:
            try:
                password_length = int(self.password_length_entry.get())
                answers = {
                    'password_options': list(self.choices),
                    'password_length': password_length
                }

                result = self.controller.generate_password(answers)
                self.result_label.config(text=result)
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides.")
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner au moins un choix.")


    def register_password_func(self):
        # Frame pour l'enregistrement du mot de passe
        register_password_frame = ttk.Frame(self.root, padding="20")
        register_password_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Label et champs pour le login
        login_label = ttk.Label(register_password_frame, text="Login:")
        login_label.grid(row=0, column=0, sticky=tk.W)
        login_entry = ttk.Entry(register_password_frame)
        login_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        # Label et champs pour le mot de passe
        password_label = ttk.Label(register_password_frame, text="Mot de passe:")
        password_label.grid(row=1, column=0, sticky=tk.W)
        password_entry = ttk.Entry(register_password_frame, show="*")
        password_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Label et champs pour la catégorie
        category_label = ttk.Label(register_password_frame, text="Catégorie:")
        category_label.grid(row=2, column=0, sticky=tk.W)
        category_entry = ttk.Entry(register_password_frame)
        category_entry.grid(row=2, column=1, sticky=tk.W, pady=5)

        # Label et champs pour le nom du site
        site_label = ttk.Label(register_password_frame, text="Nom du site:")
        site_label.grid(row=3, column=0, sticky=tk.W)
        site_entry = ttk.Entry(register_password_frame)
        site_entry.grid(row=3, column=1, sticky=tk.W, pady=5)

        # Bouton pour enregistrer le mot de passe
        # Bouton pour enregistrer le mot de passe
        save_button = ttk.Button(register_password_frame, text="Enregistrer",
                                 command=lambda: self.save_and_return_to_main_menu(login_entry.get(),
                                                                                   password_entry.get(),
                                                                                   category_entry.get(),
                                                                                   site_entry.get(),
                                                                                   self.user[0],
                                                                                   register_password_frame))
        save_button.grid(row=4, columnspan=2, pady=10)


    def save_and_return_to_main_menu(self, login, password, category, site, user_id, frame):
        self.controller.save_password(login, password, category, site, user_id)
        frame.destroy()
        self.main_menu_page()


    def display_password_func(self):
        # Frame pour l'enregistrement du mot de passe
        display_password_frame = ttk.Frame(self.root, padding="20")
        display_password_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Récupérer les mots de passe de l'utilisateur
        passwords = self.controller.get_passwords(self.user[0])

        # Afficher les mots de passe dans la frame
        for i, password in enumerate(passwords, start=1):
            ttk.Label(display_password_frame, text=f"Login: {password[1]}").grid(row=i, column=0, sticky=tk.W)
            ttk.Label(display_password_frame, text=f"Mot de passe: {password[2]}").grid(row=i, column=1, sticky=tk.W)
            ttk.Label(display_password_frame, text=f"Catégorie: {password[3]}").grid(row=i, column=2, sticky=tk.W)
            ttk.Label(display_password_frame, text=f"Site: {password[4]}").grid(row=i, column=3, sticky=tk.W)

        # Bouton pour retourner au menu principal
        close_button = ttk.Button(display_password_frame, text="Retour au menu principal",
                                  command=lambda: self.close_display_password_frame(display_password_frame))
        close_button.grid(row=len(passwords) + 1, columnspan=4, pady=10)


    def close_display_password_frame(self, frame):
        frame.destroy()
        self.main_menu_page()


    def copy_password(self):
        password = self.result_label.cget("text")
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copié", "Le mot de passe a été copié dans le presse-papiers.")
        else:
            messagebox.showerror("Erreur", "Aucun mot de passe à copier.")

    def close_generate_password_menu(self):
        self.generate_frame.destroy()
        self.main_menu_page()


    def logout_password_func(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Main()
    app.run()
