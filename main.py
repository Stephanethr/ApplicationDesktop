from tkinter import *

formule = ""


def click(num):
    global formule
    formule = formule + str(num)
    equation.set(formule)


def equalclick():
    try:
        global formule

        result = str(eval(formule))
        equation.set(result)
        formule = result

    except:
        equation.set(" error ")
        formule = ""


def effacer():
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
    btn_1 = Button(master, text=' 1 ', command=lambda: click(1), height=2, width=10)
    btn_1.grid(row=2, column=0)

    btn_2 = Button(master, text=' 2 ', command=lambda: click(2), height=2, width=10)
    btn_2.grid(row=2, column=1)

    btn_3 = Button(master, text=' 3 ', command=lambda: click(3), height=2, width=10)
    btn_3.grid(row=3, column=0)

    btn_4 = Button(master, text=' 4 ', command=lambda: click(4), height=2, width=10)
    btn_4.grid(row=3, column=1)


    plus = Button(master, text=' + ', command=lambda: click("+"), height=2, width=10)
    plus.grid(row=2, column=2)

    minus = Button(master, text=' - ', command=lambda: click("-"), height=2, width=10)
    minus.grid(row=3, column=2)


    equal = Button(master, text=' = ', command=equalclick, height=2, width=10)
    equal.grid(row=5, column=2)

    effacer = Button(master, text='effacer', command=effacer, height=2, width=10)
    effacer.grid(row=6, column=2)


    master.mainloop()