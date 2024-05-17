# Lecture 9 Notes

## The Accumulator Pattern

Suppose you want to add the numbers $1 + 2 + 3 + \ldots + 100$. The fastest
way is to use the formula $\frac{n(n+1)}{2}$. But you could also do it like
this:

```python
total = 0
for i in range(1, 101):
    total += i    # += means "add to"

print(total)
```

We call the variable `total` an **accumulator**. It starts with the value 0,
and every time through the loop we add `i` to it.

Lets write this as a function so that it works with values other than 100:

```python
def sum_to(n):
    """ Returns the sum of the numbers from 1 to n.
    Demonstrates the accumulator pattern.
    """
    total = 0
    for i in range(1, n + 1):
        total += i    # += means "add to"

    return total
```

Notice the changes:

- We name the function `sum_to`. Python already has a built-in function called
  `sum` (that works differently: it sums numbers on a list).

- Instead of `range(1, 101)`, it's `range(1, n + 1)`.

- Instead of `print(total)` at the end, it's `return total`.

- `total` is a local variable, and is automatically deleted when the function
  ends.

Now suppose you want to add the *squares* of the first $$n$$ numbers, i.e. $$1^2
+ 2^2 + \ldots + n^2$$. There is [a formula for this](https://en.wikipedia.org/wiki/Square_pyramidal_number), but lets do it with the accumulator pattern:

```python
def sum_squares(n):
    """ Returns the sum of the squares of the numbers from 1 to n.
    Demonstrates the accumulator pattern.
    """
    total = 0
    for i in range(1, n + 1):
        total += i ** 2    # += means "add to"

    return total
```

> **Challenge** Modify `sum_squares` to take two input values: a starting
> value `a`, and an ending value `b` (assume `b` is bigger than `a`). It
> should return the sum of the squares from `a` to `b`. For example,
> `sum_squares(8, 11)` returns the value of $8^2 + 9^2 + 10^2 + 11^2$.
> 
> See [sum_squares](sum_squares.py) for a sample solution.


## Functions Calling Functions

Recall the square function:

```python
import turtle

def square(n):
    for i in range(4):
        turtle.forward(n)
        turtle.left(90)
```

This function draws a flower-like shape made from squares:

```python
def draw_square_flower(n):
    for i in range(8):
        square(n)
        turtle.right(45)
```

This draws a flower of a random size:

```python
import random

def draw_random_square_flower():
    n = random.randrange(10, 50)
    draw_square_flower(n)
```

Notice that `draw_random_square_flower` takes no input and returns no output.

Finally, this draws flowers of different sizes at different positions:

```python
def flower_garden(num_flowers):
    turtle.speed('fastest')
    for i in range(num_flowers):
        draw_random_square_flower()

        # move the turtle to a new random position
        angle = random.randrange(0, 360)
        turtle.penup()
        turtle.left(angle)
        step = random.randrange(150, 200)
        turtle.forward(step)
        turtle.pendown()
```

This examples shows a common programming pattern: build a complex function
(like `flower_garden`) from calls to smaller, simpler functions.

See [scratch.py](scratch.py) for code written in the lecture (errors and all).
