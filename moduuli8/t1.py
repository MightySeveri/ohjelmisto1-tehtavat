import mysql.connector

def hae_kentan_tiedot(icao):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='airports',
        user='root',
        password='root',
        autocommit=True
    )
    kursori = yhteys.cursor()
    sql = f"SELECT name FROM airports WHERE ident='{icao}'"
    print(sql)
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Kentän tiedot ovat: {rivi[0]}")
    else:
        print("Lentoasemaa ei löydy.")

    kursori.close()
    yhteys.close()

hae_kentan_tiedot(icao)
