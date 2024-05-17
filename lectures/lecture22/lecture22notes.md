# Lecture 22 Notes

## List Basics

A **list** is a sequence of 0 or more Python values. The values can be of any
type, and don't necessarily need to be all the same. 

**List literals** are start with a `[` and end with `]`, and values are
separated by commas. For example:

```
[]                # the empty list, length 0
[5]
[5, 10, 5]
['hot', 'cold', 'warm', 'dry']
[5, 'five', 5.5]  # lists can contain different types of values
[[1,2], [3,4,5]]  # lists can contain lists
```

`[]` is the empty list, i.e a list of length 0 that has no values.

Recall that a **string** is a sequence of 0 or more *characters*. But a string
is *not* a list:

```
'apple'                     # a string
['a', 'p', 'p', 'l', 'e']   # a list of strings
```

> **Note** Python allowing lists to contain *any* type of value is somewhat
> unusual. In C++, for example, lists can only contain values of the same
> type. In practice, it's not very common to have different types of values on
> the same Python.

The `len(lst)` function returns the **length** of a list:

```
>>> len([])
0
>>> len([5])
1
>>> len(['hot', 'cold', 'warm', 'dry'])
4
>>> len([[1,2], [3,4,5]])
2
>>> len([[[]]])
1
```


## List Indexing

Lists follow the same indexing conventions as for strings. If `lst` is a list,
then `lst[i]` is the value at index position `i`. As with strings, the first
index of a list is always 0, i.e. Python lists used **0-based indexing**.

```
>>> scores = [0.88, 0.86, 0.91]
>>> scores[0]
0.88
>>> scores[1]
0.86
>>> scores[2]
0.91
>>> scores[3]
Traceback (most recent call last):
  File "__main__", line 1, in <module>
IndexError: list index out of range
```

If `lst` is a non-empty list, then `lst[0]` is the first element, and
`lst[len(lst)-1]` is the last element. The last element is at index location
`len(lst) - 1`, and not just `len(lst)`, because the first index is at 0.

If you have lists with lists, then you can get expressions with multiple
indices:

```
>>> table = [[5, 6], [2, 1], [3, 9], [10, 4]]

>>> table[1]
[2, 1]
>>> table[1][0]
2
>>> table[1][1]
1

>>> table[2]
[3, 9]
>>> table[2][0]
3
>>> table[2][1]
9
```

Or strings within lists:

```
>>> words = ['yes', 'no', 'maybe']

>>> words[0]
'yes'
>>> words[0][0]
'y'

>>> words[2]
'maybe'
>>> words[2][3]
'b'
```

## Negative List Indexing

Just as with strings, you can use negative indices to access the elements of a
list. This is useful when you want to access items near the end of the list:

```
>>> lst = [9, 3, 4, 2]
>>> lst[-1]
2
>>> lst[-2]
4
>>> lst[-3]
3
>>> lst[-4]
9
>>> lst[-5]
Traceback (most recent call last):
  File "__main__", line 1, in <module>
IndexError: list index out of range
```

In general, if `lst` is a non-empty list, then `lst[-1]` is the last element,
`lst[-2]` is the second to last element, and so on down to `lst[-len(lst)]`
(the first element of the list).


## List Membership

You can test if a list contains a particular value using the `in` and `not in`
operators:

```
>>> ages = [3, 4, 3, 3, 2]

>>> 1 in ages
False
>>> 2 in ages
True
>>> 3 in ages
True
>>> 5 in ages
False

>>> 1 not in ages
True
>>> 2 not in ages
False
>>> 3 not in ages
False
>>> 5 not in ages
True
```

Be careful with lists within lists:

```
>>> lst = [1, [2, 3], 4]

>>> 1 in lst
True
>>> 2 in lst
False
>>> 3 in lst
False
>>> [2, 3] in lst
True

>>> 1 not in lst
False
>>> 2 not in lst
True
>>> 3 not in lst
True
>>> [2, 3] not in lst
False
```

## List Slicing

The syntax for getting a slice of a list is the same as for strings. In
general, if `lst` is a list and `begin` and `end` are non-negative integers,
then `lst[begin:end]` is a new list consisting of all the elements from
`lst[begin]` to `lst[end-1]`. If `end` is `len(lst)` or bigger, then the slice
goes up to just the end of the list.

For example:

```
>>> lst = [9, 4, 3, 8, 2]
>>> lst[2:4]
[3, 8]
>>> lst[1:4]
[4, 3, 8]
>>> lst[1:5]
[4, 3, 8, 2]
>>> lst[1:700]
[4, 3, 8, 2]
```

If you leave out the `begin` value, then Python assumes it is 0. If you leave
out the `end` value, Python assumes it is `len(lst)`:

```
>>> lst = [9, 4, 3, 8, 2]
>>> lst[:4]
[9, 4, 3, 8]
>>> lst[4:]
[2]
```

If you leave out both `begin` and `end`, you get a new copy of the entire
list:

```
>>> lst = [9, 4, 3, 8, 2]
>>> lst2 = lst[:]
>>> lst2
[9, 4, 3, 8, 2]
```
