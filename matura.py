from random import choice, randint, random
import ułamki

# import cartesian_plane


f = open("zadania.doc", 'a+', encoding="utf-8")


def number_to_substract(number):
    number = str(number)
    unicode_substract_offset = 2080
    subscript = ''
    for character in number:

        if character == '.':
            subscript += '\u0323 '
        if character == "0":
            subscript += '\u2080'
        if character == "1":
            subscript += '\u2081'
        if character == "2":
            subscript += '\u2082'
        if character == "3":
            subscript += '\u2083'
        if character == "4":
            subscript += '\u2084'
        if character == "5":
            subscript += '\u2085'
        if character == "6":
            subscript += '\u2086'
        if character == "7":
            subscript += '\u2087'
        if character == "8":
            subscript += '\u2088'
        if character == "9":
            subscript += '\u2089'
    return subscript


def number_to_superscript(number):
    number = str(number)
    superscript = ''
    for character in number:
        if character == '.':
            superscript += '\u0307 '
        if character == "0":
            superscript += '\u2070'
        if character == "1":
            superscript += '\u00b9'
        if character == "2":
            superscript += '\u00b2'
        if character == "3":
            superscript += '\u00b3'
        if character == "4":
            superscript += '\u2074'
        if character == "5":
            superscript += '\u2075'
        if character == "6":
            superscript += '\u2076'
        if character == "7":
            superscript += '\u2077'
        if character == "8":
            superscript += '\u2078'
        if character == "9":
            superscript += '\u2079'
        if character == "-":
            superscript += '\u207B'
    return superscript


def wzory_vieta():
    while True:
        a = randint(-15, 15)
        b = randint(-115, 115)
        c = randint(-115, 115)
        delta = b * b - 4 * a * c
        if (delta in [0, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]) and (
                a != 0) and b != 0 and c != 0:
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


def logarytm(podstawa):
    if random() > 0.4:
        pods = 1
        liczbalog = 1
        potega1 = ''
        pierwiastek = ''

        while pods == liczbalog:
            if podstawa == 2:
                pods = choice([4, 8, 0.5, 0.25, 0.125, 32, 64, 128])
                liczbalog = choice([4, 8, 0.5, 0.25, 0.125, 32, 64, 128])
            elif podstawa == 3:
                pods = choice([9, 27, 81, 243])
                liczbalog = choice([9, 27, 81, 243])
            elif podstawa == 5:
                pods = choice([0.2, 0.04, 5, 25, 125, 625])
                liczbalog = choice([0.2, 0.04, 5, 25, 125, 625])
        while potega1 == pierwiastek or (potega1 == '\u00b2' and pierwiastek == '\u221A') or (
                potega1 == '\u00b3' and pierwiastek == '\u221B') or (potega1 == '\u2074' and pierwiastek == '\u221C'):
            potega1 = choice(['', '\u00b2', '\u00b3', '\u2074'])
            pierwiastek = choice(['', '\u221A', '\u221B', '\u221C'])
            f.write(
                f'Wartość wyrażenia: log{number_to_substract(pods)} {pierwiastek}{liczbalog}{potega1} jest równa?\n\n')
    else:
        liczba_log1 = 1
        liczba_log2 = 1
        liczba_log3 = 1
        wynik = [podstawa, podstawa ** 2, podstawa ** 3, podstawa ** 4, podstawa ** 5]
        while liczba_log1 * liczba_log2 not in wynik or liczba_log1 in wynik or liczba_log2 in wynik:
            liczba_log1 = choice([2, 4, 5, 8, 10]) * choice([1, 2, 4, 5, 8, 10])
            liczba_log2 = choice(wynik) * podstawa / liczba_log1
            liczba_log3 = choice(wynik) * podstawa * liczba_log1

        f.write(choice([
            f'log{number_to_substract(podstawa)} {liczba_log1} + log{number_to_substract(podstawa)} {liczba_log2} =',
            f'log{number_to_substract(podstawa)} {liczba_log3} - log{number_to_substract(podstawa)} {liczba_log1} ='
        ]))
        f.write(f'\n\n')


def pierwiastki():
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


def usuwanie_niewymiernosci():
    a = randint(2, 6)
    pierw = choice([2, 3, 5])
    if random() > 0.5:
        a = a * -1
    if random() > 0.6:
        f.write(f'{a}{choice(["+", "-"])}{randint(2, 6)}\u221A{pierw} \n')
        f.write("------ =\n")
        f.write(f'  \u221A{pierw}\n\n')
    else:
        f.write(f'{a}{choice(["+", "-"])}{randint(2, 6)}\u221A{pierw} \n')
        f.write("------ =\n")
        f.write(f' {randint(2, 6)}{choice(["+", "-"])}\u221A{pierw} \n\n')


procenty_variant = [1, 2, 3, 4, 5, 6]


def procenty():
    exercises = {
        1: f'Cena towaru po obniżce o {randint(1, 5) * 5}% wynosi {randint(2, 12) * 252}zł. Cena przed rabatem to?',
        2: f'Cena towaru po podwyżce o {randint(1, 3) * 20}% wynosi {randint(2, 12) * 336}zł. Cena przed podwyżką to?',
        3: f'Cena zmniejszono o {randint(1, 3) * 25}%. O ile % trzeba zwiększyć cenę aby wrócić do ceny początkowej?',
        4: f'Towar kosztuje {randint(3, 15) * 30}zł jego cena po obniżce o {randint(1, 6) * 5}% wynosi:',
        5: f'Towar kosztuje {randint(3, 15) * 30}zł jego cena po podwyżce o {randint(1, 6) * 5}% wynosi:',
        6: f'liczba {randint(1, 5) * 10} to ile procent liczby {randint(2, 5) * 100} ?'
    }
    try:
        a = choice(procenty_variant)
        f.write(exercises[a] + '\n\n')
        #procenty_variant.remove(a)
    except:
        IndexError


def potegi():
    liczba_potegowana = randint(2, 11)
    dzialania = []
    for a in range(4):
        a = choice(["*", ":"])
        dzialania.append(a)
    miejsce_kreski = randint(0, len(dzialania) - 1)  # ( 0 , 3 )
    dzialania[miejsce_kreski] = "-"
    podstawy = [1, 0, 1, 0, 1, 0, 1, 0, 1]
    k = 0
    for n, liczba in enumerate(podstawy):
        if liczba == 0:
            podstawy[n] = dzialania[k]
            k += 1
        elif liczba == 1:
            podstawy[n] = choice([-4, -3, -2, -1, -0.5, -1.5, -2.5, 2, 3, 4, 5, 2, 5, 0.5, 1.5])
    for a, potega in enumerate(podstawy):
        if potega == "*":
            f.write(" * ")
        elif potega == ":":
            f.write(" : ")
        elif potega == "-":
            f.write("\n")
            if a > 3:
                f.write("---" * a)
                f.write(" =\n")
            else:
                f.write("---" * (len(podstawy) - a))
                f.write(" =\n")
        else:
            f.write(str(liczba_potegowana))
            f.write(str(number_to_superscript(potega)))
    f.write("\n\n")

    return


def ilosc_rozwiazan():
    i = 0
    ile_nawiasow_w_liczniku = randint(2, 4)
    nawiasy = []
    while len(nawiasy) < ile_nawiasow_w_liczniku:
        nawiasy.append(randint(1, 9))
    ile = len(nawiasy)
    f.write(
        f'{choice(["Ilość", "Suma", "Iloczyn"])} {choice(["rozwiązań", "pierwiastków", "miejsc zerowych"])} poniższego równania to:\n')
    while i < ile:
        if random() > 0.5:
            f.write(f'(x{choice(["-", "+"])}{nawiasy[i]})\u00b2')
        else:
            f.write(f'(x{choice(["-", "+"])}{nawiasy[i]})')
        i += 1
    f.write("\n")
    while i < 2 * ile:
        if i == 2 * ile - 1:
            f.write("----- = 0")
        else:
            f.write("-----")
        i += 1
    f.write("\n")
    while i < 3 * ile - 1:
        f.write(f' (x{choice(["-", "+"])}{nawiasy[i - ile * 2]}) ')
        i += 1
    f.write("\n")


def wzory_sm():
    wynik = []
    for i in range(2):
        wyrazenie = ''

        liczby = str(randint(1, 7))
        literki = choice(['a', 'b', 'c', 'd', 'e', 'x', 'y', 'z'])
        pierwiastki = "\u221A" + str(choice([2, 3, 5, 6, 8, 12, 18, 24]))
        mainbranch = randint(0, 2)
        subbranch = randint(0, 2)
        subbranch2 = randint(0, 1)

        if mainbranch == 0:  # najpierw liczba potem inne rzeczy
            wyrazenie += liczby
            if subbranch == 0:
                wyrazenie += pierwiastki
                if subbranch2 == 0:
                    wyrazenie += literki
                    # print(" liczba piewiastek litera")
            elif subbranch == 1:
                wyrazenie += literki
                # print(" liczba litera")

        elif mainbranch == 1:  # napierw peirwiastek potem inne
            wyrazenie += pierwiastki
            if subbranch2 == 0:
                wyrazenie += literki
                # print(" piewiastek litera")

        elif mainbranch == 2:
            wyrazenie += literki
            # print("litera")

        # print(wyrazenie)
        wynik.append(wyrazenie)

    f.write(f'({wynik[0]}{choice(["+", "-"])}{wynik[1]})\u00b2 = \n\n')


liniowa_variant = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def liniowa_abcd():
    def zmiana(x):
        if x > 0:
            x = "+" + str(x)
        elif x < 0:
            x = str(x)
        return x

    liczby = []
    for item in range(10):
        x = randint(-8, 8)
        while x == 0 or x in liczby:
            x = randint(-8, 8)
        liczby.append(x)

    liczby_plus_minus = list(map(zmiana, liczby))
    rowno_czy_prosto = choice(['równoległej', 'prostopadłej'])

    exercises = {
        1: f'Miejscem zerowym funkcji określonej wzorem f(x)={liczby[1]}-(x{liczby_plus_minus[8]}){liczby_plus_minus[9]} jest?'
        ,
        2: f'Miejscem zerowym funkcji określonej wzorem f(x)={liczby[1]}(x{liczby_plus_minus[8]}){liczby_plus_minus[9]} jest?'
        ,
        3: f'Miejscem zerowym funkcji określonej wzorem f(x)={liczby[1]}(x{liczby_plus_minus[8]}){liczby_plus_minus[9]}\u221A{randint(2, 3)} jest?'
        ,
        4: f'Punkt A=({liczby[0]},{liczby[1]}) należy do funkcji określonej wzorem f(x)={liczby[3]}x+b . Stąd wynika że b=?'
        ,
        5: f'Dla jakiego m podane punkty są współliniowe? A({liczby[0]},{liczby[1]}) B({liczby[2]}{liczby_plus_minus[9]}m,{liczby[3]}) C({liczby[4]},{liczby[5]})'
        ,
        6: f'Wyznacz równanie prostej przechodzącej przez punkt E({liczby[0]},{liczby[1]}) i {rowno_czy_prosto} do prostej y={liczby[2]}x{liczby_plus_minus[8]}'
        ,
        7: f'Dla jakiej wartości parametru m punkt M({liczby[0]},{liczby[1]}{liczby_plus_minus[7]}m) należy do wykresu funkcji liniowej y={liczby[8]}x{liczby_plus_minus[9]}'
        ,
        8: f'Dla jakiej wartości parametru m funkcja liniowa y=({liczby[0]}{liczby_plus_minus[8]}m)x{liczby_plus_minus[9]} jest {choice(["rosnąca", "malejąca"])}?'
        ,
        9: f'Prosta przechodzi przez punkt A({liczby[0]},{liczby[1]}) oraz przez punkt D({liczby[2]},{liczby[3]}) jej {choice(["współczynnik kierunkowy", "wyraz wolny"])} wynosi?'
        ,
        10: f'Proste o równaniach y={liczby[0]}x{liczby_plus_minus[7]} oraz y=({liczby[0]}{liczby_plus_minus[8]}m)x{liczby_plus_minus[9]} są {choice(["równoległe", "prostopadłe"])} dla m= '
        ,
        11: f'Wiadomo, że f({liczby[0]})={liczby[1]} oraz że f(x)={liczby[2]}x{liczby_plus_minus[9]}b, oblicz b.'
        ,
        12: f'Oblicz wartość funkcji f(x)={liczby[0]}x{liczby_plus_minus[9]} dla argumentu równego {liczby[1] * 2}'
    }
    try:
        a = choice(liniowa_variant)
        f.write(exercises[a] + '\n\n')
        liniowa_variant.remove(a)
    except:
        IndexError


def liniowa_obrazek():
    f.write(f'{choice(["współczynnik kierunkowy", "wyraz wolny"])} pokazanej na rysunku wynosi:')
    cartesian_plane.linear_function()


kwadratowa_variant = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def kwadratowa():
    while True:
        a = randint(-5, 5)
        b = randint(-15, 15)
        c = randint(-15, 15)
        delta = b * b - 4 * a * c
        if (delta in [0, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]) and (a not in [-1, 0, 1]):
            break

    wzor_funkcji = f' {a}x\u00b2'
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
    print(wzor_funkcji)

    exercises = {
        1: f'Jaką wartość ma funkcja f(x)={wzor_funkcji} dla argumentu równego {randint(-5, 5)} ?',
        2: f'Określ monotoniczność funkcji f(x)={wzor_funkcji}',
        3: f'Podaj zbiór wartości funkcji f(x)={wzor_funkcji}',
        4: f'Dla jakiej wartości parametru m punkt A=({randint(-5, 5)},{randint(1, 5)}-m) należy do wyrkesu funkcji f(x)={wzor_funkcji}',
        5: f'Podaj wzór funkcji f(x)={wzor_funkcji} w postaci iloczynowej',
        6: f'Podaj wzór funkcji f(x)={wzor_funkcji} w postaci kanonicznej',
        7: f'Oblicz współrzędne wierzchołka paraboli określonej wzorem f(x)={wzor_funkcji}',
        8: f'Funkcja o wzorze f(x)={wzor_funkcji} przecina oś OY w punkcie',
        9: f'Oś symetrii funkcji f(x)={wzor_funkcji} to?',
        10: f'Ile miejsc zerowych ma funkcja określona wzorem f(x)={wzor_funkcji}'
    }
    try:
        a = choice(kwadratowa_variant)
        f.write(exercises[a] + '\n\n')
        kwadratowa_variant.remove(a)
    except:
        IndexError


rozne_variant = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def rozne():
    # zaokraglanie liczb
    q = round(random() * 1000, 4)
    miejsce = choice(['setek', 'dziesiątek', 'jedności', 'części dziesiątych', 'części setnych', 'części tysięcznych'])

    # zadanie z 2 liczbami
    if random() > 0.5:
        polecenie = 'iloczyn'
    else:
        polecenie = 'iloraz'
    a = randint(3, 7) * 48
    b = randint(3, 6) * 32
    potega1 = randint(12, 16)
    potega2 = randint(8, 11)
    # średnia lub mediana
    ile_liczb = randint(3, 6)
    liczby = []
    mediana_czy_srednia = choice(['medianę', 'średnią'])
    for liczba in range(ile_liczb):
        liczby.append(randint(-4, 5))
    # podzielnosc
    ilu_cyfrowa = randint(2, 5)
    podzielnosc_przez = choice([2, 5, 10])
    # ile liczb z danych cyfr
    ile_cyfr = randint(2, 4)
    jakie_cyfry = []
    while len(jakie_cyfry) != ile_cyfr:
        jaka_cyfra = randint(0, 9)
        if jaka_cyfra not in jakie_cyfry:
            jakie_cyfry.append(jaka_cyfra)

    exercises = {
        1: f'Dane są dwie liczby a = {a}*10^{potega1} i b = {b}*10^{potega2} {polecenie} tych liczb to?\n',
        2: f'A={a * b}*10^{potega1 + potega2 + 2} B={a * b / 10000}*10^{potega1 + potega2 + 4}  C={a / b * 10}*10^{potega1 - potega2 + 2} D={a / b}*10^{potega1 - potega2}'
        ,
        3: f'Zaokrąglenie liczby {q} do {miejsce} to :'
        ,
        4: f'Oblicz {mediana_czy_srednia} zestawu liczb: {liczby} . '
        ,
        5: f'Ile jest liczb {ilu_cyfrowa} cyfrowych podzielnych przez {podzielnosc_przez}'
        ,
        6: f'Wszystkich liczb {ilu_cyfrowa} cyfrowych w których występują tylko {jakie_cyfry} jest?'

    }
    try:
        a = choice(rozne_variant)
        f.write(exercises[a] + '\n\n')
        rozne_variant.remove(a)
    except:
        IndexError


def liniowa_otwarte():
    # a1, a2, a3, b1, b2, b3 = 0
    a1 = 0
    a2 = 0
    a3 = 0


# print(a1,a2,a3,b1,b2,b3)


def arkusz():
    logarytm(choice([2, 3, 5]))
    pierwiastki()
    usuwanie_niewymiernosci()
    ilosc_rozwiazan()
    liniowa_abcd()
    liniowa_abcd()
    kwadratowa()
    kwadratowa()
