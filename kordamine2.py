#2.1

# korrad = int(input("Mitu korda heliseb?: "))

# for i in range(korrad):
#     print("Tõuse ja sära!")

#2.2

# ringid = int(input("Ringide arv: "))
# porgand = 0

# while ringid > 0:
#     if ringid % 2 == 0:
#         porgand += 2
#     ringid -= 1
# print(f"Porgandite arv on {porgand}")


#2.5

import random
ounad = 14
pp = int(input("Mitu pöialpoissi tahab õuna: "))

for i in range(pp):
    oun = random.randint(1,2)
    ounad -= oun
    print(oun)
print(f"Lumivalgekesele jäi {ounad} õuna")