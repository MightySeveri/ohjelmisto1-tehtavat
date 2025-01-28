luku = int(input('Syötä luku:'))

if luku <= 1:
    print(f'{luku} ei ole alkuluku.')
else:
    alku = True
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            alku = False
            break
    if alku:
        print(f'{luku} on alkuluku.')
    else:
        print(f'{luku} ei ole alkuluku.')
