lista = []
def kokonainen():
    while True:
        luku = input('Syötä kokonaisluku:')
        if luku == "":
            break
        lista.append(int(luku))
        tasa = int(luku)
        if luku % 2 == 0:
    return tasa
tasa = kokonainen()
print('Syötetyt parilliset luvut ovat:', lista)
