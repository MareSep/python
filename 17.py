
tehingute_arv = 0
tehingud_pos = 0
pos_arv_summa = 0

with open("pangakonto.txt") as fail:   #avab faili
    sisu = fail.readlines()            #loeb failist ridade kaupa
    for number in sisu:
       # print(float(number))
        tehingute_arv += 1
        if float(number) > 0:
            tehingud_pos += 1
            pos_arv_summa += float(number)


print(f"Tehingute arv: {tehingute_arv}")
print(f"Positiivsete tehingute arv: {tehingud_pos}")
print(f"Positiivsete tehingute summa: {pos_arv_summa:.2f}")

with open("palgad.txt") as fail:
    sisu = fail.readlines()
    for i in sisu:
        print(i, end="")