from random import randint, choice

f = open("zadania.doc", 'a+', encoding="utf-8")


def kwadratowa():
    while True:
        a = randint(-5, 5)
        b = randint(-15, 15)
        c = randint(-15, 15)
        delta = b * b - 4 * a * c
        if (delta in [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]) and (a not in [-1, 0, 1]):
            break
    f.write(f'Rozwiąż:\n{a}x\u00b2')
    if b != 0:
        if b > 0:
            f.write(f'+{b}x')
        else:
            f.write(f'{b}x')
    if c != 0:
        if c > 0:
            f.write(f'+{c}')
        else:
            f.write(f'{c}')
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
