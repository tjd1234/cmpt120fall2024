# square_random_walk.py

import turtle
import random

#
# The turtle draws a random-looking path made of straight lines.
#

# Try changing the numbers in this list.
possible_angles = [0, -90, 90, -45, 45, 17]

for i in range(1, 100):
    step = random.randint(10, 20)
    turtle.forward(step)
    angle = random.choice(possible_angles)
    turtle.left(angle)
