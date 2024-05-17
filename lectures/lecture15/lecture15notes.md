## Lecture 15 Notes

Some examples of using loops.

### Example: Random Turtle Walk

In a previous lecture we saw this program for making a turtle do a "random
walk" around the screen. When the turtle hits an edge, it "wraps around" to
the opposite side of the screen ([randomWalk1.py](randomWalk1.py)):

```python
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
```

The for-loop makes the turtle move exactly 1000 times. If we wanted it to walk
*forever*, we can replace the for-loop header with a while-loop:

```python
# ...

while True:
    # ...
```


### Example: Calculating a Square Root

The easiest way to calculate a square root in Python is to use `math.sqrt`:

```python
import math

print(math.sqrt(5))  # 2.23606797749979
```

Here's another way to do it using method based on [Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method) ([squareRoot.py](squareRoot.py)):

```python
def newton_sqrt(x):
    """ Returns the square root of x, for x > 0.
    Uses Newton's method to estimate the square root.
    """
    # initial guess for the square of x is half of x
    approx = 0.5 * x

    # the expression on the right of = is a better approximation
    better = 0.5 * (approx + x / approx)

    # keep improving the approximation until no more improvements occur
    while better != approx:
        #print(f'  {approx}')
        approx = better
        better = 0.5 * (approx + x / approx)
    return approx
```

For this course, we won't worry about *why* this finds the square root, or how
the method was discovered. We use it as an example of a while-loop that is not
just a simple counting loop. 

The loop condition is `better != approx`, and ahead of time we don't how many
times the loop will iterate. So we can't write this as a for-loop.

It's instructive to uncomment the `print` statement in `newton_sqrt` to see
the intermediate values that are calculated.


### Example: Sentinel Loops

A **sentinel loop**, or **sentinel value loop**, is a loop that stops when
some final (sentinel) value is encountered. For example, this progam prints
the sum and average of the numbers entered by the user, stopping when the type
"done":

```python
count = 0
total = 0.0
num = input('Please enter a number ("done" to end): ')
while num != 'done':
    total += float(num)
    count += 1
    num = input('Please enter a number ("done" to end): ')

print()
print(f'You entered {count} numbers.')
print(f'Their total_num is {total}.')
print(f'Their average is {total / count :.2f}.')
```

In this example `'done'` is the sentinel value that makes the loop stop. The
user can enter any number of numbers.

### Example: Testing for Prime Numbers

A [prime number](https://en.wikipedia.org/wiki/Prime_number) is an integer
greater than 1 that has exactly two divisors, 1 and itself. For example, the
first few primes are 2, 3, 5, 7, 11, .... The only even prime number is 2, and
there are an infinite number of primes.

Prime numbers turn out to have [applications in computer
science](https://en.wikipedia.org/wiki/Prime_number#Other_computational_applications)
[and other
fields](https://en.wikipedia.org/wiki/Prime_number#Other_applications), and so
here we will create a function that tests if a number is prime. 

There are many algorithms that test for primes, and here we will use *simple
trial division* ([primes.py](primes.py)):

```python
def is_prime(n):
    """Returns True if n is a prime number, False if it's not.
    An integer n is prime if it's bigger than 1, and it has exactly
    two divisors, 1 and itself. The smallest prime is 2 (it's also
    the only even prime), and the next few primes are 3, 5, 7, 11.
    
    To test if a number n is prime, it checks if any of the numbers
    from 2 to n-1 divide evenly into n. If none do, then n is prime.
    This method is simple, but quite inefficient, and only useful
    for small numbers.
    """
    if n < 2: return False  # no primes are less than 2
    
    # Test if any number from 2 to n-1 divides evenly into n. If
    # any do, then n is not prime.
    for trial_divisor in range(2, n):
        if n % trial_divisor == 0:
            return False
    return True
```

See the `is_prime2` function in [primes.py](primes.py) for a more efficient
implementation of this same idea.

Another interesting function is this one, which returns a list of all the
primes less than `n`:

```python
def primes_less_than(n):
    """Returns a list of all the primes less than n.
    There are 25 primes less than 100, and 168 primes
    less than 1000.
    """
    result = []
    for n in range(n):
        if is_prime(n):
            result.append(n)
    return result
```
