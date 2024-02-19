from tkinter import *

formule = ""


def clique(num):
    global formule
    formule = formule + str(num)
    equation.set(formule)


def egale_clique():
    try:
        global formule
        # eval permet de d'éxécuter la "formule" en python
        # par exemple 3+2 sera éxécuter comme si on l'avait écrit directement en dur
        resultat = str(eval(formule))
        equation.set(resultat)
        formule = resultat

    except:
        equation.set(" erreur ")
        formule = ""


def efface():
    global formule
    formule = ""
    equation.set("")


if __name__ == "__main__":
    master = Tk()
    master.title("Calculatrice")
    master.geometry("460x315")
    equation = StringVar()

    formule_field = Entry(master, textvariable=equation)
    formule_field.grid(columnspan=3, pady=30, padx=20, ipadx=100, ipady=10)

    # lambda pour les boutons permet de retarder l'appel de clique
    # jusqu'a ce que le bouton soit cliqué
    btn_1 = Button(master, text=' 1 ', command=lambda: clique(1), height=2, width=10)
    btn_1.grid(row=2, column=0)

    btn_2 = Button(master, text=' 2 ', command=lambda: clique(2), height=2, width=10)
    btn_2.grid(row=2, column=1)

    btn_3 = Button(master, text=' 3 ', command=lambda: clique(3), height=2, width=10)
    btn_3.grid(row=3, column=0)

    btn_4 = Button(master, text=' 4 ', command=lambda: clique(4), height=2, width=10)
    btn_4.grid(row=3, column=1)

    plus = Button(master, text=' + ', command=lambda: clique("+"), height=2, width=10)
    plus.grid(row=2, column=2)

    moins = Button(master, text=' - ', command=lambda: clique("-"), height=2, width=10)
    moins.grid(row=3, column=2)

    egale = Button(master, text=' = ', command=egale_clique, height=2, width=10)
    egale.grid(row=5, column=2)

    effacer = Button(master, text='effacer', command=efface, height=2, width=10)
    effacer.grid(row=6, column=2)

    master.mainloop()
