from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry('500x300')
root.minsize(400, 300)

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

value = Entry(root, width=30, relief=GROOVE, borderwidth=5,font = "Helvetica 15")
value.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+S+N)


def button_click(number):
    value.insert(END, number)


def button_clear():
    value.delete(0, END)



def addition():
    global first_number
    global math
    math = "+"
    try:
        first_number = float(value.get())
    except:
        ValueError
    value.delete(0, END)


def substraction():
    global first_number
    global math
    math = "-"
    try:
        first_number = float(value.get())
    except:
        ValueError
    value.delete(0, END)


def multiply():
    global first_number
    global math
    math = "*"
    try:
        first_number = float(value.get())
    except:
        ValueError
    value.delete(0, END)


def divide():
    global first_number
    global math
    math = "/"
    try:
        first_number = float(value.get())
    except:
        ValueError
    value.delete(0, END)


def equals():
    try:
        second = int(value.get())
    except:
        ValueError
    value.delete(0, END)
    try:
        if math == "+":
            ans=second + first_number
            value.insert(0, ans)
        elif math == "-":
            ans = first_number - second
            value.insert(0, ans)
        elif math == "*":
            ans = second * first_number
            value.insert(0, ans)
        elif math == "/" and second != 0:
            ans = first_number / second
            value.insert(0, ans)
        elif second == 0:
            value.insert(0, "NIE DZIELI SIĘ PRZEZ ZERO MATOLE")

    except:
        NameError



button0 = Button(root, text="0", padx=69, pady=10, command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2,sticky=E+W+S+N)

button1 = Button(root, text="1", padx=30, pady=10, command=lambda: button_click(1)).grid(row=3, column=0,sticky=E+W+S+N)
button2 = Button(root, text="2", padx=30, pady=10, command=lambda: button_click(2)).grid(row=3, column=1,sticky=E+W+S+N)
button3 = Button(root, text="3", padx=30, pady=10, command=lambda: button_click(3)).grid(row=3, column=2,sticky=E+W+S+N)

button4 = Button(root, text="4", padx=30, pady=10, command=lambda: button_click(4)).grid(row=2, column=0,sticky=E+W+S+N)
button5 = Button(root, text="5", padx=30, pady=10, command=lambda: button_click(5)).grid(row=2, column=1,sticky=E+W+S+N)
button6 = Button(root, text="6", padx=30, pady=10, command=lambda: button_click(6)).grid(row=2, column=2,sticky=E+W+S+N)

button7 = Button(root, text="7",  padx=30, pady=10,command=lambda: button_click(7)).grid(row=1, column=0,sticky=E+W+S+N)
button8 = Button(root, text="8",  padx=30,pady=10,command=lambda: button_click(8)).grid(row=1, column=1,sticky=E+W+S+N)
button9 = Button(root, text="9",  padx=30, pady=10,command=lambda: button_click(9)).grid(row=1, column=2,sticky=E+W+S+N)

buttonPlus = Button(root, text="+", padx=29, pady=10, command=addition).grid(row=1, column=3,sticky=E+W+S+N)
buttonMinus = Button(root, text="-", padx=30, pady=10, command=substraction).grid(row=2, column=3,sticky=E+W+S+N)
buttonMultiply = Button(root, text="*", padx=30, pady=10, command=multiply).grid(row=3, column=3,sticky=E+W+S+N)
buttonDivide = Button(root, text="/", padx=30, pady=10, command=divide).grid(row=4, column=3,sticky=E+W+S+N)
buttonEquals = Button(root, text="=", padx=30, pady=10, command=equals).grid(row=4, column=2,sticky=E+W+S+N)
buttonClear = Button(root, text="Clear", padx=20, pady=10, command=button_clear).grid(row=0, column=3,sticky=E+W+S+N)

#Expanding
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.grid_columnconfigure(3,weight=1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)
root.grid_rowconfigure(3,weight=1)




root.mainloop()
