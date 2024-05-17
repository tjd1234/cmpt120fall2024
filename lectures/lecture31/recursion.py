# recursion.py

def f1():
    """In theory, this should loop forever an never return. But in practice Python stops
    the recursion after a certain number of calls.

    >>> f1()
    Traceback (most recent call last):
      File "/usr/lib/python3.8/doctest.py", line 1336, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.f1[0]>", line 1, in <module>
        f1()
      File "recursion.py", line 16, in f1
        f1()
      File "recursion.py", line 16, in f1
        f1()
      File "recursion.py", line 16, in f1
        f1()
      [Previous line repeated 991 more times]
    RecursionError: maximum recursion depth exceeded
    """
    f1()

def f2():
    """Similar to f1, but prints a message before each call.
    """
    print('hello!')
    f2()


count = 0
def f3():
    """This is like f2(), but prints how many times it has been called.
    """
    global count  # tell Python that count is the global variable defined outside the function
    print(f'{count}. hello!')
    count += 1
    f3()

def f4_bad():
    """A wrong way to implement f3 without using a global variable.
    """
    count = 0
    print(f'{count}. hello!')
    count += 1
    f4_bad()

def f4(count):
    """A correct way to implement f3 without using a global variable.
    """
    print(f'{count}. hello!')
    count += 1
    f4(count)

def f4_better(count):
    """A better way to implement f4.
    """
    print(f'{count}. hello!')
    f4_better(count + 1)

def f4_bad_again(count):
    print(f'{count}. hello!')
    f4_bad_again(count)  # oops: forgot the + 1


def f5_imperfect(n):
    """Prints 'hello' n times, numbered.

    >>> f5_imperfect(3)
    3. hello!
    2. hello!
    1. hello!
    """
    if n > 0:
        print(f'{n}. hello!')
        f5_imperfect(n - 1)

def f5(n):
    """Prints 'hello' n times, numbered.

    >>> f5(3)
    1. hello!
    2. hello!
    3. hello!
    """
    if n > 0:
        f5(n - 1)
        print(f'{n}. hello!')

def print_upto(n):
    """Prints the numbers from 1 to n, inclusive.

    >>> print_upto(3)
    1
    2
    3
    """
    if n > 1:
        print_upto(n - 1)
    print(n)

def print_downfrom(n):
    """Prints the numbers from n down to 1.

    >>> print_downfrom(3)
    3
    2
    1
    """
    print(n)
    if n > 1:
        print_downfrom(n - 1)

def my_range(n):
    """Returns a list of the numbers from 1 to n, inclusive.

    >>> my_range(3)
    [1, 2, 3]
    >>> my_range(1)
    [1]
    >>> my_range(0)
    []
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    else:
        return my_range(n - 1) + [n]

def say(s, n):
    """Prints s n times.

    >>> say('hello', 3)
    hello
    hello
    hello
    """
    if n > 0:
        print(s)
        say(s, n - 1)

def fill(s, n):
    """Returns a list of n copies of s.

    >>> fill('hello', 3)
    ['hello', 'hello', 'hello']
    >>> fill('hello', -9)
    []
    """
    if n <= 0:
        return []
    else:
        return fill(s, n - 1) + [s]

def sum_to_almost1(n):
    """Incorrect "transitional" function from my_range to sum_to.
    """
    if n <= 0:
        return 0
    else:
        return sum_to_almost1(n - 1) + [n]

def sum_to(n):
    """Returns the sum of the numbers from 1 to n, inclusive.

    >>> sum_to(0)
    0
    >>> sum_to(1)
    1
    >>> sum_to(3)
    6
    >>> sum_to(100)
    5050
    """
    if n <= 0:
        return 0
    else:
        return sum_to(n - 1) + n


def sum_to_mod(n):
    """Same as sum_to, but with debugging statements.
    """
    print(f'sum_to({n}) called ...')
    if n <= 0:
        print(f'sum_to({n}) returned 0')
        return 0
    else:
        result = sum_to_mod(n - 1) + n
        print(f'sum_to_mod({n}) returned {result}')
        return result

def sum_squares(n):
    """Returns the sum of the squares of the numbers from 1 to n, inclusive.

    >>> sum_squares(0)
    0
    >>> sum_squares(1)
    1
    >>> sum_squares(3)
    14
    >>> sum_squares(100)
    338350
    """
    if n <= 0:
        return 0
    else:
        return sum_squares(n-1) + n*n


def range_string(n):
    """Returns the string '1, 2, 3, 4, 5'.
   
    >>> range_string(0)
    ''
    >>> range_string(1)
    '1'
    >>> range_string(5)
    '1, 2, 3, 4, 5'
    >>> range_string(10)
    '1, 2, 3, 4, 5, 6, 7, 8, 9, 10'
    """
    if n <= 0:
        return ''
    elif n == 1:
        return '1'
    else:
        return range_string(n - 1) + ', ' + str(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
