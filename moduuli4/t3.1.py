while True:
    luku = input('Syötä luku: ')
    if luku == '':
        print('Se on loppu nyt')
        break
    luku = int(luku)
    if luku > 0:
        print(luku)
