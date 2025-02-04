def parittomat(lista):
    karsittu_lista = [luku for luku in lista if luku % 2 == 0]
    return karsittu_lista


def paa():
    lista = []
    while True:
        luku = input('Syötä kokonaisluku (jätä tyhjäksi lopettaaksesi): ')
        if luku == "":
            break
        lista.append(int(luku))

    karsittu_lista = karsi_parittomat(lista)

    print('Alkuperäinen lista:', lista)
    print('Karsittu lista:', karsittu_lista)


paa()
