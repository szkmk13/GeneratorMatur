from random import randint, choice, random

import ciag
import matura
import nierownosc
import ułamki
import planimetria

f = open("zadania.doc", 'w', encoding="utf-8")



def upraszczanie_wyrazen():
    print(f'x -3x +8x -x = ')


def test_funkcja():
    while True:
        a = randint(-15, 15)
        b = randint(-115, 115)
        c = randint(-115, 115)
        delta = b * b - 4 * a * c
        if (delta in [0, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]) and (a == 1) and b != 0 and c!= 0:
            break

    wzor_funkcji = f' x\u00b2'
    if b != 0:
        if b > 0:
            wzor_funkcji += f'+{b}x'
        else:
            wzor_funkcji += f'{b}x'
    if c != 0:
        if c > 0:
            wzor_funkcji += f'+{c}'
        else:
            wzor_funkcji += f'{c}'
    f.write(wzor_funkcji)
    f.write("\n")

count = 0


def counter(function):  # counter(nazwafunkcji)
    global count
    count += 1
    print(count, end='. ')
    function()



matura.potegi()
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
            matura.liniowa_abcd()
            matura.liniowa_abcd()
            nierownosc.kwadratowa()
            ciag.arytmetyczny_zamkniete()
            ciag.geometryczny_zamkniete()
            nierownosc.liniowa()
            nierownosc.z_wartoscia_bezwzledna()
            planimetria.trojkaty()
            planimetria.czworokaty()
            planimetria.rozne()


        elif cotam == 4:
            for i in range(25):
                # matura.procenty()
                # matura.pierwiastki()4

                # matura.usuwanie_niewymiernosci()
                matura.logarytm(choice([2, 3, 5]))

                #matura.liniowa_obrazek()
        elif cotam == 5:
            for i in range(100):
                matura.liniowa_otwarte()
                matura.liniowa_abcd()
                matura.pierwiastki()
                matura.usuwanie_niewymiernosci()
                matura.logarytm(2)
                matura.logarytm(3)
                matura.logarytm(5)



        elif cotam == 0:
            f.close()
            break

    except ValueError:
        print("Enter a number")
