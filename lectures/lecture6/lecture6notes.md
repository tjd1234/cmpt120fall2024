# Lecture 6 Notes

## The turtle Module Documentation

Python organizes related pieces of code into **modules**. For example,
`turtle` is a module that comes with [a lot of
documentation](https://docs.python.org/3/library/turtle.html).

You can find documentation for all of Python built-in commands and modules on
the same website.


## The math Module

`math` is a useful module that provides many standard math functions. A handy
trick for seeing the functions in a module is to first import the module, and
then call `dir` on it:

```python
>>> import math
>>> dir(math)
['__doc__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'acos',
 'acosh',
 'asin',
 'asinh',
 'atan',
 'atan2',
 'atanh',
 'ceil',
 'copysign',
 'cos',
 'cosh',
 'degrees',
 'e',
 'erf',
 'erfc',
 'exp',
 'expm1',
 'fabs',
 'factorial',
 'floor',
 'fmod',
 'frexp',
 'fsum',
 'gamma',
 'gcd',
 'hypot',
 'inf',
 'isclose',
 'isfinite',
 'isinf',
 'isnan',
 'ldexp',
 'lgamma',
 'log',
 'log10',
 'log1p',
 'log2',
 'modf',
 'nan',
 'pi',
 'pow',
 'radians',
 'sin',
 'sinh',
 'sqrt',
 'tan',
 'tanh',
 'tau',
 'trunc']
```

That's a lot of functions. Let's look at a couple:

```python
>>> import math

>>> math.sqrt(2)
1.4142135623730951

>>> math.factorial(52)
80658175170943878571660636856403766975289505440883277824000000000000

>>> math.sin(10)
-0.5440211108893698

>>> math.pi
3.141592653589793

>>> math.log10(2000)
3.3010299956639813

>>> math.gcd(1001, 777)
7
```

A couple of notes:

- `math.factorial(n)` returns the *factorial* of $n$, i.e. $1 \cdot 2 \cdot 3
  \cdot \ldots \cdot n$. This is an important function in computer science.
  Among other things, it tells you exactly how many ways $n$ distinct objects
  can be arranged in a line. For instance, `math.factorial(52)` is the number
  of ways a deck of 52 cards can be shuffled.
- `math.pi` is a variable, not a function.


## The random Module

Another useful module is `random`, which provides various functions for
generating random numbers:

```python
>>> import random
>>> dir(random)
['BPF',
 'LOG4',
 'NV_MAGICCONST',
 'RECIP_BPF',
 'Random',
 'SG_MAGICCONST',
 'SystemRandom',
 'TWOPI',
 '_Sequence',
 '_Set',
 '__all__',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 '_accumulate',
 '_acos',
 '_bisect',
 '_ceil',
 '_cos',
 '_e',
 '_exp',
 '_inst',
 '_log',
 '_os',
 '_pi',
 '_random',
 '_repeat',
 '_sha512',
 '_sin',
 '_sqrt',
 '_test',
 '_test_generator',
 '_urandom',
 '_warn',
 'betavariate',
 'choice',
 'choices',
 'expovariate',
 'gammavariate',
 'gauss',
 'getrandbits',
 'getstate',
 'lognormvariate',
 'normalvariate',
 'paretovariate',
 'randint',
 'random',
 'randrange',
 'sample',
 'seed',
 'setstate',
 'shuffle',
 'triangular',
 'uniform',
 'vonmisesvariate',
 'weibullvariate']
```

Here are a few useful functions. `random.randint(a, b)` returns a randomly
chosen integer from `a` to `b` (including possibly `a` or `b`):

```python
>>> random.randint(1, 6)
2
>>> random.randint(1, 6)
1
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
1
>>> random.randint(1, 6)
4
```

The function `random.random()` returns a floating point number from 0 to 1
(but never exactly 1):

```python
>>> random.random()
0.47745380693286654
>>> random.random()
0.922890294962554
>>> random.random()
0.1053133399211651
```

The function `random.shuffle` scrambles the elements of a list:

```python
>>> pets = ['dog', 'cat', 'bird', 'fish']
>>> pets
['dog', 'cat', 'bird', 'fish']
>>> random.shuffle(pets)
>>> pets
['dog', 'fish', 'bird', 'cat']
>>> random.shuffle(pets)
>>> pets
['bird', 'cat', 'fish', 'dog']
```

`random.choice` returns element chosen at random from the list:

```python
>>> pets = ['dog', 'cat', 'bird', 'fish']
>>> random.choice(pets)
'cat'
>>> random.choice(pets)
'bird'
>>> random.choice(pets)
'cat'
```

## Making Your Own Modules

It's quite easy to make your own Python modules. For example, suppose you want
to write a module that helps you create chatbots. First put your
chatbot-related variables and functions in `chatbot.py` as usual. Then you can
call them in another file using an `import chatbot` statement. As we saw
above, you will need to use dot-notation, e.g. in the importing file you have
to write `chatbot.say('Hello')` or `chatbot.set_name('Eliza')`.

We won't go into any more details here since we haven't covered functions yet,
but we will see modules again later.


## Exercise: Random Product Names

Write a Python program that generates random product names, e.g.:

```
How many product names do you want? 5

1. transparent electric coconut stretcher
2. mega auto-tuned hamster treat curler
3. super solar-powered dog toy dryer
4. mini solar-powered hamster treat dryer
5. super digital hamster treat dryer
```

The idea is to make a template for the structure of a product name, e.g. each
name in the example follows the template "{modifier1} {modifier2} {noun}
{verb}". For each modifier, noun, and verb, create a list of interesting
words. Then use `random.choice` to chose random words from the lists, and
print the results using the template.

See a sample solution in [random_products.py](random_products.py).
