import random

def noppa():
    numero = random.randint(1, 6)
    while numero != 6:
        print(numero)
        numero = random.randint(1, 6)
    print('Kutonen heitetty')

noppa()
