import turtle

t = turtle.Turtle()

turtle.setup(1400, 1400)
t.penup()
t.goto(-400, -240)  # Adjusted starting position for the larger rectangle
t.pendown()

t.fillcolor("green")
t.begin_fill()

for i in range(2):
    t.forward(800)  # Increased width
    t.left(90)
    t.forward(480)  # Increased height
    t.left(90)

t.end_fill()

t.penup()
t.goto(0, -150)  # Adjusted for larger circle
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(150)  # Increased radius
t.end_fill()

turtle.mainloop()
