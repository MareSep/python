import turtle

kylg = 100
#v2rvid = ['red', 'green', 'purple', 'blue', 'orange']
t = turtle.Pen()
t.left(90)
#turtle.bgcolor('black')

for i in range(1,10):
    #t.pencolor(v2rvid[i%5])
    #t.pensize(2)
    t.forward(kylg)
    t.right(120)
    t.forward(kylg)
    t.right(120)
    t.forward(kylg)
    t.right(160)
turtle.done()
