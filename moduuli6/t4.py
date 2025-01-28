lista = []

def kokonainen():
    summa = 0
    while True:
        luku = input('Syötä kokonaisluku:')
        if luku == "":
            break
        lista.append(int(luku))
        summa += int(luku)
    return summa
summa = kokonainen()
print('Syötettyjen lukujen summa on:', summa)
