# recursion_lecture.py

def f(count):
    if count == 0:
        return

    f(count - 1)
    print(f'{count}. hello')

def print_upto(n):
    """Prints 1 to n.
    Using recursion.
    """
    if n == 0:
        return

    print_upto(n - 1)
    print(n)

def print_downto(n):
    """Prints n down to 1.
    Uses recursion.
    """
    if n == 0:
        return

    print(n)
    print_downto(n - 1)

def my_range(n):
    if n <= 0:
        return []
    else:
        return my_range(n-1) + [n-1]


def S(n):
    if n == 0:
        return 0
    else:
        return S(n-1) + n






