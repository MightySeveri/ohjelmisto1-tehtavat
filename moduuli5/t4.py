city = []

kaupunki = input('Syötä kaupunkeja: ')
while kaupunki != "":
    city.append(kaupunki)
    kaupunki = input('Syötä kaupunkeja: ')

print('Kaupungit listattuna:')
for nimi in city:
    print(nimi)
