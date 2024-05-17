# triangle1.py

import turtle

turtle.color('orange')
turtle.pensize(5)

for i in range(3):
    turtle.forward((i+1)*100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)