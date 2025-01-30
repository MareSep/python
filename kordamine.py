#1.1

print("Tere, maailm!")
print('"Tere, maailm!"')

#1.2

aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = str(aasta) + lause_keskosa + liblikas
print(lause)

#1.3

korgus = float(input("Sisesta pilvede aluse kõrgus kilomeetrites: "))
if korgus > 6:
    print("Ülemised")
elif korgus >= 2 and korgus <= 6:
    print("Keskmised")
else:
    print("Alumised")

#1.4

import math
inimesed = int(input("Sisesta inimeste arv: "))
kohti = int(input("Sisesta bussi kohtade arv: "))
busse = 1
jaak = inimesed%kohti

if jaak > 0:
    busse = (inimesed//kohti)+1
else:
    busse = inimesed//kohti
if jaak == 0:
    jaak = kohti

print(f"Busside arv: {busse}")
print(f"Viimases bussis on inimesi: {jaak}")