# You must import the turtle library before using turtle graphics.
import turtle

# optionally, you can set the pen color and size
turtle.pensize(5)
turtle.shape('turtle')

# draw a square
for c in ['orange', 'red', 'yellow', 'green']:
    turtle.color(c)
    turtle.forward(100)
    turtle.left(90)