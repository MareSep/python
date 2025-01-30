#3.1

# fail = open("rebased.txt", encoding="UTF-8")
# vastuvoetud = []

# for rida in fail:
#     vastuvoetud.append(int(rida))
# fail.close()

# aasta = input("Sisesta aasta vahemikus 2011-2019: ")
# print(vastuvoetud[int(aasta[-1])-1])

#3.3

# fail = open("konto.txt", encoding="UTF-8")

# for kirje in fail:
#     if float(kirje) > 0:
#         print(float(kirje), end="\n")

# fail.close()

#3.4
# musa = "edm"
# fail = open(f"kaustanimi/{musa}.txt", encoding="UTF-8")

muusika = "edm.txt"
fail = open(muusika, encoding="UTF-8")

nr = 1
#Näita kõiki lugusid
for pala in fail:
    print(str(nr) + ". " + pala, end="")
    nr += 1

#Kuva valitud lugu
print()
valik = int(input("Vali lugu: "))
fail.seek(0)
#fail = open(muusika, encoding="UTF-8")
mangin = 1
for pala in fail:
    if valik == mangin:
        print(pala, end="")
    mangin += 1
fail.close()
