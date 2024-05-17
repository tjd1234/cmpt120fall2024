# Lecture 23 Notes

## Lists are Mutable

Recall that Python strings are **immutable**, i.e. a Python string can't be
changed in any way. In contrast, Python lists are **mutable**, i.e. they can
be modified:

```
>>> s = 'apple'                                          # strings are immutable
>>> s[0] = 'A'                                           # Python won't let you 
Traceback (most recent call last):                       # modify them
  File "__main__", line 1, in <module>
TypeError: 'str' object does not support item assignment

>>> lst = [4, 1, 4, 5]   # lists are mutable (changeable)
>>> lst[0] = 'A'         # you can change values, and add/remove values
>>> lst
['A', 1, 4, 5]
>>> lst[-1] = 'Z'
>>> lst
['A', 1, 4, 'Z']
```

**Aside** You can even do *self-referential* changes like this:

```
>>> lst = [1, 2, 3]
>>> lst[1] = lst
>>> lst
[1, [...], 3]
```

The `[...]` in `[1, [...], 3]` indicates an infinite list. In practice, there
is almost never any reason to create or use self-referential lists. But they
sometimes occur as bugs, so it helpful to be aware of them.

Using slice notation, you can replace an entire slice of a list with a
different slice:

```
>>> lst = [1, 2, 3, 4, 5]
>>> lst[2:4]
[3, 4]
>>> lst[2:4] = ['a', 'b', 'c', 'd']
>>> lst
[1, 2, 'a', 'b', 'c', 'd', 5]
```

To delete a value at location `i` of a list `lst`, you can use the statement
`del lst[i]`:

```
>>> food = ['pear', 'apple', 'toast', 'cereal']
>>> del food[1]
>>> food
['pear', 'toast', 'cereal']
>>> del food[2]
>>> food
['pear', 'toast']
```

`del` can also delete a slice:

```
>>> food = ['pear', 'apple', 'toast', 'cereal']
>>> del food[1:3]
>>> food
['pear', 'cereal']
```

`del` does *not* make a copy of the list. It actually modifies --- *mutates*
--- the existing list. Once something is `del`-ed, it really is gone.


## List Aliasing

When you assign a list to a variable a copy of the list is *not* made:

```
>>> a = [1, 2, 3]      # a and b are both names for the same list
>>> b = a              # changing one of the lists changes the other
>>> a[0] = -1
>>> a
[-1, 2, 3]
>>> b
[-1, 2, 3]

>>> del b[0]
>>> a
[2, 3]
>>> b
[2, 3]
```

This behaviour can be a source of subtle bugs. You always need to be sure if
the lists you are dealing with are the same or different.

Mutability adds a level of flexibility (and complexity!) to lists that we
don't have with strings. Certain operations on lists are now very fast, e.g.
changing a value at a particular index. You can also add/remove values using
methods and functions.


## List Concatenation

If `a` and `b` are lists, then `a + b` is a new list consisting of all the
elements in `a` followed by all the elements in `b`:

```
>>> a = [1, 2]
>>> b = [5, 6, 7, 8]
>>> a + b
[1, 2, 5, 6, 7, 8]
>>> b + a
[5, 6, 7, 8, 1, 2]
```

You can concatenate a list with itself using `+`:

```
>>> a = [1, 2]
>>> a + a
[1, 2, 1, 2]
>>> a + a + a
[1, 2, 1, 2, 1, 2]
```

Or you can use this shorthand with `*`:

```
>>> a = [1,2]
>>> 2 * a
[1, 2, 1, 2]
>>> 3 * a
[1, 2, 1, 2, 1, 2]
```

## List Methods

You can get a list of all the methods that come with lists by typing
`dir([])`:

```
>>> dir([]) 
['__add__', '__class__', '__contains__', '__delattr__',
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__',
'__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
'__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
'__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy',
'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

Methods that begin with `__` are special, and we will ignore them for now.
Here are the main string methods:

```
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
'remove', 'reverse', 'sort']
```

Let's look at examples of each of these:

```
>>> lst = [1, 2, 3]       # lst.append(x) adds x onto the right end of lst
>>> lst.append('cat')
>>> lst                    
[1, 2, 3, 'cat']
>>> lst.append([4, 5])
>>> lst
[1, 2, 3, 'cat', [4, 5]]


>>> lst = [1, 2, 3]       # lst.clear() removes all values from lst
>>> lst.clear()
>>> lst
[]


>>> lst = [1, 2, 3]       # lst.copy() makes a new copy of lst
>>> lst2 = lst.copy()
>>> lst2
[1, 2, 3]
>>> lst2[0] = -1
>>> lst2
[-1, 2, 3]
>>> lst
[1, 2, 3]


>>> lst = [5, 1, [1, 2], 2, 1, 9, 0, 1]  # lst.count(x) returns the number
>>> lst.count(1)                         # of times x appears in lst
3
>>> lst.count(2)
1
>>> lst.count('shoe')
0


>>> lst = [1, 2, 3]     # lst.extend(other_lst) appends all the values in
>>> lst.extend([4, 5])  # other_lst to the right end of lst
>>> lst
[1, 2, 3, 4, 5]


>>> lst = [4, 7, 5, 4]  # lst.index(x) returns the first index i such that
>>> lst.index(4)        # lst[i] == x; causes an error if x is not in lst
0
>>> lst.index(5)
2
>>> lst.index(6)
Traceback (most recent call last):
  File "__main__", line 1, in <module>
ValueError: 6 is not in list


>>> lst = [4, 8, 9]     # lst.insert(i, x) modifies lst by inserting value x
>>> lst.insert(0, 'A')  # before lst[i]
['A', 4, 8, 9]
>>> lst.insert(0, 'B')
>>> lst
['B', 'A', 4, 8, 9]
>>> lst.insert(3, 'C')
>>> lst
['B', 'A', 4, 'C', 3, 9]


>>> lst = [1, 2, 3]    # lst.pop() returns and removes the last item of lst
>>> lst.pop()
3
>>> lst
[1, 2]
>>> lst.pop()
2
>>> lst
[1]
>>> lst.pop()
1
>>> lst
[]
>>> lst.pop()
Traceback (most recent call last):
  File "__main__", line 1, in <module>
IndexError: pop from empty list


>>> lst = [1, 2, 3]   # lst.pop(i) modifies lst by removing the item at index i
>>> lst.pop(1)
2
>>> lst
[1, 3]
>>> lst.pop(1)
3
>>> lst
[1]
>>> lst.pop(1)
Traceback (most recent call last):
  File "__main__", line 1, in <module>
IndexError: pop index out of range


>>> lst = [5, 1, [1, 2], 2, 1, 9, 0, 1]  # lst.remove(x) removes the first
>>> lst.remove(1)                        # occurrence of x in lst; causes an error
>>> lst                                  # if x is not in lst
[5, [1, 2], 2, 1, 9, 0, 1]
>>> lst.remove(1)
>>> lst
[5, [1, 2], 2, 9, 0, 1]
>>> lst.remove(1)
>>> lst
[5, [1, 2], 2, 9, 0]
>>> lst.remove(1)
Traceback (most recent call last):
  File "__main__", line 1, in <module>
ValueError: list.remove(x): x not in list


>>> lst = [1, 2, 3]     # lst.reverse() modifies lst by re-arranging all its values
>>> lst.reverse()       # into reverse order
>>> lst
[3, 2, 1]
>>> lst.reverse()
>>> lst
[1, 2, 3]

>>> lst = [5, 1, 2, 1, 9, 0, 1]  # lst.sort() modifies lst by re-arranging its values
>>> lst.sort()                   # to be in ascending sorted order (according to the
>>> lst                          # <= operator)
[0, 1, 1, 1, 2, 5, 9]
```
