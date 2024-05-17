# Lecture 4 Notes

A **statement** is an instruction the computer executes, e.g. this program
consists of *6 statements*:

```python
x = input('What is x? ')    # statement 1
y = input('What is y? ')    # statement 2

x = float(x)                # statement 3
y = float(y)                # statement 4

average = (x + y) / 2       # statement 5
print('Average:', average)  # statement 6
```

Later we will see more complex statements, such as if-statements and loops.

An **expression** is a combination of values, variables, operators, and calls
to functions. These are all examples of expressions:

```python
34.22   # values are expressions

2 * (3 + 1)

"Hello" + " " + "there!"

(a + b) / 2

len('shoe')  # len is a built-in function that 
             # returns the length of a string or list
```

We **evaluate** expressions to get a simpler value. The Python interactive
interpreter will tell us the value of an expression:

```python
>>> 2 * (3 + 1)
8

>>> "Hello" + " " + "there!"
'Hello there!'

>>> len('shoe')
4
```

`>>>` indicates the expression typed by the user, and the line after is its
value.

Some expressions don't evaluate to anything simpler:

```python
>>> 5
5

>>> 4.009
4.009

>>> "moon"
'moon'

>>> [1,2,5]
[1, 2, 5]
```

## Arithmetic operators

Arithmetic works pretty much the same as regular arithmetic (`==` means "equal
to" in Python):

| **operator** |       **name**      |              **example**             |
|:------------:|:-------------------:|:------------------------------------:|
|       +      |       addition      | 3 + 4 == 7                           |
|       -      |     subtraction     | 3 - 4 == -1                          |
|       *      |    multiplication   | 3 * 4 == 12                          |
|       /      |       division      | 21 / 5 == 4.2                        |
|      //      |   integer division  | 21 // 5 == 4                         |
|      **      |    exponentiation   | 3 ** 2 == 9                          |
|       %      | modulus (remainder) | 11 % 5 == 1                          |

Python's integers can be arbitrarily large, which can sometimes be useful. For
example:

```python
# ** is the exponentiation operator
>>> 2 ** 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
```

**Exercise** Count the number of digits in `2 ** 1000` by converting it to a
string and using the `len` function.

**Careful!** The **order of operations** follows essentially the same rules as
regular arithmetic:

- expressions in `()`, parentheses, are always evaluated first
- `**` (exponentiation) is always done first
- `*` and `/` are done next, in the order they occur
- other operators are done next, in the order they occur

```python
>>> 1 + 2 * 3
7
>>> (1 + 2) * 3
9
>>> 1 * 2 ** 3 + 1
9
>>> (1 * (2 ** 3)) + 1
9
```

When in doubt, use `()` to be sure expressions are evaluated in the order you
want.

See the following for some more examples of arithmetic:

- [age_in_seconds.py](age_in_seconds.py); how many seconds old are you?
- [cylinder_info.py](cylinder_info.py); calculate the volume and surface
  area of a cylinder
- [group_maker.py](group_maker.py); divide a big group of people into smaller
  groups

## Updating Variables

To add 1 to a variable:

```python
>>> x = 5
>>> x = x + 1
>>> x
6
```

Remember that `=` *doesn't* mean equality (as in math). Instead it means
**assignment**: a copy of the value of the expression on the right is put into
the variable on the left.

To multiply a variable by 3:

```python
>>> x = 5
>>> x = 3 * x
>>> x
15
```
