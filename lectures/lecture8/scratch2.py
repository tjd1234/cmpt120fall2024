# scratch2.py

total = 0
for i in range(1, 101):
    total += i  # += means "add to"

print(total)


def sum_to(n):
    """ Returns 1 + 2 + ... + n.
    """
    total = 0  # local variable
    for i in range(1, n + 1):
        total += i
    return total


def sum_squares_to2(begin, end):
    """ Returns begin^2 + (begin + 1)^2 + ... + end^2.
    """
    total = 0  # local variable
    for i in range(begin, end + 1):
        total += i ** 2
    return total

def sum_squares_to(n):
    """ Returns 1^2 + 2^2 + ... + n^2.
    """
    return sum_squares_to2(1, n)
