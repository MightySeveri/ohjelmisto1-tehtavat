import math

def yksikkohinta(halkaisija, hinta):
    sade_metreina = (halkaisija / 2) / 100
    pinta_ala = math.pi * (sade_metreina ** 2)
    return hinta / pinta_ala

def paa():
    halkaisija1 = float(input('Syötä ensimmäisen pizzan halkaisija senttimetreinä: '))
    hinta1 = float(input('Syötä ensimmäisen pizzan hinta euroina: '))
    halkaisija2 = float(input('Syötä toisen pizzan halkaisija senttimetreinä: '))
    hinta2 = float(input('Syötä toisen pizzan hinta euroina: '))

    yksikkohinta1 = yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = yksikkohinta(halkaisija2, hinta2)

    print(f'Ensimmäisen pizzan yksikköhinta on {yksikkohinta1:.2f} euroa per neliömetri')
    print(f'Toisen pizzan yksikköhinta on {yksikkohinta2:.2f} euroa per neliömetri')

    if yksikkohinta1 < yksikkohinta2:
        print('Ensimmäinen pizza antaa paremman vastineen rahalle.')
    elif yksikkohinta1 > yksikkohinta2:
        print('Toinen pizza antaa paremman vastineen rahalle.')
    else:
        print('Molemmat pizzat antavat saman vastineen rahalle.')

paa()
