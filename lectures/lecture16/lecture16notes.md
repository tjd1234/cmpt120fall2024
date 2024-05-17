## Lecture 16 Notes

More examples of using loops.

### Example: Checking if a String is a Positive Integer

Let's write a function that tests if a string is formatted like a *positive*
integer:

```
>>> is_positive_int('9033')
True
>>> is_positive_int('0003920')
True
>>> is_positive_int('-5')
False
>>> is_positive_int('81.02')
False
>>> is_positive_int('tree bark')
False
```

Intuitively, a valid string is a sequence of 1, or more, digits. So first lets
write a function that tests if a string is a digit:

```python
def is_digit(s):
    """Returns True if string s is a digit, False otherwise.
    """
    if len(s) == 1 and s in '0123456789':
        return True
    else:
        return False
```

For example:

```
>>> is_digit('9')
True
>>> is_digit('E')
False
>>> is_digit('89')
False
```

The expression `s in '0123456789'` evaluates to `True` when `s` is a string
that appears sequentially in `'0123456789'`:

```
>>> '6' in '0123456789'
True
>>> '678' in '0123456789'
True
>>> '679' in '0123456789'
False
>>> '' in '0123456789'
True
```

So to test of `s` is a digit, we must check *both* that it's in
`'0123456789'`, and also that it's length is 1.

**Aside** `is_digit` can be more compactly written with a single `return`
statement:

```python
def is_digit(s):
    """Returns True if string s is a digit, False otherwise.
    """
    return len(s) == 1 and s in '0123456789'
```

Using `is_digit`, we can test if a string looks like a positive `int` by
checking that all its characters are digits. Here's a good first try:

```python
def bad_is_positive_int(s):        
    for c in s:
        if not is_digit(c):
            return False
            
    return True
```

The for-loop goes through each character in string `s`, one character at a
time. The if-statement in the body checks if `c` is *not* a digit. If `c`
isn't a digit, then that means `s` can't be digits-only. So we can immediately
return `False`.

If the the loop ends without calling `return False`, then that means all the
characters in `s` must be digits, i.e. there are no non-digit characters in
`s`. And so `True` is returned.

But it's not quite correct: there is one string `s` that returns the wrong
value:

```
>>> bad_is_positive_int('90477')
True
>>> bad_is_positive_int('5')
True
>>> bad_is_positive_int('-995')
False
>>> bad_is_positive_int('0000')
True
>>> bad_is_positive_int('')
True                         # uh oh: wrong answer!
```

The empty string `''` is *not* a positive integer, and so
`bad_is_positive_int('')` ought to return `False`. But as we see it
incorrectly returns `True`.

What's the problem? If you trace `bad_is_positive_int` with `s` set to the
empty string, then you'll see that the for-loop body executes 0 times, and
Python immediately goes to the next statement, `return True`.

So how do we fix this? The simplest way is to handle the empty string as a
special case:

```python
def is_positive_int(s):
    # if s is the empty string, return False immediately
    if s == '': return False
        
    for c in s:
        if not is_digit(c):
            return False
            
    return True
```

The empty string as often a special case, and it's wise to always check that
your string functions work correctly with it.


### Example: Remove all Spaces from a String

Let's write a function that takes any string `s` as input, and returns a copy
of `s` with all spaces removed. For example:

```
>>> remove_all_spaces('one 2   three  ')
'one2three'
>>> remove_all_spaces('shoebox')
'shoebox'
>>> remove_all_spaces('    ')
''
>>> remove_all_spaces('')
''
```

One way to do this is to use the accumulator pattern and go through the
characters of `s` one at a time, only keeping them if they are *not* spaces:

```python
def remove_all_spaces(s):
    """ Returns a copy of s with all spaces removed.
    """
    result = ''
    for c in s:
        if c != ' ':
            result += c
    return result
```

We can generalize `remove_all_spaces` in a useful way. Suppose that in
addition to passing in `s`, we also pass in a string of *bad* characters that
we want removed from `s`. It would work like this:

```
>>> remove_all_bad('ox way', 'yx')  # remove all 'x' and 'y' characters
'o wa'
>>> remove_all_bad('orange peel', 'aeiou')  # remove all vowel characters
'rng pl'
>>> remove_all_bad('3.145', '0123456789')  # remove all digit characters
'.'
```

Here's an implementation:

```python
def remove_all_bad(s, bad_chars):
    """ Returns a copy of s with all characters in bad_chars removed.
    """
    result = ''
    for c in s:
        if c not in bad_chars:  # only change from remove_all_spaces
            result += c
    return result
```

The only difference is that the if-statement now checks if `c` is *not* in
`bad_chars`.

Now that we have `remove_all_bad`, we can implement `remove_all_spaces` in
this simple way:

```python
def remove_all_spaces(s):
    """ Returns a copy of s with all spaces removed.
    """
    return remove_all_bad(s, ' ')
```

Here's a function that removes all digits:

```python
def remove_all_digits(s):
    """ Returns a copy of s with all digits removed.
    """
    return remove_all_bad(s, '0123456789')
```

And this function removes all vowels:

```python
def remove_all_vowels(s):
    """ Returns a copy of s with all digits removed.
    """
    return remove_all_bad(s, 'aeiouAEIOU')
```
