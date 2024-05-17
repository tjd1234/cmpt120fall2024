# Lecture 19 Notes

A **data structure** is an organized collection of data. Python has three main
built-in data strucrures that we will see in this course:

- *Strings*, which are ordered sequences of characters.
- *Lists*, which are ordered sequences of any values.
- *Dictionaries*, which let you find a value using a key value associated with
  it. For example, you could make a dictionary where you can find the name of
  a student given their SFU ID number.

In the next few lecrures, we'll look at **strings**, a very useful and
important data structure. Python has great built-in support for strings, and
so is a good language to use for string processing.

Almost all programs use strings, at least a little. Many use them quite a
lot. For example, web pages are often giant strings of
text, and so web programming relies heavily on strings.


## String Basics

In Python, a **string** is a sequence of 0 or more characters. The type of a
string is `str`:

```python
>>> type('cat')
<class 'str'>
```

A **string literal** is represented using single-quotes, double-quotes, or
triple quotes. Here are 4 examples of string literals:

```python
'you can put a " in single-quote strings'

"you can put a ' in double-quotes strings"

"""Triple-quotes strings can span
multiple lines. They are often use a doc strings
for functions.
"""

'''This is also a triple-quoted string,
using single-quotes instead of double-quotes.
'''
```

As shown you *can* split triple quotes across multiple lines, but you *cannot*
split a regular single-quoted or double-quoted string across multiple lines.

The **empty string** is a string with 0 characters, i.e. of length 0. These
all represent the empty string (the first two are by far the most common):

```
''

""

""""""

''''''
```

We will often need to treat the empty string as a special case when processing
strings.

The *order* of the characters in a string matters. For example, `'abc'` and
`'bac` are *different* strings.

The *case* of a letter in a string *matters*. For example, `'M'` and `'m'` are
*different* string, and `'Cat'` and `'cat'` are also different.

**Note** Some programming languages have a special data type for single
characters. For example, in C++ the `char` data type represents a single
character. However, Python does *not* have a character data type.
Single-character strings like `'h'` or `'!'` are regular strings of length 1.

The **length** of a string is the number of characters it contains, and in
Python the built-in `len` function returns this:

```python
>>> len('')
0
>>> len('log')
3
>>> len('a b c')
5
```


## Special Characters

In a string literal, a '`\`' indicates an **escape character**, which means
that the next character is special in some way. For example, `'\n` is an
escape character called **newline** that represents a command to send the
cursor to the next line. For example:

```python
>>> print('one\ntwo')
one
two
```

The string `'one\ntwo'` has length 7 (not 8!). Even though `'\n'` consists of
two symbols, `\` and `n`, it counts as a single character. Similarly, the
string `'\n\n\n'` has length 3:

```python
>>> len('\n\n\n')
3
```

Here are the most common escape characters that you will see in Python
strings:

|    |   **name**   |                                     **common use**                                    | **example**                            |
|:--:|:------------:|:-------------------------------------------------------------------------------------:|----------------------------------------|
| \n |    newline   | blank line                                                                            | >>> print('a\nb')<br>a<br>b            |
| \t |      tab     | fixed-width space, for formatting;<br>width of a tab is **not** defined by <br>Python | >>> print('\thello!')<br>    hello!    |
| \\\ |   backslash  | \ as a literal character                                                              | >>> print('root\\\\users')<br>root\users |
| \\' | single quote | ' as a literal character                                                           | >>> print('\\'-quote')<br>'-quote       |
| \\" | double quote | " as a literal character                                                           | >>> print("\\"-quote")<br>"-quote       |


**Example 1** Can you make a string, that when printed, displays this?

```
special characters: ' " \
```

Here's one way to do it:

```
print('special characters: \' " \\')
```

**Example 2** Can you make a string, that when printed, displays three backslashes?

```
\\\
```

Each printed `\` needs double-`\` in the string:

```python
print('\\\\\\')  # 6 backslashes
```

Note that 5 backslashes *doesn't* work:

```
>>> print('\\\\\')        # oops: 5 backslashes
  File "<stdin>", line 1
    print('\\\\\')
                 ^
SyntaxError: EOL while scanning string literal
```

The problem here is that Python reads the string as these three characters:
`\\`, `\\`, and `\\'`. This means there is no `'`-quote to end the string, and
so the error.


## Whitespace

A **whitespace character** is a character that doesn't have a visual
representation (and so, when "printed" on a piece of white paper will look
like empty white space). While there are many such characters in Python, the
three most common whitespace characters are:

- `' '`, a regular space
- `\n`, a newline
- `\t`, a tab

When programmers refers to "whitespace", they mean characters like this.
Sometimes whitespace matters, sometimes it doesn't. For instance, the
indentation in a Python program uses "significant whitespace". When we read
strings from the user, we often remove whitespace characters at the beginning
and the end using the `.strip()` method, e.g. the string `'  done\n'` becomes
`'done'`.

## Strings are Immutable

In Python, **mutable** means "changeable", and **immutable** means "not
changeable". Python strings are immutable, i.e. there is no way to modify them
or change their length. While it might sometimes seem like you are changing a
Python string, you're, you are actually making copies and constructing new
strings.

String immutability has both pros and cons:

- One good feature of immutable strings is that they are quite efficient for
  most copying operations. Since they never change, it is always safe to have
  different variables refer to the same underlying string.

- One bad feature of immutable strings is that if you need to, say, change one
  character in a very long string, then you *can't* just change the character,
  you need to construct a brand new string. If your program does this kind of
  thing a lot, then it could become very inefficient.


## String Concatenation

**Concatenating** two strings means to combine them together to make a new
string. This is easily done in Python with the `+` operator:

```
>>> 'cat' + 'nap'
'catnap'
>>> 'Elon' + ' ' + 'Musk'
'Elon Musk'
>>> 'ha' + 'ha' + 'ha'
'hahaha'
```

The last example with `'ha'` is an example of concatenating a string with
itself. You can also do that with the `'*'` operator:

```
>>> 3 * 'ha'
'hahaha'
>>> 'Boat' * 5
'BoatBoatBoatBoatBoat'
```

String expressions can get complicated:

```
>>> s = (5 * 'Meow! ' + '\n') * 6
>>> print(s)
Meow! Meow! Meow! Meow! Meow! 
Meow! Meow! Meow! Meow! Meow! 
Meow! Meow! Meow! Meow! Meow! 
Meow! Meow! Meow! Meow! Meow! 
Meow! Meow! Meow! Meow! Meow! 
Meow! Meow! Meow! Meow! Meow! 
```

## String Comparisons

If `s` and `t` are variables that refer to strings, then:

- `s == t` evaluates to `True` if `s` and `t` are the same length, and have
  exactly the same characters in the same order. Otherwise, it evaluates to
  `False`.

- `s != t` evaluates to `True` if `s` and `t` are different, and to `False` if
  `s == t`. It returns the same value as `not (s == t)`.

- `s < t` evaluates to `True` if `s` comes alphabetically before `t`, and
  `False` otherwise. `s > t` evaluates to the same value as `t < s`.

- `s <= t` evaluates to `True` if either `s < t` or `s == t`, and `False`
  otherwise. `s >= t` evaluates to the same value as `t <= s`.

For example:

```
>>> s = 'cat'
>>> t = 'dog'

>>> s == t
False
>>> s == s
True
>>> ('c' + 'at' ) == s
True
>>> s != t
True

>>> s < t
True
>>> s <= t
True

>>> s > t
False
>>> s >= t
False
```

## String Indexing

Consider this string:

```python
s = 'apple'
```

We can access individual characters in `s` using **string indexing**:

```python
>>> s[0]
'a'
>>> s[1]
'p'
>>> s[2]
'p'
>>> s[3]
'l'
>>> s[4]
'e'
>>> s[5]
Traceback (most recent call last):
  File "__main__", line 1, in <module>
IndexError: string index out of range
```

In Python, string indexing *always* starts at 0, meaning the first character
of a string is at location 0. This is known as **0-based indexing**. The index
of the last character is always *one less* than the length of the string
(because the indices start at 0). If you try to access an index location past
the last one, then you get an "index out of range" run-time error as shown in
the last example above.

Diagrams are helpful for understanding indexing:

```
       0     1     2     3     4
    +-----+-----+-----+-----+-----+
 s  | 'a' | 'p' | 'p' | 'l' | 'e' |
    +-----+-----+-----+-----+-----+
     s[0]  s[1]  s[2]  s[3]  s[4] 
```

In general, if `s` is any *non-empty* string, then `s[0]` is its first
character, and `s[len(s)-1]` is its last character. Evaluating `s[len(s)]`
causes an "index out of range" run-time error.

If `s` is the empty string, then *all* of `s[0]`, `s[len(s)-1]`, and
`s[len(s)]` cause index out of range errors. For the empty string, `s[i]` is
an out of range error for any index `i`.

Since Python strings are immutable (i.e. not changeable), it is an error to
assign a new character to a string:

```
>>> s = 'apple'
>>> s[0] = 'A'
Traceback (most recent call last):
  File "__main__", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

If you want the string `'Apple`, then you must use some combination of string
slice or string methods (discussed later) to create a new string.


## Looping Over Strings

The simplest way to loop over a Python string is like this:

```python
s = 'apple'
for c in s:
  print(c)
```

You can access every character in a string with this style of for-loop:

```python
s = 'apple'
for i in range(len(s)):
	print(s[i])
```

Or the same thing using a while-loop:

```python
s = 'apple'
i = 0
while i < len(s):  # < is important; <= would be wrong
	print(s[i])
	i += 1           # += adds a value to a variable
```

**Challenge** Using a while-loop, write a function that *reverses* a string:

```
>>> reverse('')
''
>>> reverse('a')
'a'
>>> reverse('ab')
'ba'
>>> reverse('abc')
'cba'
>>> reverse('bird')
'drib'
```

Here's one way to do it:

```python
def reverse(s):
    result = ''
    i = len(s) - 1
    while i >= 0:
        result += s[i]
        i -= 1
    return result
```

Since Python strings are immutable, the line `result += s[i]` creates a new
string every time it is called. And all of these strings are quickly discarded
when the next character from `s` is appended. So this isn't a very efficient
function.
