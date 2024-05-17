# rand_walk3.py

#
# The turtle does a "random walk" across the screen. If it hits the edge of
# the screen, it jumps to the opposite side, i.e. it "wraps around".
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
        jump_to(min_X, y)
    elif x < min_X: # gone off the left edge?
        jump_to(max_X, y)
    elif y > max_Y: # gone off the bottom edge?
        jump_to(x, min_Y)
    elif y < min_Y: # gone off the top edge?
        jump_to(x, max_Y)

