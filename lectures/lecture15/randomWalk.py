# random_walk.py

import turtle
import random

max_X = turtle.window_width() / 2
min_X = -max_X

max_Y = turtle.window_height() / 2
min_Y = -max_Y

def jump_to(x, y):
    turtle.up()
    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.goto(x, y)
    turtle.speed('normal')
    turtle.showturtle()
    turtle.down()

while True: # inifnite loop
    turtle.forward(10)

    # turn some random amount
    angle = random.uniform(-10, 10)
    turtle.left(angle)

    # "wrap-around" the screen if hit an edge
    x, y = turtle.position()
    if x > max_X:   # gone off the right edge?
        jump_to(min_X, y)
    elif x < min_X: # gone off the left edge?
        jump_to(max_X, y)
    elif y > max_Y: # gone off the bottom edge?
        jump_to(x, min_Y)
    elif y < min_Y: # gone off the top edge?
        jump_to(x, max_Y)
