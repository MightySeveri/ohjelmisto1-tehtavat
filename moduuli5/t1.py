import random

noppa = int(input('Syötä noppien määrä: '))
summa = 0

for kiekka in range(noppa):
    numero = random.randint(1, 6)
    summa += numero

print(f'Noppien summa: {summa}')
