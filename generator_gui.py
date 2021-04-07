from tkinter import *
from tkinter import messagebox
from random import random
from time import sleep
import webbrowser

from PIL import ImageTk,Image

my_img = Image("buty.png")

def ask_print():
    response = messagebox.askokcancel("Printing", "Do you really want to print?")
    if response:
        print("drukowanie")
        # drukowanie
    else:
        print("powrot")


def pisz():
    print('seima')
    i = 1
    if i < 7:
        # label = Label(root, text="").grid(row=i, column=1)
        label = Label(root, text=str(round(random(), 5)))
        label.grid(row=i, column=1)
        print(i)
        i = i + 1
        print(i)


    else:
        i = 1
        funkcja(i)


def funkcja(i):
    global guzik
    if i < 7:
        label = Label(frame2, text="").grid(row=i, column=1)
        label = Label(frame2, text=str(round(random(), 5)))

        label.grid(row=i, column=1)
        i = i + 1
        guzik = Button(buttons_display, text="enter your name", command=lambda: funkcja(i))
        guzik.grid(row=1, column=0)

    else:
        i = 1
        funkcja(i)
    # kwadratowa()
def openweb():
    url="www.deezee.pl"
    webbrowser.open(url)
    return


root = Tk()
root.title("Dzień kobiet")
root.geometry("800x600")

obraz = Label(image=my_img)
obraz.grid(row=0, column=5)
buttons_display = LabelFrame(root, text="buziki", bg="red",font="50")
buttons_display.grid(row=0, column=0, padx=50, pady=30)

frame2 = LabelFrame(root, text="Podgląd")
frame2.grid(row=0, column=1,padx=4)


print_button = Button(buttons_display, text="drukuj", command=ask_print, state=DISABLED)
print_button.grid(row=7, column=0)

guzik = Button(buttons_display, text="enter your name", command=lambda: openweb() ) #funkcja(1)
guzik.grid(row=1, column=0)

guzik1 = Button(buttons_display, text="1")
guzik1.grid(row=2, column=0)

guzik2 = Button(buttons_display, text="2")
guzik2.grid(row=2, column=1)

guzik3 = Button(buttons_display, text="3")
guzik3.grid(row=4, column=0)


root.mainloop()
