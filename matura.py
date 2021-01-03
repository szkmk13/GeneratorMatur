from random import choice, randint, random
import ułamki

f = open("zadania.doc", 'a+', encoding="utf-8")


def logarytm(podstawa):
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
    f.write(f'Wartość wyrażenia: log{pods} {pierwiastek}{liczbalog}{potega1} jest równa?\n\n')


def pierwiastki():
    ile_pierwiastkow = 5
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
    pierw = randint(2, 4)
    if random() > 0.6:
        if random() > 0.5:
            a = a * -1
        f.write(f'{a}{choice(["+", "-"])}{randint(2, 6)}\u221A{pierw} \n')
        f.write("------ =\n")
        f.write(f'  \u221A{pierw}\n\n')
    else:
        if random() > 0.5:
            a = a * -1
        f.write(f'{a}{choice(["+", "-"])}{randint(2, 6)}\u221A{pierw} \n')
        f.write("------ =\n")
        f.write(f' {randint(2, 6)}{choice(["+", "-"])}\u221A{pierw} \n\n')


def procenty():
    choice([f.write(
        f'Cena towaru po obniżce o {randint(1, 5) * 5}% wynosi {randint(2, 12) * 252}zł. Cena przed rabatem to?\n\n')
        , f.write(
            f'Cena towaru po podwyżce o {randint(1, 3) * 20}% wynosi {randint(2, 12) * 336}zł. Cena przed podwyżką to?\n\n')
        , f.write(
            f'Cena zmniejszono o {randint(1, 3) * 25}%. O ile % trzeba zwiększyć cenę aby wrócić do ceny początkowej?\n\n')
        , f.write(f'Towar kosztuje {randint(3, 15) * 30}zł jego cena po obniżce o {randint(1, 4) * 5}% wynosi:\n\n')
        , f.write(f'Towar kosztuje {randint(3, 15) * 30}zł jego cena po podwyżce o {randint(1, 4) * 5}% wynosi:\n\n')
        , f.write(f'liczba {randint(1, 5) * 10} to ile procent liczby {randint(2, 5) * 100} ?\n\n')
    ])


def ilosc_rozwiazan():
    i = 0
    ile_nawiasow_w_liczniku = randint(2, 4)
    nawiasy = []
    while len(nawiasy) < ile_nawiasow_w_liczniku:
        nawiasy.append(randint(1, 4))
    ile = len(nawiasy)
    f.write('Ile rozwiązań ma poniższe równanie:\n')
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
        f.write(f'  (x{choice(["-", "+"])}{nawiasy[i - ile * 2]})')
        i += 1
    f.write("\nA. 1  B. 2  C. 3  D. 4\n\n")


def liniowa():
    x1 = 0
    x2 = 0
    x3 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    a1 = 1
    wyraz_wolny = 1
    wersja = randint(0, 4)
    rowno_czy_prosto = choice(['równoległej', 'prostopadłej'])
    while (x1 == 0 or x2 == 0 or y1 == 0 or y2 == 0 or x3 == 0 or y3 == 0):
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
    if wersja == 0:
        f.write(
            f'Miejscem zerowym funkcji określonej wzorem f(x)={randint(2, 4)}(x{choice(["+", "-"])}{randint(1, 8)}){choice(["+", "-"])}\u221A{randint(2, 3)} jest?\n\n')
    if wersja == 1:
        f.write(
            f'Punkt A=({x1},{y1}) należy do funkcji określonej wzorem f(x)={x2}x+b . Stąd wynika że b=\n')
        f.write(
            f'A. {ułamki.skracanie(-1 * x1 * y1, x2)} B. {y1 - x2 * x1} C. {ułamki.skracanie(x2 * y1, x1)} D. {y1 - x2 * x1}\n\n')
    if wersja == 2:
        f.write(f'Dla jakiego m podane punkty są współliniowe? A({x1},{y1}) B({x2}-m,{y2}) C({x3},{y3})\n\n')
    if wersja == 3:
        f.write(
            f'Wyznacz równanie prsotej przechodządzej przez punkt E({x1},{y1}) i {rowno_czy_prosto} do prostej y={a1}x+{wyraz_wolny}\n'
            f'A. y={a1}x+{-1 * (x1 * a1 - y1)}  B. y={a1}x+{x1 * a1 - y1}  C. y={ułamki.skracanie(-1, a1)}x+{ułamki.skracanie(y1 * a1 + x1, a1)}  D. y={ułamki.skracanie(-1, a1)}x+{ułamki.skracanie(y1 * a1 - x1, a1)}  \n\n')
    if wersja == 4:
        f.write(
            f'Dla jakiej wartości parametru m punkt M({x1},{y1}-m) należy do wykresu funkcji liniowej y={x2}x{choice(["-", "+"])}{wyraz_wolny}\n'
            f'A. m= {-y1 + x2 * x1 - wyraz_wolny} B. m= {-y1 - x2 * x1 + wyraz_wolny} C. m= {-y1 - x2 * x1 - wyraz_wolny} D. m= {y1 - x2 * x1 - wyraz_wolny} \n\n')


def rozne():
    #zaokraglanie liczb
    q = round(random() * 1000, 4)
    miejsce = choice(['setek', 'dziesiątek', 'jedności', 'części dziesiątych', 'części setnych', 'części tysięcznych'])

    #zadanie z 2 liczbami
    if random() > 0.5:
        polecenie = 'iloczyn'
    else:
        polecenie = 'iloraz'
    a = randint(3, 7) * 48
    b = randint(3, 6) * 32
    potega1 = randint(12, 16)
    potega2 = randint(8, 11)
    #średnia lub mediana
    ile_liczb = randint(3,6)
    liczby=[]
    mediana_czy_srednia = choice(['medianę','średnią'])
    for liczba in range(ile_liczb):
        liczby.append(randint(-4,5))
    #podzielnosc
    ilu_cyfrowa = randint(2,5)
    podzielnosc_przez = choice([2,5,10])
    #ile liczb z danych cyfr
    ile_cyfr = randint (2,4)
    jakie_cyfry=[]
    while len(jakie_cyfry)!=ile_cyfr:
        jaka_cyfra=randint(0,9)
        if jaka_cyfra not in jakie_cyfry:
            jakie_cyfry.append(jaka_cyfra)


    print(jakie_cyfry)

    f.write(choice([
        f'Dane są dwie liczby a = {a}*10^{potega1} i b = {b}*10^{potega2} {polecenie} tych liczb to?\n'
        f'A={a * b}*10^{potega1 + potega2 + 2} B={a * b / 10000}*10^{potega1 + potega2 + 4}  C={a / b * 10}*10^{potega1 - potega2 + 2} D={a / b}*10^{potega1 - potega2} \n\n'
        ,
        f'Zaokrąglenie liczby {q} do {miejsce} to :'
        ,
        f'Oblicz {mediana_czy_srednia} zestawu liczb: {liczby} . '
        ,
        f'Ile jest liczb {ilu_cyfrowa} cyfrowych podzielnych przez {podzielnosc_przez}'
        ,
        f'Wszystkich lizcb {ilu_cyfrowa} cyfrowych w których występują tylko {jakie_cyfry} jest?'



    ]))
