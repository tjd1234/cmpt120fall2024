# binary.py

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
    result = ''
    for i in range(num_bits):
        pow2 = 2 ** (num_bits - i - 1)
        if n >= pow2:
            result += '1'
            n -= pow2
        else:
            result += '0'
    return result


def test_dec_to_bits():
    print('calling test_dec_to_bits ...')
    table = [
        (0, 1, '0'), (1, 1, '1'),
        (0, 2, '00'), (1, 2, '01'),
        (2, 2, '10'), (3, 2, '11'),
        (5, 3, '101'), (6, 3, '110'),
        (7, 3, '111'), (8, 4, '1000'),
        (9, 4, '1001'), (10, 4, '1010'),
        (11, 4, '1011'), (12, 4, '1100'),
        (13, 4, '1101'), (14, 4, '1110'),
        (15, 4, '1111'), (16, 5, '10000'),
        (17, 5, '10001'), (18, 5, '10010'),
        (25, 5, '11001'), (26, 5, '11010'),
    ]

    passed = 0
    for n, num_bits, expected in table:
        actual = dec_to_bits(n, num_bits)
        if actual == expected:
            passed += 1
        else:
            print(f'TEST {passed+1}/{len(table)} FAILED')
            print(f'  dec_to_bits(n={n}, num_bits={num_bits})')
            print(f'  expected: "{expected}"')
            print(f'    actual: "{actual}"')
            return
    
    print(f'... test_dec_to_bits: {passed}/{len(table)} tests passed')

def test1():
    for i in range(0, 21):
        print(i, dec_to_bits(i, 5))

def test2():
    """If bits_to_dec and dec_to_bits are correct, should
    print the numbers from 0 to 20.
    """
    for i in range(0, 21):
        result = bits_to_dec(dec_to_bits(i, 5))
        if result == i:
            pass
        else:
            print(f'error on i={i}')
    print('all tests done')

if __name__ == '__main__':
    test_dec_to_bits()
