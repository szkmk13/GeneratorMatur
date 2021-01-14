from random import randint, choice, random

import ciag
import matura
import nierownosc
import ułamki
import planimetria





def upraszczanie_wyrazen():
    print(f'x -3x +8x -x = ')


def test_funkcja():
    print(f"losowa liczba to: {randint(2, 93)}")


count = 0


def counter(function):  # counter(nazwafunkcji)
    global count
    count += 1
    print(count, end='. ')
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
    try:
        cotam = int(input("Wybierz: "))

        if cotam == 1:
            ułamki.dodawanie_ulamkow()
        elif cotam == 2:
            matura.pierwiastki()
            matura.usuwanie_niewymiernosci()
            matura.procenty()
            matura.rozne()
            matura.rozne()
            nierownosc.liniowa()
            matura.logarytm(2)
            matura.logarytm(3)
            matura.logarytm(5)
        elif cotam == 3:
            # f.write('Zadania otwarte:\n')
            matura.logarytm(choice([2, 3, 5]))
            matura.pierwiastki()
            matura.usuwanie_niewymiernosci()
            matura.procenty()
            matura.procenty()
            matura.rozne()
            matura.ilosc_rozwiazan()
            matura.liniowa()
            matura.liniowa()
            nierownosc.kwadratowa()
            ciag.arytmetyczny_zamkniete()
            ciag.geometryczny_zamkniete()
            nierownosc.liniowa()
            nierownosc.z_wartoscia_bezwzledna()
            planimetria.trojkaty()
            planimetria.czworokaty()
            planimetria.rozne()


        elif cotam == 4:
            for i in range(15):
                # matura.procenty()
                # matura.pierwiastki()
                # matura.usuwanie_niewymiernosci()
                matura.logarytm(choice([2, 3, 5]))
                matura.logarytm(choice([2, 3, 5]))


        elif cotam == 0:
            f.close()
            break

    except ValueError:
        print("Enter a number")
