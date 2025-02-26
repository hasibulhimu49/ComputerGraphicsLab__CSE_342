import matplotlib.pyplot as plt
r = 200
x = 0
y = r
p = 1 - r
xcor=[]
ycor=[]
while x <= y:

    if p < 0:
        x=x+1
        y=y
        p = p +  2 * x + 1
    else:
        x=x+1
        y=y-1
        p = p - 2*y + 2*x + 1

    xcor.append(x)
    ycor.append(y)
    xcor.append(y)
    ycor.append(x)
    xcor.append(x)
    ycor.append(-y)
    xcor.append(y)
    ycor.append(-x)
    xcor.append(-x)
    ycor.append(-y)
    xcor.append(-y)
    ycor.append(-x)
    xcor.append(-x)
    ycor.append(y)
    xcor.append(-y)
    ycor.append(x)

plt.scatter(xcor,ycor)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("MID POINT CIRCLE ALGO")
plt.show()
