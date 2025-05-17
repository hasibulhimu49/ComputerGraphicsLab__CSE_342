import turtle

screen=turtle.Screen()
screen.setup(1000,600)

t=turtle.Turtle()

# Draw line
t.penup()
t.goto(-400,-200)
t.pendown()
t.forward(800)


#House
t.fillcolor("gray")
t.begin_fill()
t.penup()
t.goto(-250,-200)
t.pendown()
for i in range(2):
    t.forward(500)
    t.left(90)
    t.forward(300)
    t.left(90)
t.end_fill()

#Roof
t.fillcolor("navy")
t.begin_fill()
t.penup()
t.goto(-300,100)
t.pendown()
t.forward(603)
t.setheading(90)
t.left(45)
t.forward(60)
t.setheading(90)
t.left(90)
t.forward(518)
t.left(45)
t.forward(60)
t.penup()
t.end_fill()

#Windows
t.fillcolor("yellow")
t.begin_fill()
t.penup()
t.goto(-150,0)
t.pendown()
t.setheading(90)
for i in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

t.fillcolor("yellow")
t.begin_fill()
t.penup()
t.goto(150,0)
t.pendown()
t.setheading(90)
for i in range(4):
    t.forward(50)
    t.right(90)
t.end_fill()

# Door
t.fillcolor("azure")
t.begin_fill()

t.penup()
t.goto(-30, -200)  
t.pendown()

t.setheading(90)  
t.forward(170)    
t.right(90)
t.forward(60)      
t.right(90)
t.forward(170)     
t.right(90)
t.forward(60)      
t.end_fill()


#Tree
t.fillcolor("green")
t.begin_fill()
t.penup()
t.goto(350,-200)
t.pendown()
t.right(90)
t.forward(100)
t.left(90)
t.forward(50)
t.setheading(90)
t.right(45)
t.forward(50)
t.left(135)
t.forward(30)
t.setheading(90)
t.right(45)
t.forward(70)
t.right(90)


t.forward(70)
t.right(135)
t.forward(30)
t.setheading(-90)
t.left(45)
t.setheading(315)  
t.forward(50)
t.left(-45)
t.right(90)
t.forward(50)
t.left(90)
t.forward(100)
t.end_fill()



# Draw half sun
t.fillcolor("red")
t.begin_fill()
t.penup()
t.goto(-300, -200)  
start_pos = t.pos() 
t.setheading(90)   
t.pendown()
t.circle(50, 180)   
t.goto(start_pos)   
t.end_fill()

# Rays center
t.penup()
t.goto(-350, -200)
t.setheading(90)

for angle in range(0, 181, 30):
    t.setheading(angle)
    t.forward(50)       
    t.pendown()
    t.forward(20)       
    t.penup()
    t.goto(-350, -200)  




turtle.mainloop()
