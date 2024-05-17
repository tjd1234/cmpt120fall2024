# Lecture 20 Notes

## Negative Indices

If `s` is a non-empty string, then `s[len(s)-1]` is it's last character. The
index `len(s)-1` is long and easy to mistype. So Python lets you write `s[-1]`
instead. For any non-empty string `s`, `s[-1]` is its last character, `s[-2]`
is its second to last character, `s[-3]` is its third to last character, and
so on.

So every character of a Python string has both a negative index and a
non-negative index:

```
      -5    -4    -3    -2    -1
       0     1     2     3     4
    +-----+-----+-----+-----+-----+
 s  | 'a' | 'p' | 'p' | 'l' | 'e' |
    +-----+-----+-----+-----+-----+
     s[0]  s[1]  s[2]  s[3]  s[4]
     s[-5] s[-4] s[-3] s[-2] s[-1] 
```

For example:

```
>>> s = 'apple'
>>> s[-1]
'e'
>>> s[-2]
'l'
>>> s[-3]
'p'
>>> s[-4]
'p'
>>> s[-5]
'a'
>>> s[-6]
Traceback (most recent call last):
  File "__main__", line 1, in <module>
IndexError: string index out of range
```

In practice, negative indexing is often used to access characters near the
right end of the string. It's not usually used for characters near the
beginning.

**Question** If `s` is a non-empty string, is `s[-len(s)]` the *first*
character of `s`?


### Example: Pluralizing a String

Here's a simple rule for pluralizing English words:

- If the word ends with an *s*, then do nothing (we assume it's already
  pluralized). For example, *birds* becomes *birds*.
- If the word *doesn't* end with an *s*, then add an *s* to the end of it. For
  example, *toy* becomes *toys*.

Note that these rules sometimes make mistakes. For example, they says the
plural of *try* is *trys*, but the correct plural is *tries*. We'll ignore
this and implement the rule as given:

```python
def pluralize(word):
    """Adds an 's' to the end of word, if needed. 
    If it already ends with an 's', then it is returned
    unchanged.
    """
    if word == '': return s
    if word[-1] == 's':
        return word
    else:
        return word + 's'
```

For example:

```
>>> pluralize('toy')
'toys'
>>> pluralize('toys')
'toys'
```

### String Slicing

**String slicing** is a generalization of string indexing that lets you get an
entire substring from within a string, instead of just a single character. For
example:

```
>>> s = 'apple'
>>> s[1:3]
'pp'
```

`s[1:3]` is a **string slice**, and it refers to the sequence of characters in
`s` that *start* at index location 1, and end at index location 3 (not 2!).
Here are a few more examples:

```
>>> s[0:4]
'appl'
>>> s[3:6]
'le'
>>> s[0:1]
'a'
>>> s[1:2]
'p'
>>> s[2:3]
'p'
>>> s[3:4]
'l'
>>> s[4:5]
'e'
```

Notice that in the slice `s[4:5]` the value 5 is *not* a valid index for `s`,
i.e. `s[5]` causes an out of range error. But it is okay to use it as the
second number in a slice. In fact, this second number in a slice can be any
number bigger than the string length without causing an out of range error:

```
>>> s[4:5]
'e'
>>> s[4:6]
'e'
>>> s[4:7]
'e'
>>> s[4:500]
'e'
```

You can also do slicing with negative indices, but we will not cover that in
these notes. While slicing with negative indices is occasionally useful, they
can be tricky expressions that are hard to understand.

In general, for a non-empty string `s`, a string slice has the form
`s[begin:end]`. The *first* character of the slice is `s[begin]`, and the
*last* character of the slice is `s[end-1]` (*not* `s[end]`). `begin` should
be a valid (non-negative) index for `s`, and `end` either a valid
(non-negative) index *or* equal to the length of the string. Also, the length
of the slice `s[begin:end]` is `end - begin`. In other words,
`len(s[begin:end]) == (end - begin)`

As with indexing, since strings are immutable (i.e. not changeable), you
*cannot* assign a string to a slice:

```
>>> s = 'apple'
>>> s[1:3] = 'dd'
Traceback (most recent call last):
  File "__main__", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

There are a couple of short-cut expressions for string slicing:

```
>>> s = 'apple'

>>> s[0:3]
'app'
>>> s[:3]   # same as s[0:3], 0 is optional
'app'

>>> s[3:5]
'le'
>>> s[3:]   # same as s[3:5], 5 is optional
'le'

>>> s[3:] + s[:3]
'leapp'

>>> s[:]    # makes a copy of s
'apple'
```

Slices have an optional third argument called `step` that can skip characters.
For example:

```
>>> s = '012345678'
>>> s[2:8]
'234567'
>>> s[2:8:2]  # every 2nd character starting at 2, and less than 8
'246'
>>> s[2:8:3]  # every 3rd character starting at 2, and less than 8
'25'
>>> s[2:8:4]  # every 4th character starting at 2, and less than 8
'26'
```

Slices with a step don't appear often in most Python programs. A common use of
the step parameter is to reverse a string:

```
>>> s = 'apple'
>>> s[::-1]   # reverses s
'elppa'
>>> 'star loop'[::-1]
'pool rats'
```

`[::-1]` isn't very readable notation, but it is short and can be a convenient
way to reverse a string if you can remember it.

**Trivia** `[::-1]` applied twice gives you the original string:

```
>>> 'hamburger'[::-1][::-1]
'hamburger'
```

**Challenge** A simple kids game is to take a person's first and last name,
and then swap the first letter of each to get a new name (which hopefully
sounds funny). For example, "Bill Gates" becomes "Gill Bates", and "Justin
Trudeau" becomes "Tustin Jrudeau".

Write a function called `name_change(first, last)` that does this:

```
>>> name_change('Bill', 'Gates')
'Gill Bates'
>>> name_change('Elon', 'Musk')
'Mlon Eusk'
>>> name_change('Justin', 'Trudeau')
'Tustin Jrudeau'
```

Here's a possible solution:

```python
def name_change(first, last):
    new_first = last[0] + first[1:]
    new_last = first[0] + last[1:]
    return new_first + ' ' + new_last
```

### The in and not in Operators

It's easy to test if a string contains, or doesn't contain, a particular
substring:

```
>>> 'off' in 'post office'
True
>>> 'to' in 'post office'
False

>>> 'm' in 'Computer'
True
>>> 'm' not in 'Computer'
False

>>> 'CPU' in 'Computer'
False
>>> 'CPU' not in 'Computer'
True
```

`in` and `not in` only tell you if a substring is in a string or not. If it is
in the string, they don't say where in the string. For that you need to use a
string method such as `find`, discussed in the next section.


### Example: Testing if a String is Formatted like an Integer

Here's some code from earlier in the course that tests if a string is
formatted like a *non-negative* integer:

```python
def is_digit(s):
    """Returns True if string s is a digit, False otherwise.
    """
    if len(s) == 1 and s in '0123456789':
        return True
    else:
        return False

def is_positive_int(s):
    """Returns True if string s is formatted like a positive int.
    Otherwise it returns False.
    """
    # if s is the empty string, return False immediately
    if s == '': return False
        
    for c in s:
        if not is_digit(c):
            return False
            
    return True
```

How can we test if a string is formatted like a *negative* integer? For
example, `'-8851'` is a negative integer. It starts with a `-`, and is
followed by a positive integer. So we can write this function:

```python
def is_negative_int(s):
    """Returns True if string s is formatted like a negative int.
    Otherwise it returns False.
    """
    if s == '':
    	return False
    elif s[0] == '-' and is_positive_int(s[1:]):
        return True
    else:
        return False
```

For example:

```
>>> is_negative_int('-3292')
True
>>> is_negative_int('3292')
False
>>> is_negative_int('-')
False
```

Now we can combine them to check if a string is formatted like an `int`,
positive, negative, or 0:

```python
def is_int(s):
    """Returns True if string s is formatted like an int, otherwise False.
    """
    return is_positive_int(s) or is_negative_int(s)
```

```
>>> is_int('0')
True
>>> is_int('-0')
True
>>> is_int('4390')
True
>>> is_int('-4390')
True
>>> is_int('--4390')
False
```
