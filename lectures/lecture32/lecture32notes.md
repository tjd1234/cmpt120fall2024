# Lecture 32 Notes

## Introduction

A simple way to a draw a tree is to draw the letter *V* again and again. Start
with a single line, and then draw a *V* on the end. Then on the top points of
the *V*, draw slightly smaller *V*s. Then on these draw slightly smaller *V*s
again. If you keep doing this, you end you with a tree-like shape.

In these notes, we will develop a program that simulates this drawing process. A
natural way to do this is to use recursion, because the entire tree consists of
copies of it self, but smaller.

We'll use the following helper functions in the code that follows:

```python
import turtle

def jump_to(x, y):
    """Move the turtle to the position (x, y) without drawing anything.
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def get_turtle_state():
    """Return the turtle's position and heading as a list, [(x, y), heading]
    """
    return [turtle.position(), turtle.heading()]
```


## Drawing a V Shape

The first step is to write a function that draws our *V* shape:

```python
def draw_V(x, y, size):
    """Draw a V with the bottom at (x, y).
    Returns the state of the top two points of the V.
    """
    jump_to(x, y)               # (x, y) is the bottom of the V
    turtle.left(30)
    turtle.forward(size)
    left = get_turtle_state()   # remember position and heading
    jump_to(x, y)               # go back to the bottom
    turtle.right(60)
    turtle.forward(size)
    right = get_turtle_state()  # remember position and heading
    #
    # return the position and heading of both the upper-left and upper-right
    # point of the V
    #
    return [left, right]
```

In addition to drawing a *V*-shape, with the bottom of the *V* at (x, y), this
returns a list of the state of the turtle at the top two points of the *V*. A
turtle's state consists of two things: the coordinates of the turtle on the
screen, and the direction it is facing. We return this list because later we are
going to come back and draw two more *V*s starting at those points. The lists
gives us the exact information at what position and angle to start drawing.

![diagram of a V shape](V_diagram_small.png)

## The Canopy of the Tree

Trees have at least two parts: a trunk at the bottom, and a leafy *canopy* at
the top. The trunk is a simple rectangle, but 
[for the canopy we'll use recursion](https://en.wikipedia.org/wiki/Fractal_canopy)
to draw lots and lots of *V* shapes.

```python
def canopy(x, y, size, scale = 3.0):
    #
    # add a bit of randomness to give some variety
    #
    turtle.left(random.randint(-5, 5))
    if size > 3:
        #
        # draw a V, and get the position and heading of the two points at the
        # top
        #
        left, right = draw_V(x, y, size * scale)
        
        #
        # recursively draw a V on the left point
        #
        turtle.setheading(left[1])
        left_size = random.uniform(0.8, 0.9) * size
        turtle.pensize(5 * left_size / 20)
        canopy(left[0][0], left[0][1], left_size)

        #
        # recursively draw a V on the right point
        #
        turtle.setheading(right[1])
        right_size = random.uniform(0.7, 0.9) * size
        turtle.pensize(5 * right_size / 20)
        canopy(right[0][0], right[0][1], right_size)
    else:
        if random.random() > 0.9:    # sometimes put an orange at the end of a branch
            turtle.dot(10, 'orange')
```

Notice a few things:

- The passed-in `size` says how big to make the canopy. If it's less than 3,
  then no more *V*s are drawn on that branch. Instead, either nothing is drawn,
  or an "orange" is drawn.
- The `scale` parameter controls how big the canopy is overall. Using it, you
  could, for instance, make a small-sized tree that is drawn large on the
  screen.
- Randomness is used in a couple of places to add variety, making the tree look
  different each time.
- There are lots of concrete numbers scattered throughout the function. They
  were chosen by hand, based on what looked good. You could change them and get
  very different looking trees.
- The `draw_V` function can be replaced by *any* function that draws a shape and
  returns a list of two turtle states. For instance, if you replace it with a
  different function, such as the `draw_fork` or `draw_rand` (also in
  [turtle.py](turtle.py)), you'll get quite different looking trees.


## Drawing the Entire Tree

With the `canopy` function in hand, we can now create a function that draws an
entire tree:

```python
def draw_tree(x, y, size, draw_fast=True):
    #
    # set up the turtle
    #
    if draw_fast:
        turtle.Screen().tracer(0)  # don't show any drawing on the screen

    turtle.hideturtle()

    #
    # draw the canopy
    #
    turtle.color('green')        # trees are green, right?
    turtle.setheading(90)        # trees grow upwards
    turtle.pensize(7)            # initial thickness
    canopy(x, y, size)

    #
    # draw the trunk
    #
    # done after the canopy so the trunk is drawn on top
    # 
    turtle.setheading(90)        # trees grow upwards
    turtle.pensize(15)           # trunk is thicker than the rest of the tree
    turtle.color('brown')
    trunk_len = 50               # set the trunk length
    jump_to(x, y - trunk_len)
    turtle.forward(trunk_len)    # draw the trunk

    if draw_fast:
        turtle.Screen().update() # refresh the screen to see what was drawn
```

Here is the final result:

```python
draw_tree(   0, -300, 20, 2)
draw_tree(-250,  100, 20, 2)
draw_tree( 350,  200, 20, 2)
```

![three recursive V trees](recursiveTrees_small.png)
