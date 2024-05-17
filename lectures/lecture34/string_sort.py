# string_sort.py

# A function that returns a list of strings sorted by length.

"""
Write a function called string_sort(str_list) that takes a list of strings as
input and returns a copy of str_list sorted by length, from smallest to biggest.
Strings of the same length should be sorted alphabetically. For example:

>>> string_sort(['dog', 'or', 'a', 'cat'])
['a', 'or', 'cat', 'dog']
>>> string_sort('once upon a time in a far away place'.split())
['a', 'a', 'in', 'far', 'away', 'once', 'time', 'upon', 'place']
"""

def string_sort(str_list):
    """Returns a copy of str_list sorted by length. Strings of the same length
    are sorted alphabetically.

    >>> string_sort(['dog', 'or', 'a', 'cat'])
    ['a', 'or', 'cat', 'dog']
    >>> string_sort('once upon a time'.split())
    ['a', 'once', 'time', 'upon']
    """
    # make a list of [length, string] pairs
    pairs = []
    for s in str_list:
        pairs.append([len(s), s])
    pairs.sort()

    # read the now-sorted strings back into a list
    result = []
    for p in pairs:
        result.append(p[1])
    return result
