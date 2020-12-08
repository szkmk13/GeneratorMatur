from random import randint, choice

import ciag
import matura
import nierownosc
import ułamki
import planimetria


def wypisanie_liczb():
    print(f"losowa liczba to: {randint(2,93)}")
    ux = 0
    uy = 0
    a = 0
    while ux == 0 or uy == 0 or a == 0:
        ux = randint(-4, 4)
        uy = randint(-4, 4)
        a = randint(-4, 4)

    symetria = choice(['osi OY', 'osi OX', 'początku układu współrzędnych'])

    f.write(f'1. napisz wzory funkcji których wykresy otrzymamy jeżeli:\n')
    f.write(f"a) wykres funkcji {choice(['', '-'])}{randint(2, 4)}/x przesuniemy o wektor u= [{ux},{uy}]")
    f.write(f' a następnie przekształcimy przez symetrię względem {symetria}\n\n')
    symetria = choice(['osi OY', 'osi OX', 'początku układu współrzędnych'])
    f.write(
        f'b) wykres fukncji f(x)= {a}x\u00b2{choice(["+", "-"])}{randint(2, 5)}x przekształcimy przez symetrię względem {symetria}\n\n ')
    f.write(
        f"2a. Narysuj wykres funkcji f(x)= -(|x|{randint(1, 4)})\u00b2. Wyznacz miejsca zerowe oraz podaj jej przedziały monotoniczności.\n\n")
    f.write(
        f"2b. Narysuj wykres funkcji f(x)= (|x|{choice(['+', '-'])}{randint(1, 4)})\u00b2 - {randint(1, 4)}. Wyznacz miejsca zerowe oraz podaj jej przedziały monotoniczności.\n\n")
    f.write(
        f"3. Narysuj wykres funkcji f(x)=|{randint(2, 5)}-|x{choice(['+', '-'])}{randint(2, 5)}|| i podaj jej zbiór wartości\n\n")


class Counter:
    count=0
    def __init__(self):
        self.count += 1
        print(self.count)

count = 0
def Counter(function):
    globals()['count'] += 1
    print(count,end='')
    function()



f = open("zadania.doc", 'w', encoding="utf-8")

while True:
    print("""
    1. Dodawanie ułamków (pełne strony)
    2. Funkcja
    3. Matura
    4.testownie
    """)
   # print(ułamki.skracanie(8, 4))
    cotam = int(input("Wybierz: "))

    if cotam == 1:
        ułamki.dodawanie_ulamkow()
    elif cotam == 2:
        Counter(wypisanie_liczb)
        Counter(wypisanie_liczb)
        Counter(wypisanie_liczb)
    elif cotam == 3:
        #f.write('Zadania otwarte:\n')
        matura.logarytm(choice([2, 3, 5]))
        matura.pierwiastki()
        matura.usuwanie_niewymiernosci()
        matura.procenty()
        matura.procenty()
        matura.zadanie_z_2_liczbami()
        matura.ilosc_rozwiazan()
        matura.liniowa()
        matura.liniowa()
        nierownosc.kwadratowa()
        ciag.arytmetyczny_zamkniete()
        ciag.geometryczny_zamkniete()
        nierownosc.liniowa()
        nierownosc.z_wartoscia_bezwzledna()
        planimetria.trojkaty()


    elif cotam == 4:
        for i in range(10):
            planimetria.czworokaty()
    elif cotam == 0:
        f.close()
        break
