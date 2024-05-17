# Lecture 24 Notes

**Note** The actual lecture consisted of working on 
[this zero marks quiz](lecture24Quiz.pdf) for 15 minutes, followed by an in-class 
review of the solutions ([which are here](lecture24Quiz_sol.pdf)). [quiz.py](quiz.py) has
implementations of the sample solutions.

The notes below contain more examples of writing code to work with with lists.


## Looping with Lists

You can loop through the individual elements of a list with a for-loop. For
example:

```
lst = [1, 2, 3]
for x in lst:
    print(10 * x)
```

This prints:

```
10
20
30
```

You can also use while-loops:

```
lst = [1, 2, 3]
i = 0
while i < len(lst):
    print(10 * lst[i])
    i += 1
```

### Example: Counting Even Numbers in a List

Here's a function that uses the loop accumulator pattern to count the number
of *even numbers* in a list:

```python
def count_even(num_lst):
    total = 0
    for x in num_lst:
        if x % 2 == 0:
            total += 1
    return total
```

For example:

```
>>> count_even([9, 2, 4, 2, 7])
3
>>> count_even([])
0
```

### Example: Finding the Min Value of a List

The built-in function `min` returns the minimum value of a list:

```
>>> min([1, 2, 3, 0, 4])
0
>>> min(['bird', 'cat', 'owl', 'ant'])
'ant'
```

For a list of strings, `min` returns the alphabetically first item in the
list.

Let's write our own version of `min`. Assuming `lst` is a non-empty list of
numbers, one way to find the minimum element is first assume that `lst[0]` is
the minimum, and then compare that to each following element. Every time a
following element is smaller, we set it to be the new minimum. When we have
compared every element, we're guaranteed to have the minimum of the entire
list:

```python
def min_list(lst):
    """Returns the smallest element in lst.
    """
    min_so_far = lst[0]
    for x in lst:
        if x < min_so_far:
            min_so_far = x
    return min_so_far
```

For example:

```
>>> min_list([1, 2, 3, 0, 4])
4
>>> min_list(['bird', 'cat', 'owl', 'ant'])
'ant'
```

**Exercise** Create the `max_list(lst)` function, which returns the maximum
value in a list.


## Lists as Parameters: Modifying in Place

When you pass a list to a function, it's possible for the function to modify
elements on the list. For example:

```python
def abs_list(lst):
    """Applies the absolute value to all elements of lst.
    """
    for i in range(len(lst)):
        lst[i] = abs(lst[i])

    # no return needed: lst is modified "in place"
```

The list you pass into `abs_list` is actually modified:

```
>>> lst = [5, -1, 6, -5]
>>> lst
[5, -1, 6, -5]
>>> abs_list(lst)
>>> lst            # lst was changed by abs_list
[5, 1, 6, 5]
```

Note that the following style of looping *doesn't* work if you want a function
to modify a list in place:

```python
def bad_abs_list(lst):
    for x in lst:   # x is a copy of a value in the list
        x = abs(x)
```

For example:

```
>>> lst = [5, -1, 6, -5]
>>> lst
[5, -1, 6, -5]
>>> bad_abs_list(lst)
>>> lst
[5, -1, 6, -5]    # oops: no change
```


## Functions that Create Lists

Suppose you want to create the list `[0, 1, 2, 3, 4]`. It's easy to do in
Python if you know this trick:

```
>>> list(range(5))
[0, 1, 2, 3, 4]
```

If you don't know that way of creating the list, or just want to set yourself
a challenge of not using `range`, you could do "manually" like this:

```python
def my_range(n):
    """Returns [0, 1, 2, ..., n-1].
    If n is less than, or equal to, 0, [] is returned.
    """
    result = []
    i = 0
    while i < n:
        result.append(i)
        i += 1
    return result
```

For example:

```
>>> my_range(-2)
[]
>>> my_range(0)
[]
>>> my_range(1)
[0]
>>> my_range(2)
[0, 1]
>>> my_range(3)
[0, 1, 2]
>>> my_range(4)
[0, 1, 2, 3]
```

### Making a Table

Another instructive example is a function that makes a table (a *matrix*).
Consider this code:

```python
def make_table(num_rows, num_cols):
    """Returns list representing a table with num_rows and num_cols.
    All values are 0.
    """
    result = []
    for r in range(num_rows):
        row = []
        for c in range(num_cols):
            row.append(0)
        result.append(row)
    return result
```

For example:

```
>>> board = make_table(3, 3)
>>> board
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

`board` represents a 2-dimensional table, such as tic tac toe board. You can
see it more clearly if you format it like this:

```
[
  [0, 0, 0],  # row 0
  [0, 0, 0],  # row 1
  [0, 0, 0]   # row 2
]
```

In this example, `board` is a "list of lists", and you can access individual
elements using []-bracket notation. `board[r][c]` is the value in position `c`
of row `r`:

```
>>> board = make_table(3, 3)
>>> board
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> board[1][1] = 5
>>> board
[[0, 0, 0], [0, 5, 0], [0, 0, 0]]
>>> board[0][2] = 15
>>> board
[[0, 0, 15], [0, 5, 0], [0, 0, 0]]
>>> board[2][0] = 25
>>> board
[[0, 0, 15], [0, 5, 0], [25, 0, 0]]
```
