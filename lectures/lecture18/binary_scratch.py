# binary_scratch.py

def bits_to_dec(bits):
    """Returns the base-10 int value of bits.
    Assumes bits is a string of 0s and 1s. For example:

    >>> bits_to_dec('011101')
    29
    """
    pow = len(bits) - 1
    result = 0
    for b in bits:
        result += int(b) * 2**pow
        pow -= 1   # subtract 1 from pow
    return result

def dec_to_bits(n, num_bits):
    """Returns binary representation of base-10 integer n.
    Assumes n is an int and n >= 0, and num_bits is big enough
    to represent n. A string of num_bits bits is returned. For
    example:

    >>> dec_to_bits(19, 5)
    '10011'
    >>> dec_to_bits(19, 10)
    '0000010011'
    """
    result = ''
    #for i in range(num_bits):
    #    pow2 = 2 ** (num_bits - i - 1)
    for i in range(num_bits - 2, 0, -1):
        pow2 = 2 ** i
        print(f'pow2={pow2}')
        if n >= pow2:
            result += '1'
            n -= pow2
        else:
            result += '0'
    return result

def test1():
    for i in range(0, 21):
        print(i, dec_to_bits(i, 5))

def test2():
    """If bits_to_dec and dec_to_bits are correct, should
    print the numbers from 0 to 20.
    """
    for i in range(0, 21):
        print(bits_to_dec(dec_to_bits(i, 5)))
