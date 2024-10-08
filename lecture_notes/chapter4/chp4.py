import turtle
import math

def polygon(n, side_len):
    angle = 360 / n
    for i in range(n):
        turtle.forward(side_len)
        turtle.left(angle)

def circle(radius):
    circumference = 2 * math.pi * radius
    num_sides = 40
    side_len = circumference / num_sides
    polygon(num_sides, side_len)

circle(50)
circle(100)
circle(150)
circle(200)


# draw a square
def square(side_len):
    polygon(4, side_len)


# draw a triangle
def triangle(side_len):
    polygon(3, side_len)


# draw a 5-pointed star
def star(side_len):
    for i in range(5):
        turtle.forward(side_len)

