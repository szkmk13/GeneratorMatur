from random import randint, choice
import ułamki

f = open("zadania.doc", 'a+', encoding="utf-8")

pole_czy_obwod = choice(['pole', 'obwód'])
kat = choice([30, 45, 60])
triangles_variant = [1, 2, 3, 4, 5, 6, 7]
rectangles_variant = [1, 2, 3, 4, 5]


def trojkaty():
    a = randint(1, 7)
    b = randint(4, 8)
    h = str(choice(['', 2, 3, 4, 5, 6])) + '\u221A3'
    prr = choice(['Pole', 'Długość promienia okręgu opisanego', 'Długość promienia okręgu wpisanego'])
    exercises = {
        1: f'Dany jest trójkąt równoboczny o boku {choice([a, h])}. {prr} tego trójkąta to ?',
        2: f'Dany jest trójkąt równoboczny, którego wysokość to {choice([a, h])}. {prr} tego trójkąta to ?',
        3: f'Trójkąt równoramienny o podstawie równej {a} i ramieniu {b} ma pole równe ?',
        4: f'Oblicz pole trójkąta o bokach długości {a} oraz {b} i kącie {kat}° między nimi',
        5: f'Na przeciwprostokątnej trójkąta o przyprostokątnych {a} i {h} zbudowano trójkąt równoboczny, {prr} tego trójkąta wynosi:',
        6: f'Dwa trójkąty równoboczne są do siebie podobne w skali {randint(2, 4)}, {choice(["mniejszy", "większy"])} z nich ma bok długości o {a}. Oblicz pole drugiego',
        7: f'Dwa trójkąty mają obwody podobne w skali {randint(2, 6)} ich pola są podobne w skali:'
    }
    try:
        a = choice(triangles_variant)
        f.write(exercises[a] + '\n\n')
        triangles_variant.remove(a)
    except:
        IndexError


def czworokaty():
    a = 1
    b = 1
    while a == b:
        a = randint(1, 7)
        b = randint(1, 7)
    d = str(choice(['', 2, 3, 4, 5, 6])) + '\u221A2'
    a_czy_d = choice([a, d])
    bok_czy_przekatna = choice([f'bok jest równy ', f'przekątna ma długość '])
    exercises = {
        1: f'Kwadrat którego {bok_czy_przekatna}{a_czy_d} ma pole równe ?',
        2: f'Romb, w którym {choice(["bok", "wysokość"])} ma długość {a}, a kąt ostry {kat}°. Oblicz pole tego rombu.',
        3: f'Wiedząc że przekątne rombu mają długosci {a} oraz {b} oblicz {choice(["pole", "długość boku"])} tego rombu',
        4: f'Wiedząc że dłuższa podstawa trapezu równoramiennego ma dugość {a * 4} a krótsza jest dwa razy krótsza, oblicz jego pole',
        5: f'Prostokąt o bokach długości {a} oraz {b} ma {choice(["pole równe", "przekątną równą"])} ?'
    }
    try:
        a = choice(rectangles_variant)
        f.write(exercises[a] + '\n\n')
        rectangles_variant.remove(a)
    except:
        IndexError


def rozne():
    choice([trojkaty(), czworokaty()])
