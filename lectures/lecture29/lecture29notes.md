# Lecture 29 Notes

Recall that a **data structure** is an organized collection of data. We've seen
two main Python data structures so far: *strings*, which are collections of
characters, and *lists*, which are collections of any values.

A **dictionary** is another useful data structure that stores data in
*key*:*value* pairs. Dictionaries are also known as **maps**, **associative
arrays**, or **tables** (or **hash tables**).

For example, here is a dictionary of ages:

```
>>> age = {'Marge': 34, 'Homer': 36}
```

`age` is a dictionary with two entries: `'Marge':34` and `'Homer':36`. The first
value of each entry is it's **key**, and the second value is its associated
**value**. You can retrieve them like this:

```
>>> age.keys()
dict_keys(['Marge', 'Homer'])
>>> age.values()
dict_values([34, 36])
```

In this particular example, the keys are strings. A dictionary key can be any
*immutable* (non-changeable) type, such as strings or numbers. However, keys
*can't* be *lists*, since changing the list could cause the dictionary to lose
track of the position of its associated value (the position of a value depends
on its key).

You normally access values in a dictionary by using its associated key. For
example:

```
>>> age['Marge']
34
>>> age['Homer']
36
```

**Important** Accessing a dictionary value through its key is extremely
efficient. It is much faster that accessing a list element (e.g. using `find`),
and is often faster than *binary search*. But unlike binary search, Python's
dictionaries *don't* need to be stored in sorted order.

On the flip side, accessing a key by its value is *not* efficient. You can do
it, but it's about the same speed as doing a linear search through all the
values.

If you ask for a key that's *not* in the dictionary, you get a `KeyError`:

```
>>> age['Bart']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Bart'
```

You can only efficiently access values by their keys. In `age`, you *can't* get
efficiently get a name from the age:

```
>>> age[34]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 34
```

In general, dictionaries are only efficient when you search for values by keys.
You should search a dictionary by value only as a last resort.


## Keys are Unique, Values are Not

In a Python dictionary, all the keys *must* be different: repeated keys are not
allowed. However, values don't need to be unique: values can be repeated. For
example, this is okay:

```
>>> age = {'Marge': 34, 'Homer': 36, 'Carl': 34}
```

`'Carl'` and `'Marge'` have the same age, and that's no problem: different
people can have the same age.

But this is a problem:

```
>>> bad_age = {'Marge': 34, 'Homer': 36, 'Marge': 35}  # oops, two Marge's
>>> bad_age
{'Marge': 35, 'Homer': 36}
```

Since identical keys are *not* allowed, the second `'Marge'` overwrites the
first one, which may, or may not, be what you want. 

If you really do need to have two `'Marge'`s, then you should  probably change
the keys:

```
>>> age = {'Marge 1': 34, 'Homer': 36, 'Marge 2': 35}  # okay, different keys for Marge
>>> age
{'Marge 1': 34, 'Homer': 36, 'Marge 2': 35}
```

## Dictionaries are Changeable

Like lists, dictionaries are *mutable*, i.e. they can be changed. You can
add/remove *key*:*value* pairs, and also change the value associated with a key.
For example:

```
>>> age = {'Marge': 34, 'Homer': 36}

>>> age['Bart'] = 10  # add a new key:value pair
>>> age
{'Marge': 34, 'Homer': 36, 'Bart': 10}

>>> age['Bart'] = 11  # change the value associated with a key
>>> age
{'Marge': 34, 'Homer': 36, 'Bart': 11}

>>> del age['Bart']   # remove a key:value pair
>>> age
{'Marge': 34, 'Homer': 36}
```

These are all fast operations, since they are based on the key.


## Example: Counting Words in a File

Suppose you have a text file, and want to count how many times each different
word occurs. This is a good job for a dictionary: words will be the keys, and
the associated value is how many times the word appears. 

The word counts for a very small file might look like this:

```python
{'cow': 3, 'pig': 1, 'horse': 2}
```

This means `'cow'` appears 3 times, `'pig'` appears 1 time, and `'horse'`
appears 2 times.

Let's write a program that works like this:

- It opens a text file.
- It reads the file line-by-line.
- It splits each line into individual words. Python strings have a built-in
  method called `split` to do this:
  
  ```
  >>> names = 'Ken, Alex, Art, Anna'
  >>> names.split(', ')
  ```

- It adds the words to a dictionary of *word*:*count* pairs. If the word is
  already in the dictionary, then its associated count is incremented. If the
  word is not in the dictionary, it is added with a count of 1.

Getting words from a file is conceptually easy, but the details are tricky
because of things like punctuation. For simplicity, we will strip out everything
that isn't a letter or a space using this function:

```python
def clean_text(text):
    """Remove all non-letter characters from text.

    Keeps just alphabetic characters and spaces.

    >>> clean_text('Hello, world!')
    'Hello  world'
    """
    cleaned_text = ''
    for char in text:
        if char.isalpha() or char == ' ':
            cleaned_text += char  # keep spaces and letters
        else:
            cleaned_text += ' '   # replace other characters with spaces
    return cleaned_text
```

Now we can write `count_words`, which returns a dictionary of the counts of all
the words in a text file:

```python
def count_words(fname):
    """Count the number of words in a file.
    """
    # word_count is an initially empty dictionary that stores the count of each
    # word
    word_count = {}
    
    contents = open(fname)
    for line in contents:
        # split the line into words
        words = clean_text(line).split(' ')
        
        # add all the words to the dictionary
        for w in words:
            w = w.strip()   # remove whitespace at the beginning and end
            if w != '':     # ignore empty strings
                if w in word_count:
                    word_count[w] += 1
                else:
                    word_count[w] = 1
    
    return word_count
```

For example, [jokes.txt](jokes.txt) contains this text:

```
Who's there?
A broken pencil.
A broken pencil who?
Never mind. It's pointless.
```

Then:

```
>>> words = count_words('joke.txt')
>>> words
{'Who': 1, 's': 2, 'there': 1, 'A': 2, 'broken': 2, 'pencil': 2, 'who': 1, 
 'Never': 1, 'mind': 1, 'It': 1, 'pointless': 1}

# the keys are the unique words in the file
>>> words.keys()
dict_keys(['Who', 's', 'there', 'A', 'broken', 'pencil', 'who', 'Never', 
           'mind', 'It', 'pointless'])

>>> words['pencil']
2
>>> words['there']
1

>>> words['eraser']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'eraser'
```

`'eraser'` is not in the dictionary, so we get a `KeyError`.

[dracula.txt](dracula.txt) is a text file of [Bram Stoker's *Dracula*](https://en.wikipedia.org/wiki/Dracula):

```
>>> words = count_words('dracula.txt')
>>> len(words)  # how many unique words?
10018

>>> words['vampire']
14
>>> words['blood']
112

>>> words['chilupas']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'chilupas'
```

## Printing the Top 10 Most Frequent Words

Suppose you want to print a list of the top 10 most frequently occurring words
in a file. We can do this by first getting all the word counts using
`count_words`, and then convert that to a list of *count*:*word* pairs that we
can sort by count.

```python

def print_top10(fname):
    word_count = count_words(fname)
    
    #
    # make a list if [count, word] pairs
    #
    # e.g. if word_count is {'cat':3, 'dog':2, 'mouse':1}, count_pairs
    # will be [3, 'cat'], [2, 'dog'], [1, 'mouse']
    #
    count_pairs = []
    for w in word_count:  # this loops through all they keys in word_count
        pair = [word_count[w], w]
        count_pairs.append(pair)
    
    #
    # sort the words from highest count to lowest 
    # 
    # when sorting a list, Python's built-in sort compares the first element of
    # the list first
    #
    count_pairs.sort()
    count_pairs.reverse()  # reverse the list, we want highest count to lowest

    #
    # print the top 10 words
    #
    for pair in count_pairs[:10]:
        print(pair[1], pair[0])
```

For example:

```
>>> print_top10('dracula.txt')
the 7205
and 5589
I 4831
to 4371
of 3572
a 2880
in 2384
that 2375
he 1931
was 1866
```

**Exercise** Modify `print_top10` to print the top *n* most frequently occurring
words, where *n* is any integer.
