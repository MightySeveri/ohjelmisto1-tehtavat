hytti = input('missä hyttiluokassa olet?')
LUX = hytti
A = hytti
B = hytti
C = hytti
if hytti==LUX:
    print("hytti on parvekkeellinen hytti yläkannella.")
elif hytti==A:
    print("hytti on ikkunallinen hytti autokannen yläpuolella.")
elif hytti==B:
    print("hytti on ikkunaton hytti autokannen yläpuolella")
else:
    print("hytti on ikkuaton hytti autokannen alapuolella.")