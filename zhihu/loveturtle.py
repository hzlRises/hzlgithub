import turtle
import math
wn = turtle.Screen()
wn.setworldcoordinates(-2, -2, 2, 2)
alex = turtle.Turtle()
alex.color("red")
alex.pensize(2)
alex.penup()
alex.speed(0)
walkStart = -1
walkEnd = 1
i = walkStart
j = walkEnd
while i <= 0 and j >= 0:
    y1 = math.sqrt(1 - i * i) + (i * i) ** (1/3.0)
    y2 = -math.sqrt(1 - i * i) + (i * i) ** (1/3.0)
    y3 = math.sqrt(1 - j * j) + (j * j) ** (1/3.0)
    y4 = -math.sqrt(1 - j * j) + (j * j) ** (1/3.0)
    alex.setx(i)
    alex.sety(y1)
    alex.dot()
    alex.sety(y2)
    alex.dot()
    alex.setx(j)
    alex.sety(y3)
    alex.dot()
    alex.sety(y4)
    alex.dot()
    i += 0.01
    j -= 0.01
