import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from random import choice, randint, random
f = open("ZadaniaAplikacja.doc", 'w', encoding="utf-8")

widgets = {
    "logo": [],
    "button1": [],
    "button2": [],
    "button3": [],
    "button4": [],
    "button5": [],
    "button6": [],
    "button7": [],
    "button8": [],

}
buttonstyle = ("*{border: 4px solid black;" +
               "border-radius:10px; " +
               "font-size: 35px;" +
               "margin: 20px 0;}" +
               "*:hover{background: white}")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Generator Matur")
window.setFixedWidth(1000)
window.setStyleSheet("background: #C3B6F5;")

grid = QGridLayout()
ileprzykladow = 1
def pierwiastki():
    for i in range(ileprzykladow):
        ile_pierwiastkow = 4
        pierwiastki = []
        znaki = []
        for i in range(ile_pierwiastkow):
            if random() > 0.9:
                pierwiastki.append(f"{randint(2, 5)}")
            if random() > 0.7:
                pierwiastki.append(f"{randint(2, 5)}\u221A{choice([2, 3, 5])}")
            else:
                pierwiastki.append(f'\u221A{choice([2, 3, 5]) * randint(2, 5) ** 2}')
            if i == ile_pierwiastkow - 1:
                znaki.append("=")
            else:
                znaki.append(choice(["+", "-", "*", ":"]))
        for i in range(ile_pierwiastkow):
            f.write(f'{pierwiastki[i]} {znaki[i]} ')
        f.write("\n\n")

def clicked():
    print("Ads")


def create_button(name, row, col, rowspan, colspan, function):
    button = QPushButton(name)
    button.setStyleSheet(buttonstyle)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    grid.addWidget(button, row, col, rowspan, colspan)
    button.clicked.connect(function)
    return button
def frame1():
    # title
    title = QLabel("2. Z którego działu")
    title.setAlignment(QtCore.Qt.AlignCenter)
    title.setStyleSheet("font-size:32px")
    grid.addWidget(title,0,0,1,2)
    # buttons
    button1 = create_button("pierwiastki", 1, 0, 1, 1,pierwiastki)
    button2 = create_button("kwadratowa", 1, 1, 1, 1,clicked)
    button3 = create_button("q", 2, 0, 1, 1,clicked)
    button4 = create_button("w", 2, 1, 1, 1,clicked)
    button5 = create_button("e", 3, 0, 1, 1,clicked)
    button6 = create_button("r", 3, 1, 1, 1,clicked)
    button7 = create_button("t", 4, 0, 1, 1,clicked)
    button8 = create_button("y", 4, 1, 1, 1,clicked)

    widgets["logo"].append(title)
    widgets["button1"].append(button1)
    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)

def frame2():
    x=1
    def adjust(x):
        if x==20:
            x=20
        elif x==10:
            x=10
        else: x=5
        print(x)
        global ileprzykladow
        ileprzykladow = x
        print(ileprzykladow)
        return ileprzykladow

    tasks = QLabel("1. Wybierz ile przykładów")
    tasks.setStyleSheet("font-size:40px")
    tasks.setAlignment(QtCore.Qt.AlignCenter)
    grid.addWidget(tasks,0,2,1,3)

    b1 = QPushButton("5")
    b1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    b1.clicked.connect(lambda: adjust(5))
    b2 = QPushButton("10")
    b2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    b2.clicked.connect(lambda: adjust(10))
    b3 = QPushButton("20")
    b3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    b3.clicked.connect(lambda: adjust(20))

    quitprograme = QPushButton("zapisz i wyjdź")
    quitprograme.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    quitprograme.clicked.connect(lambda: f.close())
    quitprograme.clicked.connect(lambda: quit())

    grid.addWidget(b1, 1, 2, 1, 1)
    grid.addWidget(b2, 1, 3, 1, 1)
    grid.addWidget(b3, 1, 4, 1, 1)
    grid.addWidget(quitprograme,5,4)





frame1()
frame2()
window.setLayout(grid)
window.show()
sys.exit(app.exec())
