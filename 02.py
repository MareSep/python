# 02. ülesanne

"""
    Loo aken, mille nimi on “Olümpiarõngad ja sinu nimi”
    Akna suurus 500×400
    Loo värvilised 50px olümpiarõngad (sinine, must, punane, kollane, roheline)
    Joone paksus 6
    Kiirus 0
"""
import turtle

#akna seaded
aken = turtle.Screen()
aken.setup(width=600, height=500)
aken.title("Olümpiarõngad ja Mare")
#sinine
turtle.speed(0)
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
turtle.color("blue")
turtle.pensize(6)
turtle.circle(50, 360)
#must
turtle.penup()
turtle.goto(-90, 100)
turtle.pendown()
turtle.color("black")
turtle.pensize(6)
turtle.circle(50, 360)
#punane
turtle.penup()
turtle.goto(20, 100)
turtle.pendown()
turtle.color("red")
turtle.pensize(6)
turtle.circle(50, 360)
#kollane
turtle.penup()
turtle.goto(-145, 45)
turtle.pendown()
turtle.color("yellow")
turtle.pensize(6)
turtle.circle(50, 360)
#roheline
turtle.penup()
turtle.goto(-35, 45)
turtle.pendown()
turtle.color("green")
turtle.pensize(6)
turtle.circle(50, 360)

turtle.done()