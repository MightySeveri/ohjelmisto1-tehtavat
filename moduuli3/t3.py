suku = input('Syötä sukupuolesi: ')
arvo = float(input('Syötä hemoglobiini arvosi: '))

if suku == "mies":
    mukua = 134
    mukuy = 195
    if mukua <= arvo <= mukuy:
        print('Kaikki hyvin')
    else:
        print('paniikki')
elif suku == "nainen":
    nukua = 117
    nukuy = 175
    if nukua <= arvo <= nukuy:
        print('Kaikki hyvin')
    else:
        print('paniikki')