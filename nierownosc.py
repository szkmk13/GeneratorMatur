from random import randint, choice

f = open("zadania.doc", 'a+', encoding="utf-8")


def kwadratowa():
    while True:
        l = []
        for a in range(6):
            number = randint(-8, 8)
            while number == 0:
                number = randint(-8, 8)
            l.append(number)
        a1 = l[2] * l[4]
        b1 = l[2] * l[5] + l[3] * l[4] - l[0]
        c1 = l[3] * l[5] - l[1]
        delta = b1 * b1 - 4 * a1 * c1
        if (delta in [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]) and (
                a1 not in [0, 1]):
            break
    znak = choice(['\u003c', '\u003e', '\u2264', '\u2265'])

    f.write(f'Oblicz:\n')
    f.write(f'{l[0]}x')
    f.write(f'+{l[1]}') if l[1] > 0 else f.write(f'{l[1]}')
    f.write(f' {znak} ')
    f.write(f'({l[2]}x')
    f.write(f'+{l[3]})') if l[3] > 0 else f.write(f'{l[3]})')
    f.write(f'({l[4]}x')
    f.write(f'+{l[5]})\n\n') if l[5] > 0 else f.write(f'{l[5]})\n\n')
    print(delta, a1, b1, c1)
    print(l)
    print(f'{l[0]}x + {l[1]} = ({l[2]}x + {l[3]})({l[4]}x + {l[5]})')

    while True:
        a = randint(-5, 5)
        b = randint(-15, 15)
        c = randint(-15, 15)
        delta = b * b - 4 * a * c
        if (delta in [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]) and (a not in [0, 1]):
            break
    f.write(f'Rozwiąż:\n-x\u00b2') if a == -1 else f.write(f'Rozwiąż:\n{a}x\u00b2')
    f.write(f'+{b}x') if b > 0 else f.write(f'{b}x') if b < 0 else f.write(f'')
    f.write(f'+{c}') if c > 0 else f.write(f'{c}') if c < 0 else f.write(f'')
    znak = choice(['\u003c', '\u003e', '\u2264', '\u2265'])
    f.write(f' {znak} 0\n\n')


def liniowa():
    znak = choice(['\u003c', '\u003e', '\u2264', '\u2265'])
    wersja = choice([1, 2])
    nierownosc = ''
    while True:
        q = randint(-6, 6)
        w = randint(-6, 6)
        e = randint(2, 6)
        r = randint(-6, 6)
        t = randint(-6, 6)
        y = randint(2, 6)
        if 0 not in [q, w, e, r, t, y] and 1 not in [q, w, e, r, t, y] and -1 not in [q, w, e, r, t, y]:
            break
    if wersja == 1:
        nierownosc = f'{q}({w}x{choice(["+", "-"])}{e}){znak}{r}({t}{choice(["+", "-"])}{y}x)'
    elif wersja == 2:
        nierownosc = f'{q}({w}x{choice(["+", "-"])}{e}\u221A{2}){znak}{r}x{choice(["+", "-"])}{y}\u221A{2}'
    f.write(f'Oblicz:\n {nierownosc} \n\n')


def z_wartoscia_bezwzledna():
    znak = choice(['\u003c', '\u003e', '\u2264', '\u2265'])
    wersja = choice([1, 2, 3])
    nierownosc = ''
    while True:
        q = randint(-6, 6)
        w = randint(-6, 6)
        e = randint(2, 6)
        r = randint(-6, 6)
        t = randint(-6, 6)
        y = randint(2, 6)
        if 0 not in [q, w, e, r, t, y] and 1 not in [q, w, e, r, t, y] and -1 not in [q, w, e, r, t, y]:
            break
    if wersja == 1:
        nierownosc = f'|{w}x{choice(["+", "-"])}{e}|{znak}{y}'
    elif wersja == 2:
        nierownosc = f'|{w}x{choice(["+", "-"])}{e}\u221A{2}|{znak}{y}\u221A{2}'
    elif wersja == 3:
        nierownosc = f'{y}\u221A{2}{znak}|{w}x{choice(["+", "-"])}{e}\u221A{2}|'
    f.write(f'Oblicz:\n {nierownosc} \n\n')
