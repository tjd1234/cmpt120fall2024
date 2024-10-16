# chp6.py

def f(x):
    """ A demo function for learning functions.
    This is an example of a documentation string,
    i.e. a doc string.
    """
    return 2 * x + 1

def greet(name):
    print(f'Hello {name}!')


def my_abs(x):
    """Returns absolute value of x.
    """
    if x < 0:
        return -x
    else:
        return x

def is_prime(n):
    """Returns true if n is prime, false otherwise.
    """
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def num_primes(n):
    """Returns number of primes <= n.
    """
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count

def S_formula(n):
    return n * (n + 1) // 2

def S_loop(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def S_recursive(n):
    if n == 0:
        return 0
    else:
        return S_recursive(n-1) + n

def S_test(num_tests):
    for i in range(num_tests + 1):
        sf = S_formula(i)
        sl = S_loop(i)
        sr = S_recursive(i)
        if not (sf == sl and sl == sr):
            print(f'Error: S_formula({i}) = {sf}')
            print(f'          S_loop({i}) = {sl}')
            print(f'     S_recursive({i}) = {sr}')
            return  # bare return

    print('All tests passed!')



def F(n):
    """Returns the nth Fibonacci number.
    """
    if n == 0:   # base case 1
        return 0
    elif n == 1: # base case 2
        return 1
    else:        # recursive case
        return F(n - 1) + F(n - 2)



















    
