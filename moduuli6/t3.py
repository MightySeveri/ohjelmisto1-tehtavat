def menovesi():
    bensa = float(input('syötä bensiinin määrä gallonoina'))
    while bensa > 0:
        bensa = float(input('syötä bensiinin määrä gallonoina'))
        litra = bensa * 3.785
        print(litra)
menovesi()
