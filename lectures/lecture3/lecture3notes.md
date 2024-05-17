# Lecture 3 Notes

## Introduction to Strings, Numbers, and Lists

Here are some Python **data types** and example **literals**:

- *integers*, `int`s: `5`, `0`, `-47`, ...

- *floating point* numbers, `float`s: `4.009`, `-0.001`, `4859.343`, ...

- *strings*, `str`: `'hello'`, `"goodbye!"`, `''` (the empty string), `"5"`,
  `"4.009"`, ...

- *lists*, `list`: `[2, 9, 2]`, `['hot dog', 'hamburger']`, `[]` (the empty
  list), ...

## Getting the type of a Value

The `type` function tells you a value's type (or `class`, as Python calls it):

```python
>>> type(5)
<class 'int'>
>>> type(4.0009)
<class 'float'>
>>> type('hello')
<class 'str'>
>>> type([2,9,2])
<class 'list'>
>>> type(['hot dog', 'hamburger'])
<class 'list'>
```

## Converting Between Types

Use `int` and `float` to convert strings to numbers:

```python
>>> int("5")
5
>>> float("5")
5.0
>>> float("4.0009")
4.0009
```

Watch out for errors:

```python
>>> int("4.0009")
Traceback (most recent call last):
  File "__main__", line 1, in <module>
ValueError: invalid literal for int() with base 10: '4.0009'

>>> float('pi')
Traceback (most recent call last):
  File "__main__", line 1, in <module>
ValueError: could not convert string to float: 'pi'
```

`str` converts numbers and lists to strings:

```python
>>> str(5)
'5'
>>> str(4.009)
'4.009'
>>> str([2,9,2])
'[2, 9, 2]'
```

## Variables

A **variable** is a name that refers to a value.

```python
name = 'Bob'
age = 20
gpa = 3.09

print('Student:', name)
print('Age:', age)
print('GPA:', gpa)
```

`=` means **assignment**. It's *not* equality, like in math. Python uses `==`
for equality.

`x = y` means assign a *copy* of the value of `y` to `x`. This example is
important:

```python
>>> a = 5
>>> b = a   # b gets a copy of the 5 stored by a
>>> a
5
>>> b
5
>>> a = 2   # sets a to 2, b is unchanged
>>> b
5
```

## Keywords

Python reserves about 35 names for **keywords**:

```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

You **cannot** use a keyword as a variable name.

**Rule of thumb**: choose **self-descriptive variable names** that give humans
a hint about what their purpose.


## Example: chatbots

A **chatbot** is a program that converses with a user.

Here's [a transcript of a chat with
Eliza](http://psych.fullerton.edu/mbirnbaum/psych101/eliza.htm), [one of the
first and most famous chatbots of all
time](https://en.wikipedia.org/wiki/ELIZA). Eliza emulates a psychiatrist, and
tries to help people with their problems:

``` 
#
# > is Eliza's output
# * is human's input
#

> Hello, I am Eliza. 
* I am having scary dreams.

> Do you believe it is normal to be having scary dreams? 
* No.

> Are you saying no just to be negative? 
* Yes. I don't face up to my problems.

> Why don't you face up to your problems? 
* I am scared of finding out who I really am.

> Did you come to me because you are scared of finding out who you really are?

...
```

What is the structure of a chatbot program?

1. ask the user for some input
2. print something based on the input
3. repeat steps 1 and 2

Drawing this as a diagram (a flow chart) might help.

Chatbot program:

- [chatbot1.py](chatbot1.py): asks the user for their name and says hello
- [chatbot2.py](chatbot2.py): also asks the user for their height
- [chatbot3.py](chatbot3.py): uses a list of strings and imports `random` to
  choose a random greeting
