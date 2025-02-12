# PANGAKONTO
# Looge funktsioon, mis võimaldab lisada või eemaldada summasid pangakontolt. Funktsioon peaks algama algse saldoga ja võimaldama 
# teha operatsioone:
#  deposiit (raha lisamine)
#  väljavõte (raha eemaldamine)
# Tagastage peale igat toimingut konto jääk.
# Funtsiooni parameetrid:
#  algne_saldo: algse saldo väärtus
#  toiming: String, mis tähistab tehtavat toimingut ('deposiit' või 'valjavote')
#  summa: summa, mida soovitakse lisada või eemaldada
# Näide:
# Alustades algse saldoga 100, deposiidi toiminguga 50, peaks funktsioon konto_haldur tagastama uue saldo 150.
# Väljavõte toiminguga 20 uus saldo oleks siis 130.
fail = open("kontojaak.txt")
algne_saldo = int(fail.read().strip())

def kontohaldur(algne_saldo, toiming, summa):
    if toiming == "deposiit":
        kontojaak = algne_saldo + summa
        with open("kontojaak.txt", "w") as fail:
            fail.write(str(kontojaak))
    elif toiming == "valjavote":
        kontojaak = algne_saldo - summa
        with open("kontojaak.txt", "w") as fail:
            fail.write(str(kontojaak))
    return kontojaak
   

toiming = input("Vali toiming: deposiit/valjavote: ")
summa = abs(int(input("Sisesta summa: ")))  #teisendan sisendi absoluutväärtuseks, muidu saab negatiivset arvu kasutades 
#vastupidiseid tehinguid teha
print(f"Kontojääk on {kontohaldur(algne_saldo, toiming, summa)} eurot")