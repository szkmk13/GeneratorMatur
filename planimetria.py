from random import randint, choice
import ułamki

f = open("zadania.doc", 'a+', encoding="utf-8")

pole_czy_obwod = choice(['pole', 'obwód'])
kat = choice([30, 45, 60])


def trojkaty():
    a = randint(1, 7)
    b = randint(4, 8)
    h = str(choice(['', 2, 3, 4, 5, 6])) + '\u221A3'
    prr = choice(['Pole', 'Długość promienia okręgu opisanego', 'Długość promienia okręgu wpisanego'])
    f.write(choice([
        f'Dany jest trójkąt równoboczny o boku {choice([a, h])}. {prr} tego trójkąta to ?\n\n',
        f'Dany jest trójkąt równoboczny, którego wysokość to {choice([a, h])}. {prr} tego trójkąta to ?\n\n',
        f'Trójkąt równoramienny o podstawie równej {a} i ramieniu {b} ma pole równe ?\n\n',
        f'Oblicz pole trójkąta o bokach długości {a} oraz {b} i kącie {kat}° między nimi\n\n',
        f'Na przeciwprostokątnej trójkąta o przyprostokątnych {a} i {h} zbudowano trójkąt równoboczny, {prr} tego trójkąta wynosi:\n\n',
        f'Dwa trójkąty równoboczne są do siebie podobne w skali {randint(2, 4)}, {choice(["mniejszy", "większy"])} z nich ma bok długości o {a}. Oblicz pole drugiego\n\n'
    ]))


def czworokaty():
    a = 1
    b = 1
    while a == b:
        a = randint(1, 7)
        b = randint(1, 7)
    d = str(choice(['', 2, 3, 4, 5, 6])) + '\u221A2'
    a_czy_d = choice([a, d])
    bok_czy_przekatna = choice([f'bok jest równy ', f'przekątna ma długość '])
    print(f'Kwadrat którego {bok_czy_przekatna}{a_czy_d} ma pole równe ?')
    print(f'Romb, w którym {choice(["bok", "wysokość"])} ma długość {a}, a kąt ostry {kat}°. Oblicz pole tego rombu.')


def rozne():
    choice([trojkaty(), czworokaty()])
