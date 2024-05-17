# curvy_random_walk.py

import turtle
import random

#
# The turtle draws a random-looking curvy path.
#
for i in range(1, 100):
    step = random.randint(3, 10)
    turtle.forward(step)
    angle = random.randint(-45, 45)
    turtle.left(angle)