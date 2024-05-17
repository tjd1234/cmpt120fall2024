# sample_code.py

def reverse(s):
    """Returns a string that is the reverse of s.

    >>> reverse('bird')
    'drib'
    """
    result = ''
    i = len(s) - 1
    while i >= 0:
        result += s[i]
        i -= 1
    return result

def pluralize2(word):
    if word == '':
        return word
    elif word[-1] == 's':
        return word
    else:
        return word + 's'


def pluralize(word):
    if word == '' or word[-1] == 's':
        return word
    else:
        return word + 's'
