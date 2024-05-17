# search_test.py

import time

#
# Different ways to test if a value occurs in a list.
#
# Which one is fastest? Which has the nicest implementation?
#


#
# Correctness testing
#

def test_contains(contains):
    """Checks that the passed-in contains function works correctly.

    assert is a built-in Python statement that checks if a condition is true. If
    the condition is true, then nothing happens and the program continues to
    execute. But if the condition is false, then the program immediately stops
    and an error message is printed.


    """
    print(f'calling test_contains({contains.__name__}) ... ', end='')
    assert contains(3, []) == False
    assert contains(3, [3]) == True
    assert contains(1, [3]) == False
    assert contains(4, [3]) == False
    assert contains(3, [1, 3, 5]) == True
    assert contains(1, [1, 3, 5]) == True
    assert contains(5, [1, 3, 5]) == True
    assert contains(0, [1, 3, 5]) == False
    assert contains(2, [1, 3, 5]) == False
    assert contains(-1, [-1, 3, 51, 100]) == True
    assert contains(100, [-1, 3, 51, 100]) == True
    assert contains(2, [-1, 3, 51, 100]) == False
    assert contains(200, [-1, 3, 51, 100]) == False
    print('passed')


def contains_builtin(x, lst):
    return x in lst


def contains_for_each(x, lst):
    for item in lst:
        if item == x:
            return True
    return False


def contains_for_range(x, lst):
    for i in range(len(lst)):
        if lst[i] == x:
            return True
    return False


def contains_while(x, lst):
    i = 0
    while i < len(lst):
        if lst[i] == x:
            return True
        i += 1
    return False


def contains_recursive_linear(x, lst):
    if lst == []:
        return False
    elif lst[0] == x:
        return True
    else:
        return contains_recursive_linear(x, lst[1:])


def contains_recursive_binary(x, lst):
    """Assumes lst is sorted.
    """
    if lst == []:
        return False
    else:
        mid = len(lst) // 2
        if lst[mid] == x:
            return True
        elif x < lst[mid]:
            return contains_recursive_binary(x, lst[:mid])
        else: # lst[mid] < x
            return contains_recursive_binary(x, lst[mid+1:])


test_contains(contains_builtin)
test_contains(contains_for_each)
test_contains(contains_for_range)
test_contains(contains_while)
test_contains(contains_recursive_linear)
test_contains(contains_recursive_binary)


#
# Performance testing
#

def test_performance():
    """Tests performance of the contains functions by looking for -1,
    which is not in the list. This forces each function call to do the maximum
    amount of work.
    """
    #
    # contains_recursive_linear is excluded because it makes more recursive
    # calls than is permitted by Python's recursion limit
    #
    contains_functions = [#contains_recursive_linear,
                          contains_builtin,
                          contains_for_each,
                          contains_for_range,
                          contains_while,
                          contains_recursive_binary]

    test_data = list(range(1000000))
    print()
    for contains in contains_functions:
        print(f'testing:  {contains.__name__:25}  ', end='')
        start = time.time()
        for i in range(100):
            contains(-1, test_data)
        elapsed_time = time.time() - start
        print(f'{elapsed_time:.2f} seconds')

test_performance()
