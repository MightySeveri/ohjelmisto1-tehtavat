lentoasemat = {}

def syota_lentoasema():
    icao = input("Syötä lentoaseman ICAO-koodi: ")
    nimi = input("Syötä lentoaseman nimi: ")
    lentoasemat[icao] = nimi
    print("Lentoasema tallennettu.")
def hae_lentoasema():
    icao = input("Syötä lentoaseman ICAO-koodi: ")
    if icao in lentoasemat:
        print(f"Lentoaseman nimi: {lentoasemat[icao]}")
    else:
        print("Lentoasemaa ei löydy.")
while True:
    print("\nValitse toiminto:")
    print("1: Syötä uusi lentoasema")
    print("2: Hae lentoaseman tiedot")
    print("3: Lopeta ohjelma")
    valinta = input("Syötä valintasi (1, 2, tai 3): ")

    if valinta == "1":
        syota_lentoasema()
    elif valinta == "2":
        hae_lentoasema()
    elif valinta == "3":
        print("Ohjelma lopetettu.")
        break
    else:
        print("Virheellinen valinta, yritä uudelleen.")
