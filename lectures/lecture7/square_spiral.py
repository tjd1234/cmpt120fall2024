# square_spiral.py

import turtle
import math

#
# Draws a square spiral
#
# In the turtle.forward statement, try different expression, e.g. 3*i, i*i,
# i * math.sin(i)
#
for i in range(1, 100):
    turtle.forward(3 * i)
    turtle.left(90)