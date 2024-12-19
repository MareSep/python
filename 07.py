#19.12
#Mare

#7.1
nimi = ["Jyri Pootsman", "Mari Jyrgens", "ansambel Maali", "Terminaator - Juulikuus lumi on maas"]

for i in range (4):
    print(f"{i+1}. {nimi[i]}")
valik = int(input("Vali lugu (1-4): "))
print(f"Mängin: {nimi[valik-1]}")