import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip
from Controller import Controller
import hashlib
import subprocess
import sv_ttk


class Main:

    def __init__(self):
        self.choices = None
        self.controller = Controller()
        self.user = None
        self.root = tk.Tk()
        self.root.title("PassGuardian")
        self.create_connect_menu()
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+%d+%d" % (width // 2, height // 2, width // 4, height // 4))

    def check_os_theme(self):
        """Checks DARK/LIGHT mode of Windows."""
        try:
            import winreg

            registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            reg_keypath = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize'
            try:
                reg_key = winreg.OpenKey(registry, reg_keypath)
            except FileNotFoundError:
                return "light"
            for i in range(1024):
                try:
                    value_name, value, _ = winreg.EnumValue(reg_key, i)
                    if value_name == 'AppsUseLightTheme':
                        if value == 0:
                            return "dark"
                except OSError:
                    break
            return "light"

        except ImportError:
            """Checks DARK/LIGHT mode of macos."""
            cmd = 'defaults read -g AppleInterfaceStyle'
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, shell=True)

            check = bool(p.communicate()[0])
            if check:
                return "dark"
            else:
                return "light"

    def create_connect_menu(self):
        self.connect_frame = ttk.Frame(self.root, padding="20")
        self.connect_frame.grid(row=0, column=0, padx=10, pady=10)

        self.username_label = ttk.Label(self.connect_frame, text="Nom d'utilisateur  ")
        self.username_label.grid(row=0, column=0, sticky=tk.E, pady=(5, 2))

        self.username_entry = ttk.Entry(self.connect_frame)
        self.username_entry.grid(row=0, column=1, padx=(0, 10), pady=(5, 2),
                                 sticky="ew")

        self.password_label = ttk.Label(self.connect_frame, text="Mot de passe  ")
        self.password_label.grid(row=1, column=0, sticky=tk.E, pady=(5, 2))

        self.password_entry = ttk.Entry(self.connect_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=(0, 10), pady=(5, 2),
                                 sticky="ew")

        self.login_button = ttk.Button(self.connect_frame, text="Se connecter", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        self.register_button = ttk.Button(self.connect_frame, text="Créer un compte", command=self.open_register_page)
        self.register_button.grid(row=3, column=0, columnspan=2, pady=(2, 10), padx=10,
                                  sticky="ew")

        self.register_button = ttk.Button(self.connect_frame, text="Fermer l'application", command=self.close_root)
        self.register_button.grid(row=4, column=0, columnspan=2, pady=(2, 10), padx=10, sticky="ew")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def close_root(self):
        self.root.destroy()

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
        self.register_frame.grid(row=0, column=0, padx=10, pady=10)

        self.new_username_label = ttk.Label(self.register_frame, text="Nom d'utilisateur  ")
        self.new_username_label.grid(row=0, column=0, sticky=tk.E, pady=(5, 2))

        self.new_username_entry = ttk.Entry(self.register_frame)
        self.new_username_entry.grid(row=0, column=1, padx=(0, 10), pady=(5, 2), sticky="ew")

        self.new_password_label = ttk.Label(self.register_frame, text="Mot de passe  ")
        self.new_password_label.grid(row=1, column=0, sticky=tk.E, pady=(5, 2))

        self.new_password_entry = ttk.Entry(self.register_frame, show="*")
        self.new_password_entry.grid(row=1, column=1, padx=(0, 10), pady=(5, 2), sticky="ew")

        self.register_button = ttk.Button(self.register_frame, text="S'enregistrer", command=self.register)
        self.register_button.grid(row=2, columnspan=2, pady=10, padx=10, sticky="ew")

        self.return_button = ttk.Button(self.register_frame, text="Retour à la page de connexion",
                                        command=self.close_register_page)
        self.return_button.grid(row=3, columnspan=2, pady=(2, 10), padx=10, sticky="ew")

        # Configuration de la grille pour centrer le cadre
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

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
        self.main_menu_frame.grid(row=0, column=0)

        title_style = ttk.Style()
        title_style.configure("Title.TLabel", font=("Helvetica", 24))

        self.welcome_label = ttk.Label(self.main_menu_frame, text="PassGuardian", style="Title.TLabel")
        self.welcome_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.generate_button = ttk.Button(self.main_menu_frame, text="Générer un mot de passe",
                                          command=self.generate_password_menu)
        self.generate_button.grid(row=1, column=0, pady=5, sticky="ew")

        self.register_password = ttk.Button(self.main_menu_frame, text="Enregistrer un mot de passe",
                                            command=self.register_password_func)
        self.register_password.grid(row=2, column=0, pady=5, sticky="ew")

        self.display_password = ttk.Button(self.main_menu_frame, text="Voir les mots de passe enregistrés",
                                           command=self.display_password_func)
        self.display_password.grid(row=3, column=0, pady=5, sticky="ew")

        self.logout_password = ttk.Button(self.main_menu_frame, text="Se déconnecter",
                                          command=self.logout_password_func)
        self.logout_password.grid(row=4, column=0, pady=5, sticky="ew")

        # Configuration de la grille pour centrer le cadre
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        """     TODO

        self.delete_password = ttk.Button(self.main_menu_frame, text="Supprimer un mot de passe",
                                           command=self.delete_password_func)
        self.delete_password.grid(row=4, column=0, pady=5)"""

    def generate_password_menu(self):

        if hasattr(self, "main_menu_frame"):
            self.main_menu_frame.destroy()

        self.generate_frame = ttk.Frame(self.root, padding="20")
        self.generate_frame.grid(row=0, column=0)

        result_frame = ttk.Frame(self.generate_frame, padding=5)
        result_frame.grid(row=1, column=0, pady=20, columnspan=3,
                          sticky=tk.W + tk.E)

        ttk.Label(result_frame, text="Mot de passe : ").pack(side='left')

        self.result_label = ttk.Label(result_frame, text="", anchor='w')
        self.result_label.pack(side='left')

        options = [
            {"name": "Des lettres minuscules [abc...]", "value": 1},
            {"name": "Des lettres majuscules [ABC...]", "value": 2},
            {"name": "Des chiffres [123...]", "value": 3},
            {"name": "Des caractères spéciaux", "value": 4}
        ]

        self.choices = set()

        # Met à jour les choix en vidant d'abord l'ensemble `self.choices`,
        # puis en ajoutant les valeurs des options cochées.
        def update_choices():
            self.choices.clear()
            for opt in options:
                if opt["value"] in choice_vars and choice_vars[opt["value"]].get() == 1:
                    self.choices.add(opt["value"])

        # Crée un dictionnaire de variables de case à cocher avec les options, et associe chaque variable à une
        # case à cocher dans la fenêtre tkinter.
        # Lorsqu'une case à cocher est cochée ou décochée, la fonction `update_choices` est appelée pour mettre
        # à jour les choix.
        choice_vars = {}
        for i, option in enumerate(options):
            choice_vars[option["value"]] = tk.IntVar()
            ttk.Checkbutton(self.generate_frame, text=option["name"], variable=choice_vars[option["value"]], onvalue=1,
                            offvalue=0, command=update_choices).grid(row=i + 2, column=0, sticky=tk.W,
                                                                     pady=5)

        ttk.Label(self.generate_frame, text="Nombre de caractères  ").grid(row=len(options) + 2, column=0, sticky=tk.W)
        self.password_length_entry = ttk.Entry(self.generate_frame)
        self.password_length_entry.grid(row=len(options) + 2, column=1, sticky=tk.W,
                                        pady=5)

        close_button = ttk.Button(self.generate_frame, text="Retour", command=self.close_generate_password_menu)
        close_button.grid(row=len(options) + 3, column=0, sticky=tk.W, pady=15,
                          padx=(0, 5))

        copy_button = ttk.Button(self.generate_frame, text="Copier", command=self.copy_password)
        copy_button.grid(row=1, column=0, columnspan=3, sticky=tk.E, pady=15,
                         padx=(5, 0))

        ok_button = ttk.Button(self.generate_frame, text="Confirmer", command=self.selection)
        ok_button.grid(row=len(options) + 3, column=2, sticky=tk.E, pady=10, padx=(5, 0))

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def selection(self):
        if self.choices:
            try:
                password_length = int(self.password_length_entry.get())
                answers = {
                    'password_options': list(self.choices),
                    'password_length': password_length
                }
                result = self.controller.generate_password(answers)
                if not result:
                    messagebox.showerror("Erreur", "La taille du mot de passe doit être entre 8 et 30")
                else:
                    self.result_label.config(text=result)
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides.")
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner au moins un choix.")

    def register_password_func(self):

        if hasattr(self, "main_menu_frame"):
            self.main_menu_frame.destroy()

        # Frame pour l'enregistrement du mot de passe
        register_password_frame = ttk.Frame(self.root, padding="20")
        register_password_frame.grid(row=0, column=0)

        # Label et champs pour le login
        login_label = ttk.Label(register_password_frame, text="Login  ")
        login_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        login_entry = ttk.Entry(register_password_frame)
        login_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        # Label et champs pour le mot de passe
        password_label = ttk.Label(register_password_frame, text="Mot de passe  ")
        password_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        password_entry = ttk.Entry(register_password_frame, show="*")
        password_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Label et champs pour la catégorie
        category_label = ttk.Label(register_password_frame, text="Catégorie  ")
        category_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        category_entry = ttk.Entry(register_password_frame)
        category_entry.grid(row=2, column=1, sticky=tk.W, pady=5)

        # Label et champs pour le nom du site
        site_label = ttk.Label(register_password_frame, text="Nom du site  ")
        site_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        site_entry = ttk.Entry(register_password_frame)
        site_entry.grid(row=3, column=1, sticky=tk.W, pady=5)

        # Bouton pour enregistrer le mot de passe
        save_button = ttk.Button(register_password_frame, text="Enregistrer",
                                 command=lambda: self.save_and_return_to_main_menu(login_entry.get(),
                                                                                   password_entry.get(),
                                                                                   category_entry.get(),
                                                                                   site_entry.get(),
                                                                                   self.user[0],
                                                                                   register_password_frame))
        save_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        # Bouton pour retourner au menu principal
        close_button = ttk.Button(register_password_frame, text="Retour",
                                  command=lambda: self.close_register_password_func(register_password_frame))
        close_button.grid(row=5, column=0, columnspan=2, pady=5, sticky="ew")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def close_register_password_func(self, frame):
        frame.destroy()
        self.main_menu_page()

    def save_and_return_to_main_menu(self, login, password, category, site, user_id, frame):
        self.controller.save_password(login, password, category, site, user_id)
        frame.destroy()
        self.main_menu_page()

    def display_password_func(self):

        if hasattr(self, "main_menu_frame"):
            self.main_menu_frame.destroy()

        # Frame pour l'enregistrement du mot de passe
        display_password_frame = ttk.Frame(self.root, padding="20")
        display_password_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Récupérer les mots de passe de l'utilisateur
        passwords = self.controller.get_passwords(self.user[0])

        # Créer un tableau avec des en-têtes
        headers = ["Login", "Catégorie", "Site", "Mot de passe", ""]
        for i, header in enumerate(headers):
            ttk.Label(display_password_frame, text=header.ljust(20)).grid(row=0, column=i, sticky=tk.W)

        # Fonction pour afficher le mot de passe en clair ou le masquer
        def show_password_clear(label, password):
            if label.cget("text") == password:
                label.config(text="*" * len(password))
            else:
                label.config(text=password)

        # Afficher les mots de passe dans le tableau
        for i, password in enumerate(passwords, start=1):
            login_label = ttk.Label(display_password_frame, text=password[1].ljust(20))
            login_label.grid(row=i, column=0, sticky=tk.W)

            category_label = ttk.Label(display_password_frame, text=password[3].ljust(20))
            category_label.grid(row=i, column=1, sticky=tk.W)

            site_label = ttk.Label(display_password_frame, text=password[4].ljust(20))
            site_label.grid(row=i, column=2, sticky=tk.W)

            password_label = ttk.Label(display_password_frame, text="*" * len(password[2]))
            password_label.grid(row=i, column=3, sticky=tk.W)

            # Bouton "Afficher" pour afficher ou masquer le mot de passe
            show_button = ttk.Button(display_password_frame, text="Afficher",
                                     command=lambda label=password_label, pw=password[2]: show_password_clear(label,
                                                                                                              pw))
            show_button.grid(row=i, column=4, padx=5)

            ttk.Button(display_password_frame, text="Copier",
                       command=lambda p=password[2]: self.copy_password_2(p)).grid(
                row=i, column=5, padx=5)
            ttk.Button(display_password_frame, text="Supprimer",
                       command=lambda id=password[0]: self.delete_password(id, display_password_frame)).grid(row=i,
                                                                                                             column=6,
                                                                                                             padx=5)

        # Bouton pour retourner au menu principal
        close_button = ttk.Button(display_password_frame, text="Retour au menu principal",
                                  command=lambda: self.close_display_password_frame(display_password_frame))
        close_button.grid(row=len(passwords) + 1, columnspan=7, pady=10)

        # Bouton pour retourner au menu principal
        close_button = ttk.Button(display_password_frame, text="Retour au menu principal",
                                  command=lambda: self.close_display_password_frame(display_password_frame))
        close_button.grid(row=len(passwords) + 1, columnspan=7, pady=10)

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

    def copy_password_2(self, password):
        pyperclip.copy(password)
        messagebox.showinfo("Copié", "Le mot de passe a été copié dans le presse-papiers.")

    def delete_password(self, id, display_password_frame):
        self.controller.delete_password(id)
        # Actualiser l'affichage des mots de passe
        display_password_frame.destroy()
        self.display_password_func()

    def close_generate_password_menu(self):
        self.generate_frame.destroy()
        self.main_menu_page()

    def return_to_connect_menu(self):
        # Fermez tous les autres frames actifs
        self.main_menu_frame.destroy()  # Supprimez le frame du menu principal s'il est ouvert
        # Reconstruisez le menu de connexion
        self.create_connect_menu()

    def logout_password_func(self):
        self.return_to_connect_menu()

    def run(self):
        print(self.check_os_theme())
        # Obtenez le thème du système d'exploitation
        os_theme = self.check_os_theme()

        # Utilisez le thème obtenu pour définir le thème dans sv_ttk
        sv_ttk.set_theme(os_theme)
        self.root.mainloop()


if __name__ == "__main__":
    app = Main()
    app.run()
