# primes.py

def is_prime(n):
    """Returns True if n is a prime number, False if it's not.
    An integer n is prime if it's bigger than 1, and it has exactly
    two divisors, 1 and itself. The smallest prime is 2 (it's also
    the only even prime), and the next few primes are 3, 5, 7, 11.
    There are an infinite number of primes.

    To test if a number n is prime, it checks if any of the numbers
    from 2 to n-1 divide evenly into n. If none do, then n is prime.
    This method is simple, but quite inefficient, and only useful
    for small numbers.
    """
    if n < 2: return False  # no primes are less than 2

    # Test if any number from 2 to n-1 divides evenly into n. If
    # any do, then n is not prime.
    for trial_divisor in range(2, n):
        if n % trial_divisor == 0:
            return False
    return True


def is_prime2(n):
    """Returns True if n is a prime number, False if it's not.
    An integer n is prime if it's bigger than 1, and it has exactly
    two divisors, 1 and itself. The smallest prime is 2 (it's also
    the only even prime), and the next few primes are 3, 5, 7, 11.
    There are an infinite number of primes.

    Compared to is_prime1, still uses trial division but does so more
    efficiently. Only odd trial divisors are checked, and only up to
    the square root of the number (sime divisors always come in pairs).
    """
    if n < 2:        # no primes are less than 2
        return False
    elif n == 2:     # 2 is special prime: it's the only even prime
        return True
    elif n % 2 == 0: # no even number over 2 is prime
        return False
    else:            # at this point, n is an odd number bigger than 2
        # We use "trial division" to find divisors for n. Divisors always
        # come in pairs so we only need to search up to (and including)
        # the square root of n.
        trial_divisor = 3
        while trial_divisor ** 2 <= n:
            if n % trial_divisor == 0:
                return False
            trial_divisor += 2
        return True

def is_prime_test(is_prime):
    non_primes = [-1, 0, 1, 4, 6, 9, 15, 100]
    primes = [2, 3, 5, 7, 11, 13, 17, 101]

    for n in non_primes:
        assert not is_prime(n)

    for n in primes:
        assert is_prime(n)

    print('is_prime: all tests passed')

#is_prime_test(is_prime)
#is_prime_test(is_prime2)

def primes_less_than(n):
    """Returns a list of all the primes less than n.
    There are 25 primes less than 100, and 168 primes
    less than 1000.
    """
    result = []
    for n in range(2, n):
        if is_prime(n):
            result.append(n)
    return result

def num_primes_less_than(n):
    return len(primes_less_than(n))

#primes = primes_less_than(100)
#print(primes)
#print(len(primes))
