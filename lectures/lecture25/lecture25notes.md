# Lecture 25 Notes

An **algorithm** is a finite sequence of precise instructions that solve a
computational problem. Algorithms are one of the key ideas in computer science,
so much so that you might even say that computer science is the study of
algorithms.

In general, we want algorithms that run quickly, don't use too much memory, and
are easy to debug and understand.

In what follows, we'll study two different problems: *searching* and *sorting*.
We'll see multiple ways to solve each of these problems.

Our implementations of searching and sorting won't be as efficient as they could
be. Instead, we focus on clarity and understanding. High-performance
implementations of searching and sorting require a lot more work and are
significantly more complex.

See [searching.py](searching.py) for the code used in these notes.


## The Basic Search Problem

Suppose you have a list of values $$a_0, a_1, \ldots, a_{n-1}$$ that are all the
same type. They could be numbers, strings, letters, or lists --- *any* value
that can be compared. The **search problem** asks for an answer to this
question:

> What is the index position of an element on the list that is equal to a
> given *target value* $$x$$?

If the target value $$x$$ is nowhere on the list, then we want the search to
somehow signal that. For simplicity, we will do this by having it return the
value -1, i.e. -1 means "$$x$$ was not found".

If $$x$$ occurs more than once on the list, then we usually want the *first*,
i.e. *left-most* occurrence of $$x$$. If we want a different one, then we will
say that explicitly.

Lets look at some examples. Consider this list:

```
[3, 9, -2, 4, -2]`
```

If you want to find the position of the first -2, you can see that the left-most
-2 is at index location 2. If you want the position of 5, then the result is -1
because 5 is *not* on the list.

Or suppose we have this list:

```
['car', 'ebike', 'foot', 'scooter']`
```

If you want to know the position of `'scooter'`, the search will tell you it's
at index location 3. If you want to know the position of `'bike'`, -1 is
returned because `'bike'` is *not* in the list.


### The Linear Search Algorithm

The **linear search** algorithm is the most basic and important answer to the
search problem. It's already implemented by the built-in `index` list method:

```
>>> nums = [3, 9, -2, 4, -2]
>>> nums.index(-2)
2

>>> nums.index(5)
Traceback (most recent call last):
  File "__main__", line 1, in <module>
ValueError: 5 is not in list


>>> vehicles = ['car', 'ebike', 'foot', 'scooter']
>>> vehicles.index('scooter')
3

>>> vehicles.index('bike')
Traceback (most recent call last):
  File "__main__", line 1, in <module>
ValueError: 'bike' is not in list
```

Instead of returning -1 when it can't find the target value, `index` causes a
`ValueError` exception. In Python, **exceptions** are a general-purpose way of
signaling and handling errors, but we won't be covering them in this course.

Let's implement our own version of linear search. First, we should think of the
*algorithm* to solve the problem. This isn't too hard for linear search. To
determine if one of the values $$a_0, a_1, \ldots, a_{n-1}$$ equals $$x$$, we
will check them one at time, starting with $$a_0$$, then $$a_1$$, then $$a_2$$,
and so on. Eventually we will find a value equal to $$x$$, or prove that $$x$$
is not in the list.

```python
def linear_search(x, lst):
    """Returns the position of the left-most x in lst.
    If x is not in lst, returns -1.
    lst is assumed to be a list of values. Order doesn't matter.
    """
    i = 0
    while i < len(lst):
        if lst[i] == x: # x found at location i
            return i 
        i += 1
    return -1           # x not in lst
```

For example:

```
>>> nums = [3, 9, -2, 4, -2]
>>> linear_search(-2, nums)
2
>>> linear_search(5, nums)
-1

>>> vehicles = ['car', 'ebike', 'foot', 'scooter']
>>> linear_search('scooter', vehicles)
3
>>> linear_search('bike', vehicles)
-1
```

**Important** For linear search, *it doesn't matter what order the elements in
the list are*. Linear search works the same whether the values are in sorted
order, or in a totally random order. All that matters is that the values being
searched can be compared with `==`.


### The Reverse Linear Search Algorithm

Another way to solve the linear search problem is to check the elements of the
list going from right to left, i.e. by starting at the *end* of the list and
moving towards the start. We call this **reverse linear search**. The main
difference between it and regular linear search is that when $$x$$ occurs
multiple times in the list then reverse linear search returns the position of
the *right-most* occurrence of $$x$$. Regular linear search returns the
left-most position.

Here's an implementation of reverse linear search:

```python
def reverse_linear_search(x, lst):
    """Returns the position of the right-most x in lst.
    If x is not in lst, returns -1.
    lst is assumed to be a list of values. Order doesn't matter.
    """
    i = len(lst) - 1
    while i >= 0:
        if lst[i] == x: # x found at location i
            return i 
        i -= 1
    return -1           # x not in lst
```

For example:

```
>>> nums = [3, 9, -2, 4, -2]
>>> reverse_linear_search(-2, nums)
4                                   # different result than regular linear search
>>> reverse_linear_search(5, nums)
-1

>>> vehicles = ['car', 'ebike', 'foot', 'scooter']
>>> reverse_linear_search('scooter', vehicles)
3
>>> reverse_linear_search('bike', vehicles)
-1
```

Reverse linear search can be useful in practice. Sometimes you might know
approximately where in the list the item you're searching for might be. If it's
probably near the *end* of the list, then reverse linear search might it faster
than regular linear search. For instance, when searching for the position of the
`'.'` in a file name, it's probably faster to use reverse linear search since
the `'.'` tends to be near the end of the file name, e.g. `story.txt`,
`index.md`, `searching.py`, etc.

> **Aside** There are other ways you could do linear search. As long as you
> *check* all the items in the list, you can do that in any order that you like.
> For instance, you could:
> 
> - start in the middle, and then scan to the left, "wrapping-around" to the
>   start of the list when you hit the end
> - start in the middle and expand outwards in both left and right directions;
>   this will give you the value of $$x$$ that is closest to your starting
>   point'
> - start at both the beginning and the end, and scan inwards towards the middle
>   from both directions
>   
> In practice, you'd only use one of these other methods if you had some reason
> to think they would find $$x$$ more quickly. If you know nothing about the
> order of the elements on the list, then just use regular linear search.
``