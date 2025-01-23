yritykset = 0
while True:
    tun = input('Syötä tunnus:')
    sal = input('Syötä salasana:')
    if yritykset == 5:
        print('tili lukittu')
        break
    if tun != 'python' or sal != 'rules':
        print('tunnus tai salasana väärin')
    if tun == 'python' and sal == 'rules':
        print('tervettuloa')
        yritykset += 1
        break