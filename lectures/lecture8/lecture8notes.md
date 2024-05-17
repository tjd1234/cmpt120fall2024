# Lecture 8 Notes

## Functions

A **function** is a named group of statements. Functions can receive input and
return output.

For instance, this function draws a square:

```python
import turtle

def square(n):  # function header
    for i in range(4):     # function body has 3 lines
        turtle.forward(n)
        turtle.left(90)
```

Note a few things:

- `def square(n):` is called the **function header**. The three indented lines
  of code under it are called the **function body**.

- `def` is short for *definition*.

- The function's name is `square`, and it takes one input that it calls `n`.
- 
  Function names follow essentially the same rules for variable names, e.g.
  they must consist of letters, digits, and underscores, and they *can't*
  start with a digit or be the same as a Python keyword.

- A function header always ends with a `:`.

- The code in a function body must be consistently indented underneath the
  header. The indentation is how Python determine's what's in the function
  body.

- `square` takes one input value `n`, which is used in the statement
  `turtle.forward(n)`. Thus `n` must be a number. If you call, say,
  `square('two')`, then the function will crash with an error when it runs
  `turtle.forward(n)`.

- `square` does *not* return a value. Instead, it makes the turtle draw a
  picture. This is quite different than a mathematical function, which would
  always return a value.


# Function Documentation

It's often a good idea to **document** a function, i.e. to explain what it
does and how it works. For example:

```python
import turtle

def square(size):
    """ Draws a square with sides of length size.
    Assumes the turtle module has been imported.
    """
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
```

Here we've put a **doc-string** after the header and before the body, indented
the same amount as the body.

`"""` in Python are **triple quotes**, and they are useful here because they
let you write multi-line strings.

You can also put documentation before a function using source code comments:

```python
import turtle

# Draws a square with sides of length size.
# Assumes the turtle module has been imported.
def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
```

> **Practice** Write a function `triangle(size)` that, when called, draws an
> equilateral triangle with all sides of length `size`.


## Functions that Return Values

As in mathematics, Python functions can return values.

**Example** This function takes an input value (the radius of a circle), and
returns an output value (the area of the circle):

```python
def circle_area(radius):
    return 3.14 * radius ** 2
```

The `return` keyword causes the function to immediately stop, and the value of
the returned expression is the output of the function.

**Example** This function returns the sum of the numbers from 1 to $n$ using
the formula $\frac{n(n+1)}{2}$:

```python
def add_nums(n):
    """ Returns 1 + 2 + 3 + ... + n
    """
    return n * (n + 1) / 2
```

**Example** This function takes two inputs and returns a single value (the
area of the triangle):

```python
def triangle_area(base, height):
    """ Returns the area of a triangle.
    """
    return base * height / 2
```

**Example** Here's a function that returns a string:

```python
def exclaim(s, n):
  """ Returns a string with n exclamation marks after s.
  """
  return s + '!' * n
```

For instance:

```python
>>> exclaim('Yes', 5)
'Yes!!!!!'
>>> exclaim('No', 2)
'No!!'
```

### Local Variables

You can create new variables inside functions:

```python
def cube_surface_area(side):
  face = side ** 2
  return 6 * face
```

`face` is called a **local variable**, or sometimes a **temporary variable**.
It is only used inside of `cube_surface_area`. When the function ends, Python
automatically deletes `face`.

### Functions that Take No Input

Here's a function that returns a value, but doesn't take any input:

```python
import random

def roll_die():
  """ Randomly returns 1, 2, 3, 4, 5, or 6.
  """
  return random.randrange(1, 7)
```

Every time you call `roll_die()` it returns a randomly chosen value form 1 to
6:

```python
>>> roll_die()
4
>>> roll_die()
1
>>> roll_die()
6
>>> roll_die()
6
```

> **Challenge** If you roll 5 6-sided dice, what's the %-chance
> that they are all the same? Write a Python program that
> repeatedly rolls 5 6-sided dice and keeps count of
> how many times they're all the same. The number of times
> they are all the same divided the total number of rolls
> is then estimate for the answer to the question.
> 
> See [dice_experiment.py](dice_experiment.py) for a sample solution.


See [scratch.py](scratch.py) for code written in the lecture (errors and all).
