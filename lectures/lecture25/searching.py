# searching.py

import time
import random

####################################################################################
#
# Linear search
#
####################################################################################

def linear_search(x, lst):
    """Returns the position of the left-most x in lst.
    If x is not in lst, returns -1.
    lst is assumed to be a list of values. Order doesn't matter.
    """
    i = 0
    while i < len(lst):
        if lst[i] == x: # x found at location i
            return i
        i += 1
    return -1           # x not in lst

def linear_search_test():
    """Test that linear search works correctly.

    assert expr does nothing if expr evaluates to True. If expr evaluates to
    False, then the program immediately crashes with an error message.
    """
    assert linear_search(5, []             ) == -1
    assert linear_search(5, [3]            ) == -1
    assert linear_search(5, [3, 1]         ) == -1
    assert linear_search(5, [5]            ) ==  0
    assert linear_search(5, [5, 2]         ) ==  0
    assert linear_search(5, [2, 5]         ) ==  1
    assert linear_search(5, [5, 5, 5]      ) ==  0
    assert linear_search(5, [1, 2, 5, 4, 7]) ==  2
    print('all linear_search tests passed!')

linear_search_test()


#
# Reverse linear search
#
def reverse_linear_search(x, lst):
    """Returns the position of the right-most x in lst.
    If x is not in lst, returns -1.
    lst is assumed to be a list of values. Order doesn't matter.
    """
    i = len(lst) - 1
    while i >= 0:
        if lst[i] == x: # x found at location i
            return i
        i -= 1
    return -1           # x not in lst

def reverse_linear_search_test():
    """Test that linear search works correctly.

    assert expr does nothing if expr evaluates to True. If expr evaluates to
    False, then the program immediately crashes with an error message.
    """
    assert reverse_linear_search(5, []             ) == -1
    assert reverse_linear_search(5, [3]            ) == -1
    assert reverse_linear_search(5, [3, 1]         ) == -1
    assert reverse_linear_search(5, [5]            ) ==  0
    assert reverse_linear_search(5, [5, 2]         ) ==  0
    assert reverse_linear_search(5, [2, 5]         ) ==  1
    assert reverse_linear_search(5, [5, 5, 5]      ) ==  2
    assert reverse_linear_search(5, [1, 2, 5, 4, 7]) ==  2
    print('all reverse_linear_search tests passed!')

reverse_linear_search_test()

####################################################################################
#
# Binary search
#
####################################################################################

def binary_search(x, lst):
    """Returns an index i such that list[i] == x.
    If x is not in lst, returns -1.
    lst must be in sorted order, from smallest to biggest.
    """
    lo = 0
    hi = len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == x:
            return mid    # x found at location mid
        elif x < lst[mid]:
            hi = mid - 1
        else: # lst[mid] < x
            lo = mid + 1
    return -1             # x not in lst

def binary_search_test():
    """Test that binary search works correctly.

    assert expr does nothing if expr evaluates to True. If expr evaluates to
    False, then the program immediately crashes with an error message.
    """
    assert binary_search(5, []             ) == -1
    assert binary_search(5, [3]            ) == -1
    assert binary_search(5, [3, 1]         ) == -1
    assert binary_search(5, [5]            ) ==  0
    assert binary_search(5, [5, 2]         ) ==  0
    assert binary_search(5, [2, 5]         ) ==  1
    assert binary_search(5, [5, 5, 5]      ) in [0, 1, 2]
    assert binary_search(5, [1, 2, 5, 4, 7]) ==  2
    print('all binary_search tests passed!')

binary_search_test()

####################################################################################
#
# Performance testing functions
#
####################################################################################

import random

def rand_range(n):
    """Returns a new list with 0, 1, 2, ..., n-1 in random order.
    """
    result = list(range(n))
    random.shuffle(result)
    return result

def linear_search_mod(x, lst):
    """Same as linear_search, but returns # of comparisons.
    """
    comp_count = 0
    i = 0
    while i < len(lst):
        comp_count += 1
        if lst[i] == x: # x found at location i
            # return i
            return comp_count
        i += 1
    # return -1           # x not in lst
    return comp_count

def linear_search_performance():
    print('\nLinear Search Performance')
    for size in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
        lst = rand_range(size)

        total_comps = 0

        # search for 50 values we know are in lst
        for i in range(50):
            total_comps += linear_search_mod(i, lst)

        # search for 50 values we know are not in lst
        for i in range(50):
            total_comps += linear_search_mod(-1, lst)

        avg_comps = total_comps / 100
        print(f'{size} {avg_comps}')
        # print(f'linear search size {size}, avg_comps = {avg_comps}')

#linear_search_performance()

"""
Linear Search Performance
linear search size 1000, avg_comps = 759.1
linear search size 2000, avg_comps = 1459.23
linear search size 3000, avg_comps = 2330.1
linear search size 4000, avg_comps = 3111.48
linear search size 5000, avg_comps = 3779.53
linear search size 6000, avg_comps = 4467.92
linear search size 7000, avg_comps = 5485.42
linear search size 8000, avg_comps = 6403.07
linear search size 9000, avg_comps = 7266.68
linear search size 10000, avg_comps = 7451.71
"""

def binary_search_mod(x, lst):
    """Same as linear_search, but returns # of comparisons.
    """
    comp_count = 0
    lo = 0
    hi = len(lst) - 1
    while lo <= hi:
        comp_count += 1
        mid = (lo + hi) // 2
        if lst[mid] == x:
            # return mid    # x found at location mid
            return comp_count
        elif x < lst[mid]:
            hi = mid - 1
        else: # lst[mid] < x
            lo = mid + 1
    #return -1             # x not in lst
    return comp_count

def binary_search_performance():
    print('\nBinary Search Performance')
    for size in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
        lst = list(range(size))

        total_comps = 0

        # search for 50 values we know are in lst
        for i in range(50):
            r = random.randrange(50)
            total_comps += binary_search_mod(r, lst)

        # search for 50 values we know are not in lst
        for i in range(25):
            total_comps += binary_search_mod(-1, lst)
            total_comps += binary_search_mod(len(lst), lst)

        avg_comps = total_comps / 100
        print(f'{size} {total_comps}')
        # print(f'binary search size {size}, avg_comps = {avg_comps}')

#binary_search_performance()

"""
Binary Search Performance
binary search size 1000, avg_comps = 9.26
binary search size 2000, avg_comps = 10.26
binary search size 3000, avg_comps = 11.08
binary search size 4000, avg_comps = 11.26
binary search size 5000, avg_comps = 11.94
binary search size 6000, avg_comps = 12.08
binary search size 7000, avg_comps = 12.19
binary search size 8000, avg_comps = 12.26
binary search size 9000, avg_comps = 12.86
binary search size 10000, avg_comps = 12.94
"""

def search_compare():
    print('Comparing built-in index to linear search and binary search ...')
    print('Generating random lists ...')
    sizes = [n for n in range(10000, 20001, 1000)]
    print(sizes)
    data = [rand_range(n) for n in sizes]

    # test built-in index
    index_times = []
    print(f'Testing built-in index ...')
    for lst in data:
        reps = 100
        total_time = 0
        # search for values in the list
        for i in range(reps):
            r = random.randrange(len(lst))
            start = time.time_ns()
            try: lst.index(r)
            except: pass
            find_time = time.time_ns() - start
            total_time += find_time

        # search for values not in the list
        for i in range(reps):
            r = -1  # -1 is not in the list
            start = time.time_ns()
            try: lst.index(r)
            except: pass
            find_time = time.time_ns() - start
            total_time += find_time

        index_times.append(find_time / (2 *reps))

    # test linear search
    linear_times = []
    print(f'Testing linear search ...')
    for lst in data:
        reps = 100
        total_time = 0
        # search for values in the list
        for i in range(reps):
            r = random.randrange(len(lst))
            start = time.time_ns()
            linear_search(r, lst)
            find_time = time.time_ns() - start
            total_time += find_time

        # search for values not in the list
        for i in range(reps):
            r = -1  # -1 is not in the list
            start = time.time_ns()
            linear_search(r, lst)
            find_time = time.time_ns() - start
            total_time += find_time

        linear_times.append(find_time / (2 *reps))

    # test binary search
    binary_times = []
    print(f'Testing binary search ...')
    for lst in data:
        reps = 100
        total_time = 0
        # search for values in the list
        for i in range(reps):
            r = random.randrange(len(lst))
            start = time.time_ns()
            binary_search(r, lst)
            find_time = time.time_ns() - start
            total_time += find_time

        # search for values not in the list
        for i in range(reps):
            r = -1  # -1 is not in the list
            start = time.time_ns()
            binary_search(r, lst)
            find_time = time.time_ns() - start
            total_time += find_time

        binary_times.append(find_time / (2 *reps))

    # print results
    index_times = [t/(10**9) for t in index_times]
    linear_times = [t/(10**9) for t in linear_times]
    binary_times = [t/(10**9) for t in binary_times]

    print()
    print('n index linear binary')
    for i in range(len(sizes)):
        print(f'{sizes[i]} {index_times[i]} {linear_times[i]} {binary_times[i]}')

#search_compare()
