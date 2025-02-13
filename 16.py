import os
from datetime import date

print(f"Tere {os.getlogin()}")
print(f"sinu rada {os.getcwd()}")

kataloogidearv = 10
kustuta = 8
kp = str(date.today())

#loob kaustad
try:
    os.mkdir(kp)
    print(f"{kp} kataloog loodud")
    for i in range(1, kataloogidearv+1):
        kaust = kp+"/"+str(i)
        os.makedirs(kaust)
except:
    print("Kataloog on juba olemas")

#kustutab kausta
if os.path.exists(kp+"/"+str(kustuta)):
    os.rmdir(kp+"/"+str(kustuta))
    print(f"{kustuta} kataloog kustutatud")
else:
    print(f"{kustuta} kataloogi ei leitud")
