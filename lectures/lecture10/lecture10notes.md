# Lecture 10 Notes

## Calling a main() Function

It's traditional to call the first function of your program `main`. In C++ and
Java, for example, you *must* have a function called `main` in every program.

Python doesn't *require* a `main()` function, but it's usually a good idea to
have one because it tells people where to start reading your code. Python
programs can consist of hundreds of functions, and agreeing that `main()` is
the first function called makes it easier to read.

Consider this program:

```main
name = 'Bob'
age = 20
gpa = 3.09

print('Student:', name)
print('Age:', age)
print('GPA:', gpa)
```

Here it is re-written using a `main()` function:

```main
def main():
    name = 'Bob'
    age = 20
    gpa = 3.09

    print('Student:', name)
    print('Age:', age)
    print('GPA:', gpa)
```

To run this program you need to type `main()`.

The variables `name`, `age`, and `gpa` are *local variables*, i.e. they exist
only inside `main`. When `main` ends the variables are automatically deleted.
When the variables were not in a function, they were *global variables*, which
means *any* Python code could read/write them. In general, global variables
are bad because it is hard to keep track of when and how they're modified.


## Example: Re-writing Euclid's GCD Algorithm

Earlier in the course we saw this program for calculating the [greatest common
divisor (GCD)](https://en.wikipedia.org/wiki/Greatest_common_divisor) of two
numbers:

```python
# euclid.py

# get the input numbers from the user (as strings)
a = input('What is a? ')
b = input('What is b? ')

# convert the strings to integers
a = int(a)
b = int(b)

# find the greatest common divisor
while a != b:
    print(a, b)  # see how and a and b change
    if a > b:
        a = a - b
    else:
        b = b - a

# print the result
print("greatest common divisor:", a)
```

See [euclid.py](euclid.py).


Lets re-structure it using functions.

First, it asks the user to enter a number, which is read as a string and then
converted to an `int`. Let's make a function to do that:

```python
def get_int(prompt):
    result = input(prompt)
    result = int(result)
    return result
```

> **Challenge** Re-write `get_int` so it uses only one statement: a single
> `return`.

Now we can get `a` and `b` like this:

```python
a = get_int('What is a? ')
b = get_int('What is b? ')
```

This is both shorter, and more readable: the names of the function say what is
happening. Plus you can save `get_int` to re-use in other programs.

Second, let's put the GCD algorithm in its own function:

```python
def gcd(a, b):
    """ Returns the greatest common divisor of a and b.
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    # a == b at this point
    return a
```

For example:

```python
>>> gcd(1345, 9038)
1
>>> gcd(2751, 19038)
3
```

With these functions, the original program can be written like this:

```python
a = get_int('What is a? ')
b = get_int('What is b? ')
print("greatest common divisor:", gcd(a, b))
```

> **Challenge** Re-write this program so it uses no variables, and has only
> one statement: a single call to `print`.

This is the code we want to run first, so we can put it in a main function:

```python
# euclid2.py

def main():
    a = get_int('What is a? ')
    b = get_int('What is b? ')
    print("greatest common divisor:", gcd(a, b))

def get_int(prompt):
    result = input(prompt)
    result = int(result)
    return result

def gcd(a, b):
    """ Returns the greatest common divisor of a and b.
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    # a == b at this point
    return a
```

See [euclid2.py](euclid2.py).

The `main()` function is short and simple, and in some cases that may be all
you need to read. If you need more details about `get_int` or `gcd`, you can
read those next.


## Example: Least Common Multiple (LCM)

As another example of using functions, let's create a Python function that calculates the [least common multiple](https://en.wikipedia.org/wiki/Least_common_multiple), or [LCM](https://en.wikipedia.org/wiki/Least_common_multiple), or two integers. 

For example, the least common multiple of 4 and 6 is 12, and the least common
multiple of 10 and 24 is 120.

We can calculate the LCM with this formula:

$$\mathrm{lcm}(a, b) = \frac{|ab|}{\mathrm{gcd}(a, b)}$$

Converting this Python:

```python
def lcm(a, b):
    """ Returns the lowest common multiple of a and b.
    Assumes a and b are both ints.
    """
    return abs(a * b) // gcd(a, b)  # // is integer division
```

Now we could re-write `main` from above like this:

```python
def main():
    a = get_int('What is a? ')
    b = get_int('What is b? ')
    print("greatest common divisor:", gcd(a, b))
    print("  least common multiple:", lcm(a, b))
```
