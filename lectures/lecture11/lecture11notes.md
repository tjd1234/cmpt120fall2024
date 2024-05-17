# Lecture 11 Notes

## Boolean Values

Python has a very useful type called `bool` that represents *true* and *false*
values. The two `bool` types are `True` and `False`. We call these **boolean
values**, or **booleans** for short.

```python
>>> type(True)
<class 'bool'>
>>> True
True
>>> False
False
```

Note:

- *Capitals matter*: `True` is a boolean value, but `true` is the name of a
  variable.
- `True` and `False` are *not* strings (they don't begin/end with quotes).


## Building Boolean Expressions with Relational Operators

The `==` operator tests for *equality*. For example:

```python
>>> 5 == 5
True
>>> 5 == 6
False

>>> 'Cat' == 'Cat'
True
>>> 'cat' == 'Cat'
False

>>> [1,6,3] == [1,6,3]
True
>>> [1,6,3] == [1,3,6]
False

>>> True == True
True
>>> False == True
False
>>> True == False
False
>>> False == False
True
```

**Question** Why does Python use `==` for equality instead of `=`, as in
mathematics?

The `!=` operator tests if two values are *not equal*:

```python
>>> 5 != 5
False
>>> 5 != 6
True

>>> 'Cat' != 'Cat'
False
>>> 'cat' != 'Cat'
True

>>> [1,6,3] != [1,6,3]
False
>>> [1,6,3] != [1,3,6]
True

>>> True != True
False
>>> False != True
True
>>> True != False
True
>>> False != False
False
```

In general, if `a == b` is *true*, then `a != b` is *false*. And vice-versa:
if `a != b` is *true*, then `a == b` is *false*. In general, `a == b` and `a
!= b` are always different, which means the expression `(a == b) != (a != b)`
is *always* true.

Expressions of the form `x == y` or `x != y` are examples of **boolean
expressions**, i.e. expressions that evaluate to a `bool`.

You can test if values are *less than* or *greater than* each other using
these operators:

```python
x < y    # true if x is less than y, and false otherwise
x <= y   # true if x is less than, or equal to, y, and false otherwise

x > y    # true if x is greater than y, and false otherwise
x >= y   # true if x is greater than, or equal to, y, and false otherwise
```

Like `==` and `!=`, these operators work with both numbers and strings (and
lists as well, but we'll rarely, if ever use them for lists):

```python
>>> 5 < 9
True
>>> 9 < 5
False
>>> 5 < 5
False
>>> 'ant' < 'zebra'  # when a and b are strings, a < b returns true
True                 # if the string in a comes before the string in b
>>> 'zebra' < 'ant'  # alphabetically
False
>>> 'ant' < 'ant'
False

>>> 5 <= 9
True
>>> 9 <= 5
False
>>> 5 <= 5
True
>>> 'ant' <= 'zebra'
True
>>> 'zebra' <= 'ant'
False
>>> 'ant' <= 'ant'
True
```

As mentioned above, when you compare *strings* with `<` or `<=`, then Python
checks *alphabetical order*.

We leave examples of `>` and `>=` as an exercise for the reader. They are like
`<` and `<=` in the obvious way.


## Logical Operators

If `a` and `b` are both boolean expressions (or boolean values), we can use
the following **logical operators** to combine them into bigger expressions:

```python
a and b   # true just when both a and b are true; false otherwise
a or b    # true when one, or both, of a and b are true; false otherwise
not a     # true if a is false, and false if a is true
```

For example, the boolean expression `2 < 5 and 'cat' == 'cat'` evaluates to
`True` because `2 < 5` is `True` and `'cat' == 'cat'` is `True`.

The boolean expression `'dog' < 'dog' and 1 <= 100` is `False` because the
expression `'dog' < 'dog'` is `False`. An expression of the form `a and b` is
only true when *both* `a` and `b` are true.

However, if the boolean expression `'dog' < 'dog' or 1 <= 100` is `True`
because `1 <= 100` is `True`. An expression of the form `a or b` is `True`
when just `a` is `True`, or just `b` is `True`, or when both `a` and `b` are
`True`.

**Question** If the boolean expression `a and b` is `True`, does that mean
that the expression `a or b` is also `True`?

**Question** Is it correct to say that the boolean `a or b` is `False`, just
when both `a` and `b` are `False`?

Here are some examples of boolean expressions using `not`:

- `not True` evaluates to `False`
- `not False` evaluates to `True`
- `not (3 == 3)` evaluates to `False`. That's because `3 == 3` evaluates to
  `True`, and `not` "flips" it to return the opposite boolean value.
- `not (3 != 3)` evaluates to `True`. That's because `3 != 3` evaluates to
  `False`, and `not` "flips" it to return the opposite boolean value.
- `not (not True)` evaluates to `True`
- `not (not False)` evaluates to `False`
- `not (not ('box' < 'shoe'))` evaluates to `True`

**Question** Do the boolean expressions `p` and `not (not p)` *always*
evaluate to the same boolean value?

Note that the boolean expression `a != b` is logically equivalent to `not (a
== b)`, i.e. both expressions always evaluate to the same value. In other
words, this expression is always true: `(a != b) == (not (a == b))`.

Mixing and matching `and`, `or`, and `not` lets us create a huge variety of
different boolean expressions.

**Example** Suppose `4 <= 5` evaluates to `True`. Using `or`, we could write
it as the logically equivalent expression `4 < 5 or 4 == 5`. `4 < 5 or 4 == 5`
evaluates to `True` because `4 < 5` is `True`. An expression of the form `a or
b` is true when at least `a` is `True`, or `b` is `True`, or both `a` and `b`
are `True`.

**Question** Suppose you know for a fact that the boolean expression `a`
evaluates to `True`, but you don't know what `b` evaluates to. Can you
conclude that `a or b` evaluates to `True`?

**Question** Suppose you know for a fact that the boolean expression `a`
evaluates to `False`, but you don't know what `b` evaluates to. Can you
conclude that `a and b` evaluates to `False`?

You can use variables with boolean expressions. For example, if `n` has the
value 5, then the expression `n == 4 and n < 10 ` evaluates to `False`.

**Example** Suppose `n` is a variable that has been set to some integer value,
but we don't know what it is. What is a boolean expression that evaluates to
`True` when `n` is 4 or 6, `False` for every other value of `n`?

This expression works: `n == 4 or n == 6`. But this expression **does not
work**: `n == 4 or 6`. `n == 4 or 6` is equivalent to `(n == 4) or 6`, which
is not a sensible boolean expression, although Python often will return a
value for it (but maybe not the value you think):

```python
>>> n = 5
>>> n == 4 or 6
6                    # ???
```

**Question** Suppose `a`, `b` and `c` are variables that have been assigned
integers, but we don't know which integers. What is a boolean expression that
evaluates to `True` just when `a`, `b`, and `c` are in increasing order.

**Answer** An expression that works is this: `a < b and b < c`. Or, depending
on the exact circumstances, `a <= b and b <= c` might be better.

This kind of expression is so common that Python also lets you write this: `a
< b < c`, or `a <= b <= c`.

**Question** Suppose `a`, `b` and `c` are variables that have been assigned
integers, but we don't know which integers. What is a boolean expression that
evaluates to `True` just when `a`, `b`, and `c` all have the same value.

**Answer** expression that works is this: `a == b and b == c`.

**Question** Re-do the previous question, but this time write a boolean
expression that evaluates to `True` just when `a`, `b`, and `c` are all
different.

**Answer** An expression that works is this: `a != b and a != c and b != c`.
