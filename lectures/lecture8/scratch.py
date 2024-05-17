# scratch.py

import turtle
import random

def square(n):  # function header
    """ Draws a square with each side of length n.
    Assumes turtle is imported.
    """
    for i in range(4):
        turtle.forward(n)
        turtle.left(90)

def square_flower(n):
    for i in range(8):
        square(n)
        turtle.right(45)

def random_square_flower():
    r = random.randrange(10, 101)
    square_flower(r)

#random_square_flower()
#random_square_flower()

colors = ['red', 'green', 'blue', 'yellow', 'orange']

def flower_garden(num_flowers):
    turtle.speed('fastest')
    for i in range(num_flowers):
        col = random.choice(colors)
        turtle.color(col)
        random_square_flower()

        angle = random.randrange(0, 360)
        step = random.randrange(150, 200)
        turtle.up()
        turtle.left(angle)
        turtle.forward(step)
        turtle.down()

flower_garden(10)

def triangle(n):
    """ Draw an equilateral triangle of side length n.
    Assumes turtle is imported.
    """
    for i in range(3):
        turtle.forward(n)
        turtle.left(120)

def circle_area(radius):
    return 3.14 * radius ** 2

def sum_to(n):
    """ Returns 1 + 2 + 3 + ... + n.
    Assumes n >= 1.
    """
    return n * (n + 1) / 2

def exclaim(s, n):
    return s + n*'!'

def cube_surface_area(side):
    face = side ** 2  # local variable
    return 6 * face

def roll_die():
    return random.randrange(1, 7)
