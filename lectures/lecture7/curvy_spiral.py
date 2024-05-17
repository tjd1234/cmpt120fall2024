# curvy_spiral.py

import turtle
import math

#
# Draws a curvy spiral.
#
# The turtle only draws straight lines, but sometimes they can look curved.
#
# Try putting different values in forward and left to see what sort
# of shapes you can draw. They can be quite surprising!
#
for i in range(1, 100):
    turtle.forward(i * math.sin(i))
    turtle.left(10)