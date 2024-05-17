# Lecture 5 Notes

[Turtle graphics](https://en.wikipedia.org/wiki/Turtle_graphics) is a fun and
useful way to draw pictures.

Imagine a robot turtle on a piece of paper. It can walk straight in any
direction, and it draws a line when it moves. The robot turtle follows these
basic commands:

- go forward *n* steps (where a step is usually 1 pixel on the screen); going
  forward *-n* steps makes the turtle go backwards
- turn left *d* degrees; turning right is the same as turning left *-d*
  degrees

Python comes with its own turtle graphics library, and you can use it like
this ([square1.py](square1.py)):

```python
# You must import the turtle library before using turtle graphics.
import turtle

# optionally, you can set the pen color and size
turtle.color('orange')
turtle.pensize(5)
turtle.shape('turtle')

# draw a square
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
```

A couple of notes:

- We're using simpler turtle code than used in the interactive textbook.
  Either approach is fine, but we will stick with this one since the programs
  are usually shorter.
- The statement `turtle.shape('turtle')` is for fun, and draws the turtle as a
  little turtle icon. Removing this line will draw the turtle as a triangle.

**Exercise**. Draw an *equilateral triangle* (all sides the same length) using
turtle graphics. Sample solution in [triangle1.py](triangle1.py).


## For Loops

You get a nice pattern if you draw 4 squares ([square2.py](square2.py)):

```python
import turtle

turtle.color('orange')
turtle.pensize(5)

# draw 4 identical squares to make a nice pattern
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
```

Repeating the same square-drawing code so many times is tedious and hard to
read. So instead we can use a **for-loop** to repeatedly call it
([square3.py](square3.py)):

```python
import turtle

turtle.color('orange')
turtle.pensize(5)

# the indented code below is repeated 4 times
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
```

**Exercise**. Do the same thing with the *equilateral triangle* from the
previous exercise. Sample solution in [triangle2.py](triangle2.py).


## Other Kinds of for-loops

For-loops **iterate** through the elements of a list:

```python
colors = ['orange', 'black', 'green', 'yellow']
print('My favourite colors are: ')
for c in colors:
    print("  ", c)
```

This prints:

```
My favourite colors are: 
   orange
   black
   green
   yellow
```

When used with the `range` function, a for-loop can count:

```python
for i in range(5):
    print(i, i**2)
```

This prints:

```
0 0
1 1
2 4
3 9
4 16
```

You can give `range` a starting and ending value:

```python
for i in range(2, 6):
    print(i, i**2)
```

This prints:

```
2 4
3 9
4 16
5 25
```

## General Form of For-loop

A for-loop has this general form:

```python
for i in <something>:    # for-loop header
    ... statements ...   # for-loop body
```

A few important notes:

- `i` is called the **loop variable**, or **index variable**. You can use any
  variable instead of `i`, but `i` is traditional and is short for *index*.
- `<something>` can be a list, string, or a function like `range`
- The `:` is necessary. It marks the end of the for-loop *header*, and the start
  of the statements in the *body*.
- The statements in the for-loop body must be consistently indented.


## More Turtles and For-loops

Do you see how the original square-drawing code could be shortened using a
for-loop?

```python
# You must import the turtle library before using turtle graphics.
import turtle

# optionally, you can set the pen color and size
turtle.color('orange')
turtle.pensize(5)

# draw a square
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
```

The square consists of going forward and left 4 times in a row:

```python
# You must import the turtle library before using turtle graphics.
import turtle

# optionally, you can set the pen color and size
turtle.color('orange')
turtle.pensize(5)

# draw a square
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
```

**Important** This is not *exactly* the same as the original square-drawing
code because the turtle ends up pointing east at the end of this code. In the
original, the turtle ended up facing south.

Another way to draw a square is like this:

```python
# You must import the turtle library before using turtle graphics.
import turtle

# optionally, you can set the pen color and size
turtle.pensize(5)

# draw a square
for c in ['orange', 'red', 'yellow', 'green']:
    turtle.color(c)
    turtle.forward(50)
    turtle.left(90)
```

The code in the for-loop body runs four times because there are four colors in
the list. Furthermore, the color of each side is set to a different color.


## Other Turtle Stuff

Check out the [Python turtle
documentation](https://docs.python.org/3/library/turtle.html) for many more
things you can do with turtle graphics.
