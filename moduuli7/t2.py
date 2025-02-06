nimet = set()

while True:
    nimi = input("Syötä nimi (jätä tyhjäksi lopettaaksesi): ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
print("\nSyötetyt nimet:")
for nimi in nimet:
    print(nimi)
