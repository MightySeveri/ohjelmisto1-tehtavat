luvut = []

while True:
    luku = input('Syötä luku: ')
    if luku == '':
        break
    luku = int(luku)
    if luku > 0:
        luvut.append(luku)

luvut.sort(reverse=True)
print('Viisi suurinta lukua annetuista:', luvut[:5])
