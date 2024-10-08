import turtle
import math

def polyline(n, length, angle):
    for i in range(n):
        turtle.forward(length)
        turtle.left(angle)
        
##polyline(25, 100, 100)

def arc(radius, angle):
    arc_len = 2 * math.pi * radius * (angle / 360)
    n = 30
    side_len = arc_len / n
    step_angle = angle / n
    polyline(n, side_len, step_angle)


arc(100, 270)


def polygon(num_sides, length):
    """Draw a regular polygon with num_sides
    each of the given length.
    """
    angle = 360 / num_sides
    polyline(num_sides, length, angle)
    
##    angle = 360 / num_sides
##    for i in range(num_sides):
##        turtle.forward(length)
##        turtle.right(angle)

def circle(radius):
    """Draw a circle of a given radius.
    """
    circumference = 2 * math.pi * radius
    num_sides = 30
    side_len = circumference / num_sides
    polygon(num_sides, side_len)
    
##circle(25)
##circle(50)
##circle(100)
##circle(500)

# square
def square(size):
    polygon(4, size)

##for i in range(10):
##    square(20 * i)


# triangle
def triangle(size):
    polygon(3, size)

##for i in range(10):
##    triangle(20 * i)

# star
def star(size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

##for i in rangege(10):
##    star(20 * i)



##polygon(3, 100)
##polygon(4, 100)
##polygon(5, 100)
##polygon(6, 100)
##polygon(7, 100)
