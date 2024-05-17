# positive_int.py

def is_digit(s):
    """Returns True if string s is a digit, False otherwise.
    """
    #return len(s) == 1 and s in '0123456789'
    if len(s) == 1 and s in '0123456789':
        return True
    else:
        return False
#
# A more compact way to write is_digit:
#
#def is_digit(s):
#    """Returns True if string s is a digit, False otherwise.
#    """
#    return len(s) == 1 and s in '0123456789'

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
