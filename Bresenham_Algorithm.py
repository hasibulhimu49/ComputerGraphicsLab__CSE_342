import matplotlib.pyplot as plt
print("Enter the value of x1")
x1=int(input())
print("Enter the value of x2")
x2=int(input())
print("Enter the value of y1")
y1=int(input())
print("Enter the value of y2")
y2=int(input())
dx= x2-x1
dy=y2-y1
pk=2*dy-dx
if abs(dx) > abs(dy):
     steps = abs(dx)
else:
     steps = abs(dy)

xcoordinate = []
ycoordinate = []

i=0
while i<steps:
     i+=1
     if pk>=0:
      x1=x1+1
      y1=y1+1
      pk=pk+2*dy-2*dx
     elif pk<1:
      x1=x1+1
      y1=y1
      pk=pk+2*dy
     print("x1: ",x1, "y1:", y1)
     xcoordinate.append(x1)
     ycoordinate.append(y1)
plt.plot(xcoordinate,ycoordinate, color='red', marker='o')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Bresenham Line Drawing Algorithm")
plt.show()
