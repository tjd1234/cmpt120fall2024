# euclid2.py

def main():
    a = get_int('What is a? ')
    b = get_int('What is b? ')
    print("greatest common divisor:", gcd(a, b))

def get_int(prompt):
    result = input(prompt)
    result = int(result)
    return result

def gcd(a, b):
    """ Returns the greatest common divisor of a and b.
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    # a == b at this point
    return a
