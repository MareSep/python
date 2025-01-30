#11.1
def pikim_sona(s):
    sona = ""
    for i in s:
        if len(sona) < len(i):
            sona = i
    print("Pikim sõna on: " + sona)

#11.2
def viruvinkel(t1, t2):
    if t1[0] == t2[0]:
        return True
    else:
        return False


sonad = ["viisnurk", "ring", "ruut", "suvaline"]
pikim_sona(sonad)
print(viruvinkel("Mario", "Mets"))
