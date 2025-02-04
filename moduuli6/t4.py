def laske_summa(lista):
    return sum(lista)

def paaohjelma():
    lista = []
    while True:
        luku = input('Syötä kokonaisluku: ')
        if luku == "":
            break
        lista.append(int(luku))
    summa = laske_summa(lista)
    print('Syötettyjen lukujen summa on:', summa)

paaohjelma()
