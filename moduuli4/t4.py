luku = 6
arva = input('arvaa luku')
arva =int(arva)
while luku != arva:
    arva = int(input('arvaa luku'))
    if arva < luku:
        print('liian pieni')
    if arva > luku:
        print('liian suuri')
    if arva == luku:
        print('aivan oikein')

#ohejlma kysyy ensimmäisellä kerralla kahdesti koska en keksinyt miten saan sen muuten loopattua