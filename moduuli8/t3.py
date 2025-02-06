import mysql.connector
from geopy.distance import geodesic

def hae_koordinaatit(icao):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='airports',
        user='root',
        password='root',
        autocommit=True
    )

    kursori = yhteys.cursor()
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{icao}'"
    kursori.execute(sql)
    tulos = kursori.fetchone()

    kursori.close()
    yhteys.close()

    if tulos:
        return (tulos[0], tulos[1])
    else:
        print(f"Lentoaseman {icao} koordinaatteja ei löytynyt.")
        return None

def laske_etaeisyys(icao1, icao2):
    koordinaatit1 = hae_koordinaatit(icao1)
    koordinaatit2 = hae_koordinaatit(icao2)

    if koordinaatit1 and koordinaatit2:
        etaeisyys = geodesic(koordinaatit1, koordinaatit2).kilometers
        print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on {etaeisyys:.2f} kilometriä.")
    else:
        print("Etäisyyden laskeminen epäonnistui.")

icao1 = input("Syötä ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Syötä toisen lentokentän ICAO-koodi: ")

laske_etaeisyys(icao1, icao2)
