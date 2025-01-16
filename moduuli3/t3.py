suku = input('syötä sukupuolesi')
mies = suku
nainen = suku
arvo = input('syötä hemoglobiin arvosi')
if suku == mies:
    muku = (134, 195)
    muku = str (muku)
    if arvo > muku:
        if arvo < muku:
            print('kaikki hyvin')
if suku == nainen:
    nuku = (117, 175)
    nuku = str (nuku)
    if arvo > nuku:
        if arvo < nuku:
            print('kaikki hyvin')
else:
    print('paniikki tee jotain')
