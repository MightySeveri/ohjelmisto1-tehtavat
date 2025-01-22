tuuma = int(input('syötä tuumia'))
va = tuuma * 2.54
while va > 0:
    tuuma = int(input('syötä tuumia'))
    va = tuuma * 2.54
    print(f"tuumat muunnettuna centeiksi", va)
else:
    print('ei käy negatiivinen')