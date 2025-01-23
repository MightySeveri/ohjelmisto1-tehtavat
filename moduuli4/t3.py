luku = 6
arva = input('arvaa luku')
while luku != arva:
    if arva < 6:
        print('liian pieni')
    if arva > 6:
        print('liian suuri')
    if arva == luku:
        print('aivan oikein')