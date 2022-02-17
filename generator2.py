from random import randint, choice, random

import ciag
import matura
import nierownosc
import ułamki
import planimetria

f = open("zadania.doc", 'w', encoding="utf-8")
count = 0


def upraszczanie_wyrazen():
    liczby = []
    litery=["a","b","c","x"]
    for item in range(5):
        if random() > 0.5:
            x = randint(-8, 8)
            if x > 0:
                x = "+" + str(x)
        else:
            x = choice(["+", "-"]) + str(randint(2, 9)) + litery[randint(0,len(litery)-1)]
        liczby.append(x)

    f.write(f'{randint(-9, -3)}')
    for a in range(len(liczby)):
        f.write(f'{liczby[a]}')
    f.write("=\n")


def counter(function):  # counter(nazwafunkcji)
    global count
    count += 1
    print(count, end='. ')
    function()


# ułamki.fraction_change(randint(1, 16) / choice([2, 4, 8]))

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
            matura.wzory_sm()
            matura.wzory_sm()
            matura.logarytm(choice([2, 3, 5]))
            # matura.pierwiastki()
            matura.potegi()
            matura.usuwanie_niewymiernosci()
            matura.procenty()
            matura.procenty()
            matura.rozne()
            matura.rozne()
            matura.ilosc_rozwiazan()
            matura.liniowa_abcd()
            matura.liniowa_abcd()
            nierownosc.kwadratowa()
            ciag.arytmetyczny_zamkniete()
            ciag.geometryczny_zamkniete()
            nierownosc.liniowa()
            planimetria.trojkaty()
            planimetria.czworokaty()
            planimetria.rozne()


        elif cotam == 4:
            for i in range(20):
                upraszczanie_wyrazen()
                # nierownosc.kwadratowa()
                matura.wzory_sm()
                # wzory_vieta()
                # matura.kwadratowa()
                # matura.procenty()
                # matura.pierwiastki()
                # matura.wzory_sm()
                # matura.usuwanie_niewymiernosci()
                # matura.logarytm(choice([2, 3, 5]))
                # matura.liniowa_abcd()
            # matura.liniowa_obrazek()
            # ciag.arytmetyczny_zamkniete()
            # ciag.geometryczny_zamkniete()
        elif cotam == 5:
            for i in range(100):
                #matura.liniowa_otwarte()
                #matura.liniowa_abcd()
                #matura.pierwiastki()
                #matura.usuwanie_niewymiernosci()
                #nierownosc.kwadratowa()
                #matura.logarytm(2)
                #matura.logarytm(3)
                #matura.logarytm(5)
                matura.procenty()



        elif cotam == 0:
            f.close()
            break

    except ValueError:
        print("Enter a number")
