# sample_code.py

def reverse(s):
    result = ''
    i = len(s) - 1
    while i >= 0:
        result += s[i]
        i -= 1
    return result


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


def name_change(first, last):
    """Swaps the first two letters of first and last.
    The result is returned as a concatenated string.

    >>> name_change('Bill', 'Gates')
    'Gill Bates'
    """
    new_first = last[0] + first[1:]
    new_last = first[0] + last[1:]
    return new_first + ' ' + new_last


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


def is_int(s):
    """Returns True if string s is formatted like an int, otherwise False.
    """
    return is_positive_int(s) or is_negative_int(s)
