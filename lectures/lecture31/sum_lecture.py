# sum_lecture.py


def sum_to_mod(n):
    """Same as sum_to, but with print statements.
    """
    print(f'sum_to_mod({n}) called ...')
    if n <= 0:
        print(f'sum_to_mod({n}) returned 0')
        return 0
    else:
        result = sum_to_mod(n - 1) + n
        print(f'sum_to_mod({n}) returned {result}')
        return result
