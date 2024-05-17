# squareRoot.py

import math

def newton_sqrt(x):
    """ Returns the square root of x, for x > 0.
    Uses Newton's method to estimate the square root.
    """
    # initial guess for the square of x is half of x
    approx = 0.5 * x

    # the expression on the right of = is a better approximation
    better = 0.5 * (approx + x / approx)

    # keep improving the approximation until no more improvements occur
    while better != approx:
        print(f'  {approx}')
        approx = better
        better = 0.5 * (approx + x / approx)
    return approx

newton_sqrt(5)

#print('math.sqrt', 'newton_sqrt')
#for i in range(1, 11):
#    print(math.sqrt(i), newton_sqrt(i))
