vuosi = int(input('syötä vuosiluku'))
if vuosi % 4 == 0 and vuosi % 400 == 0:
    print('vuosi on karannut')
elif vuosi % 4 == 0 and vuosi % 400 != 0:
    print('vuosi on karannut')
else:
    print('vuosi ei ole karannut')