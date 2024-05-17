# Lecture 31 Notes

## Overview

**Recursion** is a deep and interesting idea with many applications in computer
science, mathematics, and science. The general idea of recursion is that you can
build a *big* out of *small* things that all look the same, but at different
sizes. For example, here is a recursive picture called the [Sierpinski triangle](https://en.wikipedia.org/wiki/Sierpinski_triangle):

![Sierpinski triangle](sierpinski_triangle_small.png)

The entire picture is made of three smaller copies of the entire picture, and
each one those is made of three smaller copies, and so and so on.

Here's another example called the [Barnsley fern](https://en.wikipedia.org/wiki/Barnsley_fern):

![Barnsley Fern](Barnsley_fern_small.png)

Each leaf of the fern is made of smaller copies of the fern, again and again
until it gets so small you can't see it. This looks impressively similar to real
ferns, and so it seems that recursion is a process that nature itself sometimes
follows.

Learning recursion in programming can be tricky, so we introduce it step-by-step
in a practical way.

## Introduction to Recursion

In programming, a function is **recursive** if it calls itself. For example,
`f1` is a recursive function:

```python
def f1(n):
    f1(n)
```

When run, it should, in *theory*, loop forever and never return a value.
However, Python has a limit on how many times a function can call itself, and if
it reaches that limit, a `RecursionError` exception is raised:

```
>>> f1()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in f
  File "<stdin>", line 1, in f
  File "<stdin>", line 1, in f
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
```

A function like `f1()` that always crashes, or never ends, isn't very useful.
Here's a slightly more useful recursive function:

```python
def f2():
    print('hello!')
    f2()
```

When run, it prints `hello!` many times, and then crashes with a
`RecursionError`:

```
>>> f2()
hello!
hello!
hello!
hello!
... lots more ...
hello!

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "recursion.py", line 22, in f2
    f2()
  File "recursion.py", line 22, in f2
    f2()
  File "recursion.py", line 22, in f2
    f2()
  [Previous line repeated 992 more times]
  File "recursion.py", line 21, in f2
    print('hello!')
RecursionError: maximum recursion depth exceeded while calling a Python object
```

In theory, this should loop forever and print `'hello!'` an infinite number of
times. But in practice, computers only have a limited memory and time, so it
eventually crashes.

> **Note** From now on we'll skip writing out the Traceback message, and just
> write the `RecursionError` line.

How many times is `'hello!` printed? One way to figure this out is to print the
number of each one like this:

```python
count = 0  # count is a global variable

def f3():
    global count  # tell Python to use the global count variable
    print(f'{count}. hello!')
    count += 1
    f3()
```

It prints this:

```python
>>> f3()
1. hello!
2. hello!
3. hello!
4. hello!
... lots more ...
993. hello!
994. hello!

RecursionError: maximum recursion depth exceeded while calling a Python object
```

So we see `'hello!'` is printed 994 times before the program crashes.

A problem with `f3` is that it relies on the global variable `count`. Global
variables are generally a bad idea because other code in the program could
modify `count` in a way that makes `f3` work incorrectly. We also need the ugly
statement `global count` to tell Python that the *global* `count` defined
outside the function is the variable to use.

How could we re-write `f3` so that it doesn't use a global variable? One way
that *doesn't* work is this:

```python
def f4_bad():
    count = 0
    print(f'{count}. hello!')
    count += 1
    f4_bad()
```

`f4_bad` prints this:

```
>>> f4_bad()
0. hello!
0. hello!
0. hello!
... lots more ...
0. hello!
0. hello!

RecursionError: maximum recursion depth exceeded while calling a Python object
```

`count` is always 0 because every time you call `f4_bad`, it creates a *new*
`count` that is initialized to 0. When `count += 1` is called, that particular
value is never touched again by the function.

Instead of declaring a local variable inside the function, what if we instead
pass it as a parameter?

```python
def f4(count):
    print(f'{count}. hello!')
    count += 1
    f4(count)
```

It prints this:

```
>>> f4(0)    # must pass in the 0
1. hello!
2. hello!
3. hello!
... lots more ...
993. hello!
994. hello!

RecursionError: maximum recursion depth exceeded while calling a Python object
```

This works! Well, it still crashes, but we'll fix that in a moment. By passing
the `count` as a parameter, we are able to correctly update it.

The statement `count += 1` in `f4` is usually deleted, and instead `f4_better`
is called directly with `count + 1`:

```python
def f4_better(count):
    print(f'{count}. hello!')
    f4_better(count + 1)
```

The `+` is important in the last line. If you forget it, then `count` is never
incremented:

```python
def f4_bad_again(count):
    print(f'{count}. hello!')
    f4_bad_again(count)  # oops: forgot the + 1
```

This prints:

```
>>> f4_bad_again(0)
0. hello!
0. hello!
0. hello!
... lots more ...
0. hello!
0. hello!

RecursionError: maximum recursion depth exceeded while calling a Python object
```

## Getting Rid of the Infinite Loop

All the recursive functions above suffer from the obvious defect that they run
until they crash. We never want out code to crash.

An idea for fixing this is to pass in, as a parameter, how many times we want
the line printed. For example, we want to be able to do this:

```
>>> f5(3)
1. hello!
2. hello!
3. hello!

>>> f5(5)
1. hello!
2. hello!
3. hello!
4. hello!
5. hello!
```

We'll call the parameter being passed `n`, and treat it as the number of times
we want the line printed. If `n` is less than 1, we do nothing. If it's bigger
than 1, we will print a line and then recursively print another one, but this
time using `n - 1`:
 
```python
def f5_imperfect(n):
    if n > 0:
        print(f'{n}. hello!')
        f5_imperfect(n - 1)
```

This works, although not perfectly:

```
>>> f5_imperfect(3)
3. hello!
2. hello!
1. hello!

>>> f5(5)
5. hello!
4. hello!
3. hello!
2. hello!
1. hello!
```

The numbers are in *reverse* order. But we want them to start small and get big.
How can we fix that?

It turns out that swapping the two lines in the if-statement work:

```python
def f5_better(n):
    if n >= 0:
        f5_better(n - 1)       # call f5_better first
        print(f'{n}. hello!')  # then print
```

For example:

```
>>> f5_better(3)
0. hello!
1. hello!
2. hello!
```

This works because the *first* time `f5_better` is called, `n` is 3. That means
the `n` in the print statement is 3. So we shouldn't print it right away: we
should do all the other print statements first.

Finally, we want to start at 1, not 0. This is a small change to the print
statement:

```python
def f5(n):
    if n >= 0:
        f5(n - 1)
        print(f'{n+1}. hello!')  # n changed to n + 1
```

For example:

```
>>> f5(3)
1. hello!
2. hello!
3. hello!
```

## **Try These #1**

See [recursion.py](recursion.py) for sample solutions to these exercises.

1. Write a recursive function call `print_upto(n)` that prints the numbers from
   1 up to, and including n:
   
   ```
   >>> print_upto(4)
   1
   2
   3
   4
   ```

2. Write a recursive function call `print_downfrom(n)` that prints the numbers
   from n down to 1:
   
   ```
   >>> print_downfrom(4)
   4
   3
   2
   1
   ```

3. Write a recursive function called `my_range(n)` that returns (not prints!)
   the list `[0, 1, 3, ..., n-1]`:
   
   ```
   >>> my_range(-2)
   []
   >>> my_range(1)
   [1]
   >>> my_range(3)
   [1, 2, 3]
   ```

   If `n` is less than, or equal to, 0, return the empty list.

4. Write a recursive function called `say(s, n)` that prints the string `s` `n`
   times:
   
   ```
   >>> say('hello', 3)
   hello
   hello
   hello
   >>> say('I like cheese!', 5)
   I like cheese!
   I like cheese!
   I like cheese!
   I like cheese!
   I like cheese!
   ```

   If `n` is less than, or equal to, 0, print nothing.

5. Write a recursive function called `fill(s, n)` that returns (not prints!) a
   new list with `n` copies of `s`:
   
   ```
   >>> fill('hello', 3)
   ['hello', 'hello', 'hello']
   >>> fill('I like cheese!', 5)
   ['I like cheese!', 'I like cheese!', 'I like cheese!', 'I like cheese!', 'I like cheese!']
   ```

    If `n` is less than, or equal to, 0, return the empty list.


## Recursively Summing 1 + 2 + 3 + ... + n

Lets write a recursive function that returns the sum $$1 + 2 + 3 + \ldots + n$$.
It should work like this:

```
>>> sum_to(3)
6
>>> sum_to(5)
15
>>> sum_to(100)
5050
```

> **Note** In practice, you would never use a recursive function, or even a
> loop, to calculate $$1 + 2 + 3 + \ldots n$$. Instead, you would use the
> formula $$\frac{n(n+1)}{2}$$. So take this example for what it is, an example
> to help learn recursion.

To make this function, lets use the strategy of starting with an existing
function, and then modifying it step-by-step. The function we'll start with is
this:

```python
def my_range(n):
    """Returns [0, 1, 2, ..., n-1]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    else:
        return my_range(n - 1) + [n]
```

How can we turn this into `sum_to`? First a couple of simple things:

- We rename it to `sum_to`
- The `n <= 0` case should return 0
- We get rid if the `n == 1` special case

This gives us:

```python
def sum_to_almost1(n):
    if n <= 0:
        return 0
    else:
        return sum_to_almost1(n - 1) + [n]
```

How do we modify the last line? Think about this sum:

```
1 + 2 + 3 + ... + (n-1) + n
```

How could you describe it *recursively*? More specifically, how can you describe
the sum from 1 to `n` using the sum from 1 to some other number?

The trick is that `1 + 2 + 3 + ... + (n-1)` is what `sum_to(n-1)` returns, and
so `sum_to(n)` is equal to `n + sum_to(n-1)`:

```
  1 + 2 + 3 + ... + (n-1) + n
= (1 + 2 + 3 + ... + (n-1)) + n
= sum_to(n-1) + n
```

So:

```python
def sum_to(n):
    if n <= 0:
        return 0
    else:
        return n + sum_to(n - 1)
```

This works! It may seem like `sum_to` isn't doing anything, but if you run it
you'll see it does return the `1 + 2 + ... + n` as promised.

To get a better intuition for how `sum_to` works, here is a modified version
that prints when the function is called and when it returns:

```python
def sum_to_mod(n):
    """Same as sum_to, but with print statements.
    """
    print(f'sum_to_mod({n}) called ...')
    if n <= 0:
        print(f'sum_to_mod({n}) returned 0')
        return 0
    else:
        result = sum_to_mod(n - 1) + n
        print(f'sum_to_mod({n}) returned {result}')
        return result
```

For example:

```
>>> sum_to_mod(5)
sum_to_mod(5) called ...
sum_to_mod(4) called ...
sum_to_mod(3) called ...
sum_to_mod(2) called ...
sum_to_mod(1) called ...
sum_to_mod(0) called ...
sum_to_mod(0) returned 0
sum_to_mod(1) returned 1
sum_to_mod(2) returned 3
sum_to_mod(3) returned 6
sum_to_mod(4) returned 10
sum_to_mod(5) returned 15
15
```

Notice a couple of things:

- The first function call, `sum_to_mod(5)`, is the *last* one to return.
- All the functions are called, and then after that they all return (in reverse
  order to which they were called).
- The first 6 function calls are stored in memory, and that takes up memory
  space (and time). So just after `sum_to_mod(0) called ...` is printed, a copy
  of all the numbers from 1 to n are stored, as parameters, inside the function
  calls. If `n` is big, this could be a significant waste of time and memory.

In *practice*, recursion is *not* a common technique because it typically uses
more time and memory than equivalent loop versions. Recursion can be a useful
problem-solving tool in some situations, e.g. we saw that *mergesort* used
recursion in a pretty efficient way.

In *theory*, however, recursion is an extremely important idea, and in fact can
be used as the basis for pretty much all computation. Any program that uses
loops can be rewritten using just recursion instead --- although the resulting
code might be slower, or use more memory, or be harder to understand.

## **Try These #2**

See [recursion.py](recursion.py) for sample solutions to these exercises.

6. Write a recursive function called `sum_squares(n)` that returns the sum of
   the squares of the numbers from 1 to `n`, e.g. $$1^2 + 2^2 + \ldots + n^2$$:
   
   ```
   >>> sum_squares(3)    
   14
   >>> sum_squares(5)
   55
   >>> sum_squares(100)
   338350
   ```

   If `n` is less than, or equal to, 0, return 0.

7. Write a recursive function called `range_string(n)` that returns a *string*
   containing the numbers from 1 to `n` separated by commas:
   
   ```
   >>> range_string(0)
   ''
   >>> range_string(1)
   '1'
   >>> range_string(5)
   '1, 2, 3, 4, 5'
   >>> range_string(10)
   '1, 2, 3, 4, 5, 6, 7, 8, 9, 10'
   """
   ```

   If `n` is less than, or equal to, 0, return the empty string.
