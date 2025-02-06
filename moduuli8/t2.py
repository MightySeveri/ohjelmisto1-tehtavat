import mysql.connector
def hae_maakoodi(iso_country):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='airports',
        user='root',
        password='root',
        autocommit=True
    )
    kursori = yhteys.cursor()
    sql = f"SELECT name FROM airport WHERE iso_country='{iso_country}'"
    print(sql)
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Maakoodi on: {rivi[0]}")
    else:
        print("Maakoodia ei löydy.")

    kursori.close()
    yhteys.close()

hae_maakoodi('FI')
