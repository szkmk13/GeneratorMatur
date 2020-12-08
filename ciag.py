from random import randint, choice

f = open("zadania.doc", 'a+', encoding="utf-8")


def slownie(wyraz):
    if wyraz == 2:
        wyraz = "drugi"
    if wyraz == 3:
        wyraz = "trzeci"
    if wyraz == 4:
        wyraz = "czwarty"
    if wyraz == 5:
        wyraz = "piąty"
    if wyraz == 6:
        wyraz = "szósty"
    if wyraz == 7:
        wyraz = "siódmy"
    if wyraz == 8:
        wyraz = "ósmy"
    if wyraz == 9:
        wyraz = "dzwiewiąty"
    if wyraz == 10:
        wyraz = "dziesiąty"
    if wyraz == 11:
        wyraz = "jedenasty"
    if wyraz == 12:
        wyraz = "dwunasty"
    if wyraz == 13:
        wyraz = "trzynasty"
    if wyraz == 14:
        wyraz = "czternasty"
    if wyraz == 15:
        wyraz = "piętnasty"
    if wyraz == 16:
        wyraz = "szesnasty"
    if wyraz == 17:
        wyraz = "siedemnasty"
    return wyraz + " wyraz"


def suma_n_wyrazow_arytmetyczny(a1, r, n):
    suma = (2 * a1 + (n - 1) * r) / 2 * n
    if suma == int(suma):
        return int(suma)
    else:
        return suma


def suma_n_wyrazow_geometryczny(a1, q, n):
    suma = a1 * (1 - q ** n) / (1 - q)
    if suma == int(suma):
        return int(suma)
    else:
        return suma


def arytmetyczny_zamkniete():
    ktore = randint(0, 4)
    a1 = 0
    r = 0
    n = (randint(8, 12))
    wyraz = 0
    wyraz2 = 0

    while a1 == 0 or r == 0 or wyraz == wyraz2:
        a1 = randint(-10, 10)
        r = randint(-10, 10)
        n = randint(5, 12)
        wyraz = randint(2, n)
        wyraz2 = randint(2, n)
    awyraz = a1 + r * (wyraz - 1)
    awyraz2 = a1 + r * (wyraz2 - 1)

    if ktore == 0:
        f.write(
            f'W ciągu arytmetycznym pierwszy wyraz jest równy {a1}, a {slownie(wyraz)}  jest równy {awyraz}. Oblicz '
            f'{slownie(wyraz2)} \n\n')
    elif ktore == 1:
        f.write(
            f'{slownie(wyraz2)} ciągu arytmetycznego jest równy {awyraz2}, reszta tego ciągu to {r}. Stąd wynika, że {slownie(wyraz)} jest równy ?\n\n')
    elif ktore == 2:
        f.write(
            f'Dany jest ciąg arytmetyczny którego {slownie(wyraz)} to {awyraz}, i {slownie(wyraz + 1)} to {awyraz + r} więc:\n')
        f.write(
            f'A. a{wyraz + 5}={awyraz + 5 * r} B. a{wyraz + 3}={awyraz + 2 * r} C. a{wyraz - 2}={awyraz - 3 * r} D. a{wyraz - 1}={awyraz - r}\n\n')
    elif ktore == 3:
        f.write(
            f'Suma pierwszych {n} wyrazów ciągu arytmetycznego wynosi {suma_n_wyrazow_arytmetyczny(a1, r, n)} . Wiedząc że a1={a1} oblicz r.\n\n')
    elif ktore == 4:
        f.write(
            f'W ciągu arytmetycznym {slownie(wyraz - 1)} to {awyraz - r} , a {slownie(wyraz + 1)} jest równy {awyraz + r} Więc a{wyraz}=\n')
        f.write(f'A. {awyraz + 2 * r} B. {awyraz2 - r} C. {awyraz} D. {awyraz2}\n\n')


def geometryczny_zamkniete():
    ktore = randint(0, 4)
    a1 = 0
    q = 0
    n = (randint(4, 6))

    while a1 == 0 or a1 == 1 or a1 == -1 or suma_n_wyrazow_geometryczny(a1, q, n) % 1 != 0:
        a1 = randint(-6, 6)
        q = choice([2, 3, 4, 0.5, 1.5])
    wyraz = randint(2, n)
    wyraz2 = randint(2, n)
    awyraz = a1 * q ** (wyraz - 1)
    awyraz2 = a1 * q ** (wyraz2 - 1)

    if ktore == 0:
        f.write(
            f'Dany jest ciąg geometryczny którego {slownie(wyraz)} to {awyraz} i a1 = {a1}. Oblicz iloczn tego ciągu\n\n')
    elif ktore == 1:
        f.write(
            f'W ciągu geometrycznym {slownie(wyraz)} to {awyraz} a {slownie(wyraz2)} jest równy {awyraz2} oblicz iloczyn tego ciągu\n\n')
    elif ktore == 2:
        f.write(
            f'W ciągu geometrycznym {slownie(wyraz)} to {awyraz} a {slownie(wyraz2)} jest równy {awyraz2} oblicz pierwszy wyraz tego ciągu\n\n')
    elif ktore == 3:
        f.write(
            f'{suma_n_wyrazow_geometryczny(a1, q, n)} to suma pierwszych {n} wyrazów ciągu geometrycznego w któym a1={a1} oblicz iloczyn tego ciągu\n\n')
    elif ktore == 4:
        f.write(
            f'Ciąg geometryczny, którego {slownie(wyraz)} to {awyraz} , a {slownie(wyraz + 2)} jest równy {awyraz * q * q} ma iloczyn równy \n')
        f.write(f'A. {wyraz2} B. {wyraz} C. {q} D. {a1}\n\n')


def otwarte():
    ktore = randint(0, 4)
    a1 = 0
    r = 0
    n = (randint(8, 12))

    while a1 == 0 or r == 0:
        a1 = randint(-10, 10)
        r = randint(-10, 10)
        n = randint(4, 12)
    wyraz = randint(3, n)
    wyraz2 = randint(3, n)
    awyraz = a1 + r * (wyraz - 1)
    awyraz2 = a1 + r * (wyraz2 - 1)
