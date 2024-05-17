# square5.py

# You must import the turtle library before using turtle graphics.
import turtle

# optionally, you can set the pen color and size
turtle.pensize(5)

# draw a square
for c in ['orange', 'red', 'yellow', 'green']:
    turtle.color(c)
    turtle.forward(50)
    turtle.left(90)
