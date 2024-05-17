# remove_spaces.py

def remove_all_spaces(s):
    """ Returns a copy of s with all spaces removed.
    """
    result = ''
    for c in s:
        if c != ' ':
            result += c
    return result













def remove_all_bad(s, bad_chars):
    """ Returns a copy of s with all characters in bad_chars removed.
    """
    result = ''
    for c in s:
        if c not in bad_chars:  # only change from remove_all_spaces
            result += c
    return result



def remove_all_digits(s):
    """ Returns a copy of s with all digits removed.
    """
    return remove_all_bad(s, '0123456789')




def remove_all_spaces2(s):
    """ Returns a copy of s with all spaces removed.
    """
    return remove_all_bad(s, ' ')
