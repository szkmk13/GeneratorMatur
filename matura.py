from random import choice, randint, random
import ułamki
import cartesian_plane

f = open("zadania.doc", 'a+', encoding="utf-8")


def number_to_substract(number):
    number = str(number)
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


def procenty():
    f.write(choice([
        f'Cena towaru po obniżce o {randint(1, 5) * 5}% wynosi {randint(2, 12) * 252}zł. Cena przed rabatem to?'
        ,
        f'Cena towaru po podwyżce o {randint(1, 3) * 20}% wynosi {randint(2, 12) * 336}zł. Cena przed podwyżką to?'
        ,
        f'Cena zmniejszono o {randint(1, 3) * 25}%. O ile % trzeba zwiększyć cenę aby wrócić do ceny początkowej?'
        ,
        f'Towar kosztuje {randint(3, 15) * 30}zł jego cena po obniżce o {randint(1, 4) * 5}% wynosi:'
        ,
        f'Towar kosztuje {randint(3, 15) * 30}zł jego cena po podwyżce o {randint(1, 4) * 5}% wynosi:'
        ,
        f'liczba {randint(1, 5) * 10} to ile procent liczby {randint(2, 5) * 100} ?'
    ]))
    f.write("\n\n")


def potegi():
    dzialania = ["*", "*", "*"]
    miejsce_dzielenia = randint(0, len(dzialania))
    dzialania[miejsce_dzielenia] = ":"
    podstawa = randint(2, 11)
    print(dzialania)
    for potega in range(len(dzialania) + 1):
        print(potega)

    for dzialanie in dzialania:
        print(f'{2} + {dzialanie}')

    return


def ilosc_rozwiazan():
    i = 0
    ile_nawiasow_w_liczniku = randint(2, 4)
    nawiasy = []
    while len(nawiasy) < ile_nawiasow_w_liczniku:
        nawiasy.append(randint(1, 4))
    ile = len(nawiasy)
    f.write(f'Ile {choice(["rozwiązań", "pierwiastków"])} ma poniższe równanie:\n')
    while i < ile:
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
    f.write("\nA. 1  B. 2  C. 3  D. 4\n\n")


def wzory_sm():
    wynik = []
    for i in range(2):
        wyrazenie = ''

        liczby = str(randint(2, 6))
        literki = choice(['a', 'b', 'c', 'x', 'y'])
        pierwiastki = "\u221A" + str(choice([2, 3, 5]))
        xdxd = [liczby, literki, pierwiastki]
        mainbranch = randint(0, 2)
        inna = [pierwiastki, literki, '']
        subbranch = randint(0, 2)
        inna2 = [literki, '']
        subbranch2 = randint(0, 1)

        if mainbranch == 0:  # najepirw liczba potem inne rzeczy
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


def liniowa_abcd():
    x1 = 0
    x2 = 0
    x3 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    a1 = 1
    wyraz_wolny = 1
    rowno_czy_prosto = choice(['równoległej', 'prostopadłej'])
    while x1 == 0 or x2 == 0 or y1 == 0 or y2 == 0 or x3 == 0 or y3 == 0 or y1 == y3:
        x1 = randint(-6, 6)
        x2 = randint(-6, 6)
        x3 = randint(-6, 6)
        y1 = randint(-6, 6)
        y2 = randint(-6, 6)
        y3 = randint(-6, 6)
        wyraz_wolny = randint(2, 8)
        if random() > 0.5:
            a1 = randint(2, 5)
        else:
            a1 = randint(-5, -2)

    f.write(choice([
        f'Miejscem zerowym funkcji określonej wzorem f(x)={randint(2, 4)}-(x{choice(["+", "-"])}{randint(1, 8)}){choice(["+", "-"])}*{randint(2, 3)} jest?'
        ,
        f'Miejscem zerowym funkcji określonej wzorem f(x)={randint(2, 4)}(x{choice(["+", "-"])}{randint(1, 8)}){choice(["+", "-"])}{randint(2, 8)} jest?'
        ,
        f'Miejscem zerowym funkcji określonej wzorem f(x)={randint(2, 4)}(x{choice(["+", "-"])}{randint(1, 8)}){choice(["+", "-"])}\u221A{randint(2, 3)} jest?'
        ,
        f'Punkt A=({x1},{y1}) należy do funkcji określonej wzorem f(x)={x2}x+b . Stąd wynika że b=\n'
        f'A. {ułamki.skracanie(-1 * x1 * y1, x2)} B. {y1 + x2 * x1} C. {ułamki.skracanie(x2 * y1, x1)} D. {y1 - x2 * x1}'
        ,
        f'Dla jakiego m podane punkty są współliniowe? A({x1},{y1}) B({x2}-{randint(2, 4)}m,{y2}) C({x3},{y3})'
        ,
        f'Wyznacz równanie prostej przechodzącej przez punkt E({x1},{y1}) i {rowno_czy_prosto} do prostej y={a1}x+{wyraz_wolny}\n'
        f'A. y={a1}x+{-1 * (x1 * a1 - y1)}  B. y={a1}x+{x1 * a1 - y1}  C. y={ułamki.skracanie(-1, a1)}x+{ułamki.skracanie(y1 * a1 + x1, a1)}  D. y={ułamki.skracanie(-1, a1)}x+{ułamki.skracanie(y1 * a1 - x1, a1)}  '
        ,
        f'Dla jakiej wartości parametru m punkt M({x1},{y1}-m) należy do wykresu funkcji liniowej y={x2}x{choice(["+" + str(wyraz_wolny), "-" + str(wyraz_wolny)])}\n'
        f'A. m= {y1 + x2 * x1 - wyraz_wolny} B. m= {y1 - x2 * x1 + wyraz_wolny} C. m= {y1 - x2 * x1 - wyraz_wolny} D. m= {y1 + x2 * x1 + wyraz_wolny} '
        ,
        f'Dla jakiej wartości parametru m funkcja liniowa y=({a1}{choice(["+", "-"])}{wyraz_wolny}m)x+{x1} jest {choice(["rosnąca", "malejąca"])}?\n'
        f'A. m>{ułamki.skracanie(a1, -1 * wyraz_wolny)} B. m>{ułamki.skracanie(a1, wyraz_wolny)}  C. m<{ułamki.skracanie(a1, wyraz_wolny)}  D. m<{ułamki.skracanie(a1, -1 * wyraz_wolny)} '
        ,
        f'Prosta przechodzi przez punkt A({x1},{x2}) oraz przez punkt D({y1},{y2}) jej {choice(["współczynnik kierunkowy", "wyraz wolny"])} wynosi?\n'
        ,
        f'Proste o równaniach {x1}x+{y1}'

    ]))
    f.write('\n\n')


def liniowa_obrazek():
    f.write(f'{choice(["współczynnik kierunkowy", "wyraz wolny"])} pokazanej na rysunku wynosi:')
    cartesian_plane.linear_function()


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

    f.write(choice([
        f'Jaką wartość ma funkcja f(x)={wzor_funkcji} dla argumentu równego {randint(-5, 5)} ?',
        f'Określ monotoniczność funkcji f(x)={wzor_funkcji}',
        f'Podaj zbiór wartości funkcji f(x)={wzor_funkcji}',
        f'Dla jakiej wartości parametru m punkt A=({randint(-5, 5)},{randint(1, 5)}-m) należy do wyrkesu funkcji f(x)={wzor_funkcji}',
        f'Podaj wzór funkcji f(x)={wzor_funkcji} w postaci iloczynowej',
        f'Podaj wzór funkcji f(x)={wzor_funkcji} w postaci kanonicznej',
        f'Oblicz współrzędne wierzchołka paraboli określonej wzorem f(x)={wzor_funkcji}',
        f'Funkcja o wzorze f(x)={wzor_funkcji} przecina oś OY w punkcie',
        f'Oś symetrii funkcji f(x)={wzor_funkcji} to?',
        f'Ile miejsc zerowych ma funkcja określona wzorem f(x)={wzor_funkcji}'

    ]))
    f.write('\n\n')


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

    f.write(choice([
        f'Dane są dwie liczby a = {a}*10^{potega1} i b = {b}*10^{potega2} {polecenie} tych liczb to?\n'
        f'A={a * b}*10^{potega1 + potega2 + 2} B={a * b / 10000}*10^{potega1 + potega2 + 4}  C={a / b * 10}*10^{potega1 - potega2 + 2} D={a / b}*10^{potega1 - potega2}'
        ,
        f'Zaokrąglenie liczby {q} do {miejsce} to :'
        ,
        f'Oblicz {mediana_czy_srednia} zestawu liczb: {liczby} . '
        ,
        f'Ile jest liczb {ilu_cyfrowa} cyfrowych podzielnych przez {podzielnosc_przez}'
        ,
        f'Wszystkich liczb {ilu_cyfrowa} cyfrowych w których występują tylko {jakie_cyfry} jest?'

    ]))
    f.write('\n\n')


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
