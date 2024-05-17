# rand_walk2.py

#
# The turtle does a "random walk" across the screen. If it hits the edge of
# the screen, it immediately jumps back to the center, i.e. position (0, 0).
#
# random.uniform(a, b) returns a random float from a to b.
#

import turtle
import random

#
# Get the dimensions of the screen.
#
max_X = turtle.window_width() / 2
min_X = -max_X

max_Y = turtle.window_height() / 2
min_Y = -max_Y

# print(f'upper right = ({min_X}, {max_X}), lower left = ({min_Y}, {max_Y})')

def jump_to(x, y):
    """ Move turtle to (x, y) without drawing a line.
    """
    turtle.up()
    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.goto(x, y)
    turtle.speed('normal')
    turtle.showturtle()
    turtle.down()

#
# main program
#
for n in range(1000):
    turtle.forward(10)
    angle = random.uniform(-10, 10)
    turtle.left(angle)

    x, y = turtle.position()

    if x > max_X:   # gone off the right edge?
        jump_to(0, 0)
    elif x < min_X: # gone off the left edge?
        jump_to(0, 0)
    elif y > max_Y: # gone off the bottom edge?
        jump_to(0, 0)
    elif y < min_Y: # gone off the top edge?
        jump_to(0, 0)
