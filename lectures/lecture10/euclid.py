# euclid.py

def get_int(prompt):
    return int(input(prompt))

def gcd(a, b):
    """ Returns the greatest common divisor of a and b.
    Assumes a and b are positive.
    """
    while a != b:
        #print(a, b)  # see how and a and b change
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def lcm(a, b):
    """ Returns the lowest commmon multiple of a and b.
    Assumes a and b are positive.
    """
    return a * b // gcd(a, b)

def main():
     a = get_int('What is a? ')
    b = get_int('What is b? ')

    print("greatest common divisor:", gcd(a, b))
    print(" lowest common multiple:", lcm(a, b))
