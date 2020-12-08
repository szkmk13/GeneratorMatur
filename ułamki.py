from random import random, randint

f = open("zadania.doc", 'a+', encoding="utf-8")


def dodawanie_ulamkow():
    for j in range(14):
        liczniki = []
        kreski_i_znaki = []
        mianowniki = []
        for i in range(4):  # ilość ułamków w zadaniu
            if random() > 0.4:
                liczniki.append(-1 * randint(1, 5))
            else:
                liczniki.append(randint(1, 5))
            mianowniki.append(randint(2, 8))
            if mianowniki[i] == abs(liczniki[i]):  # mianownik różny od licznika i jego przeciwieństwa
                mianowniki[i] += 1
            if i == 3:
                kreski_i_znaki.append(" - =")
            else:
                kreski_i_znaki.append(" - +")

        for licznik in liczniki:  # wypisywanie liczników

            if licznik < 0:
                f.write(f'{licznik}  ')
            if licznik > 0:
                f.write(f' {licznik}  ')
        f.write("\n")
        for kreska in kreski_i_znaki:
            f.write(kreska)
        f.write("\n")
        for mianownik in mianowniki:
            f.write(f' {mianownik}  ')
        f.write("\n\n")


def skracanie(licznik, mianownik):
    ulamek = 0
    dzielniki = [2, 3, 5, 7, 11, 13]
    ujemne = False
    if licznik * mianownik < 0:
        ujemne = True
    licznik = abs(licznik)
    mianownik = abs(mianownik)
    for dzielnik in dzielniki:
        while licznik % dzielnik == 0 and mianownik % dzielnik == 0:
            licznik = licznik / dzielnik
            mianownik = mianownik / dzielnik

    while licznik > mianownik:  # wyłączanie calosci
        licznik -= mianownik
        ulamek += 1
    if licznik == mianownik:
        return int(ulamek + licznik / mianownik)

    if abs(licznik) == 1 and abs(mianownik) == 3:
        ulamek = str(ulamek) + '.(3)'
    elif abs(licznik) == 2 and abs(mianownik) == 3:
        ulamek = str(ulamek) + '.(6)'
    elif abs(mianownik) == 7:
        ulamek = str(ulamek) + f' {licznik}/7'
    elif abs(mianownik) == 9:
        ulamek = str(ulamek) + f' {licznik}/9'
    else:
        ulamek = ulamek + licznik / mianownik

    if ujemne is True:
        ulamek = "-" + str(ulamek)

    return ulamek
