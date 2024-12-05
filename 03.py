# 03. ülesanne
#Mare 05.12.2024
import turtle

#3.1 Tervitus
nimi = "Imre"
vanus = 20
keskmine_hinne = 6.5
print(nimi,",", vanus, "aastat vana ja keskmine hinne on", keskmine_hinne,".")
print(f"{nimi}, {vanus} aastat vana ja keskmine hinne on {keskmine_hinne}.")

#3.2 Ostunimekiri

toode = "porgand"
kogus = 3
hind = 5.35
print("Soovin "+str(toode)+"eid "+str(kogus)+", mille tüki hind on "+str(hind)+" eurot.")

#3.3 Reisiplaan

sihtkoht = "Soome"
paevade_arv = 5
oobimise_hind = 30.50
print(sihtkoht, "reis kestab", paevade_arv, "päeva ja üks öö maksab", oobimise_hind, "eurot.")

#3.7 Turtle kolmnurk

kylje_pikkus = 100
nurk = 120
kujundi_varv = "red"

turtle.shape("turtle")
turtle.speed(0)
turtle.color(kujundi_varv)
"""turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.penup()
turtle.forward(kylje_pikkus*1.5)
turtle.pendown()
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.penup()
turtle.forward(kylje_pikkus*1.5)
turtle.pendown()
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)

turtle.done()"""

for i in range(3):
    turtle.forward(kylje_pikkus)
    turtle.left(nurk)
    turtle.forward(kylje_pikkus)
    turtle.left(nurk)
    turtle.forward(kylje_pikkus)
    turtle.left(nurk)
    turtle.penup()
    turtle.forward(kylje_pikkus*1.5)
    turtle.pendown()
turtle.done()
