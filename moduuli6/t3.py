def gallona_litroiksi(gallona):
    return gallona * 3.785

def menovesi():
    bensa = float(input('Syötä bensiinin määrä gallonoina: '))
    while bensa >= 0:
        litra = gallona_litroiksi(bensa)
        print(f'{bensa} gallonaa on {litra:.2f} litraa')
        bensa = float(input('Syötä bensiinin määrä gallonoina: '))

menovesi()
