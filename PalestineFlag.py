import turtle
t = turtle.Turtle()

turtle.setup(1000, 1000)
t.penup()
t.goto(-200, 120) 
t.pendown()

t.fillcolor("black")
t.begin_fill()

for i in range(2):
    t.forward(400)
    t.left(90)
    t.forward(80)
    t.left(90)

t.end_fill()

t.fillcolor("white")
t.begin_fill()

for i in range(2):
    t.forward(400)
    t.right(90)
    t.forward(80)
    t.right(90)

t.end_fill()

t.penup()
t.goto(-200, -40) 
t.pendown()

t.fillcolor("green")
t.begin_fill()

for i in range(2):
    t.forward(400)
    t.left(90)
    t.forward(80)
    t.left(90)

t.end_fill()

t.fillcolor("red")
t.begin_fill()

t.left(45)
t.forward(170)
t.left(90)
t.forward(170)
t.left(135)
t.forward(240)
t.end_fill()

turtle.mainloop()