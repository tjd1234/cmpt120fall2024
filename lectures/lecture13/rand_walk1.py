# rand_walk1.py

#
# The turtle does a "random walk" across the screen. It's possible for
# the turtle to walk off the screen and disappear.
#
# random.uniform(a, b) returns a random float from a to b.
#

import turtle
import random

def jump_to(x, y):
    """ Move turtle to (x, y) without drawing a line.
    """
    #turtle.up()
    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.goto(x, y)
    turtle.speed('normal')
    turtle.showturtle()
    #turtle.down()

#for n in range(1000):
while True:
    turtle.forward(10)
    angle = random.uniform(-10, 10)
    turtle.left(angle)

    # check for edge collisions
    x, y = turtle.position()
    if x >= 400:  # off right edge?
        #h = turtle.heading()
        turtle.left(180)
        print('Hit right edge')
    elif x <= -400:  # off left edge?
        turtle.left(180)
        print('Hit left edge')
    elif y >= 400:   # off top edge?
        turtle.left(180)
        print('Hit top edge')
    elif y <= -400:  # off bottom edge?
        turtle.left(180)
        print('Hit bottom edge')
