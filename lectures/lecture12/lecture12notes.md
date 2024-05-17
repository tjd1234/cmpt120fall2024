# Lecture 12 Notes

## If-statements

**If-statements** are the main way of making decisions in Python and they come
in a few different styles. For example:

```python
name = input('Who are you? ')
if name == 'Joe':
	print('Good day Mr President')

print('...')
```

The line `if name == 'Joe'` is the first line of an **if-statement**. It
starts with the keyword `if`, followed by a boolean expression (i.e. an
expression that evaluates to `True` or `False`), followed by a `:` that marks
the end of the statement. The code indented underneath is the **body of the
if-statement**, and will only be executed if the boolean expression evaluates
to `True`. If it evaluates to `False`, then the body is skipped.

An if-statement can also have an `else`:

```python
name = input('Who are you? ')
if name == 'Joe':
	print('Good day Mr President')
else:
	print('Hey, you\'re not the president!')

print('...')
```

The code indented under the `else` part of an if-statement is only executed if
*none* of the previous if-statement expressions evaluate to `True`. It's a
catch-all for if-statements.

Here's another example. Imagine a website ask you to enter your password
twice, to confirm it:

```python
pass1 = input('Please enter your password: ')
pass2 = input('Please re-enter your password: ')

if pass1 == pass2:
	print('Okay, the passwords match')
else:
	print("Uh oh, the passwords don't match")
```

You could also have written it this way:

```python
pass1 = input('Please enter your password: ')
pass2 = input('Please re-enter your password: ')

if pass1 != pass2:
	print("Uh oh, the passwords don't match")
else:
	print('Okay, the passwords match')
```

In general, and if-else statement has this form:

```python
if <condition> :
	# ... code to run if condition is true ...
else:
	# ... code to run if condition is false ...
```

The boolean expression being tested is often called the if-statement's
**condition**.


## elif statements

An if-statement can check multiple conditions. For example, suppose a school
with 3 semesters uses the code `s1` for the spring semester, `s2` for the
summer semester, and `s3` for the fall semester:

```python
code = input('Please enter semester code: ')

if code == 's1':      # condition 1
	print('Spring!')
elif code == 's2':    # condition 2
	print('Summer!')
elif code == 's3':    # condition 3
	print('Fall!')
else:
	print('Unknown semester code:', code)
```

This if-statement has 3 conditions. Python checks them **one at time in order
from top to bottom**. The first condition that is `True`, Python runs the
indented code underneath and then jumps out of the if-statement. If none of
the conditions are true, the code in the `else` part is executed.

**Example**: Transit Fares

A city bus system has these rules for fares:

- Children 12 and under ride *free*.
- Youths 14 to 18, or seniors 65 and older, pay *concession* fares.
- Everyone else pays *full* fares.

Write a program that asks a user to enter their age, and then uses an
if-elif-else statement to print the correct fare. If the user enters an age
less than 0, then print a helpful error message.

Here are a few sample runs:

```
How old are you? 66
Senior: concession fare

How old are you? 16
Youth: concession fare

How old are you? 6
Child: free

How old are you? -6
-6 is not a valid age

```

Here's one possible answer (see [bus1.py](bus1.py)):

```python
age = input('How old are you? ')
age = int(age)

if age < 0:
    print(f"{age} is not a valid age!")
elif age <= 12:
    print('Child: free')
elif age <= 18:
    print('Youth: concession fare')
elif age >= 65:
    print('Senior: concession fare')
else:
    print('Adult: full fare')
```

This solution has a readability issue: the statement `elif age <= 18` on its
own is easy to mis-read as the rule is "if age is less than or equal to 18,
then it's a youth concession fare". But that's not correct. You need to know
the two cases that come before it are false.

Here is an alternative solution that makes the rules a little more explicit
(see [bus2.py](bus2.py)):

```python
age = input('How old are you? ')
age = int(age)

if age < 0:
    print(f"{age} is not a valid age!")
elif 0 <= age <= 12:
    print('Child: free')
elif 14 <= age <= 18:
    print('Youth: concession fare')
elif 65 <= age:
    print('Senior: concession fare')
else:
    print('Adult: full fare')
```

Now the condition for a youth concession fare is precise, `elif 14 <= age <=
18`.
