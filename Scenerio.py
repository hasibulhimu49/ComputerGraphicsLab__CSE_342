import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightyellow")
screen.setup(width=800, height=800)
t = turtle.Turtle()
t.speed(9)
t.penup()

# Draw sky and sea
colors = ["#FDF2A6", "#F9DC6E", "#F58C50", "#D95692", "#5A3A8A", "#1ABFDA"]
heights = [200, 100, 100, 100, 100, 200]  
y = 400
for color, h in zip(colors, heights):
    t.penup()
    t.goto(-400, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(800)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()
    \
    y -= h


# Draw the half sun
t.penup()
t.speed(6)
t.goto(100, 200)  # Center top of the sun
t.left(90)
t.color("#F58C50")
t.begin_fill()
t.circle(100, 180) 
t.end_fill()



# Draw the boat
t.penup()
t.goto(-250, -300)  # Top-left
t.setheading(0)
t.pendown()
t.color("black")
t.begin_fill()
t.goto(150, -300)    
t.goto(70, -350)     
t.goto(-170, -350)   
t.goto(-250, -300)   
t.end_fill()

# Draw the person on right side using 2 circles (body + head)
t.penup()
t.goto(30, -320) 
t.pendown()
t.begin_fill()
t.circle(25)      
t.end_fill()

t.penup()
t.goto(30, -280)  
t.pendown()
t.begin_fill()
t.circle(15)    
t.end_fill()


# Hide turtle and finish
t.hideturtle()
turtle.done()