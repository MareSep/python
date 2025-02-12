# PANGAKONTO
# Looge funktsioon, mis võimaldab lisada või eemaldada summasid pangakontolt. Funktsioon peaks algama algse saldoga ja võimaldama teha operatsioone:
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
algne_saldo = 100
summa = 
deposiit = algne_saldo + summa
valjavote = algne_saldo - summa
def kontohaldur(algne_saldo, toiming, summa):
