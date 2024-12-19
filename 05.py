#1,

try:
    vanus = int(input("Sinu vanus: "))
    if vanus >= 18:
        print("Lubatud")
    else:
        print("Keelatud")

except:
    print("Viga sisestuses!")

#2.
try:
    kraadid = 20
    
    if kraadid < 0:
        print("Talveriided")
    elif kraadid >= 0 and kraadid <= 15:
        print("Kevad-sügis")
    else:
        print("Suvi!")
except:
    print("Viga sisestuses!")
    
#3.
import random

try:
    arv1 = random.randint(1,10)
    arv2 = random.randint(1,10)
    vastus = int(input(f"Mis on {arv1} * {arv2} vastus? \nSisesta vastus:"))
    korrutis = arv1 * arv2
    if korrutis == vastus:
        print("Õige!")
    else:
        print("Vale!")
    
except:
    print("viga")
    
#4.
import random
import turtle

try:
    valik = random.randint(0,1)
    arvamus = int(input("Vali kull 1 või kiri 0: "))
    if valik == arvamus:
        print("Arvasid ära")
        turtle.color("green")
        turtle.circle(50)
    else:
        print("Arvasid valesti")
        turtle.color("red")
        turtle.circle(50)
    turtle.done()
except:
    print("viga")


