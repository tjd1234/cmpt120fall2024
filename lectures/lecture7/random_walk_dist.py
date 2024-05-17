# random_walk_dist.py

import turtle
import random
import math

#
# The turtle draws a random-looking curvy path.
#
# The turtle starts at point (0, 0) in the center
# of the screen.
#
for i in range(1, 100):
    step = random.randint(3, 10)
    turtle.forward(step)
    angle = random.randint(-45, 45)
    turtle.left(angle)

#
# get the final position of the turtle
#
x = turtle.xcor()
y = turtle.ycor()

#
# calculate the distance between (0, 0) and (x, y)
#
dist = math.sqrt(x**2 + y**2)

print(f'The turtle ended up at ({x}, {y})')
print(f'{dist} pixels from where it started')