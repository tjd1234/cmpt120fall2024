# sorting.py

import random
import time

is_sorted_True_cases = [
    [], [1], [1, 2], [2, 2],
    [1, 2, 3], [-1, 2, 5, 8],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [10, 200, 200, 300, 5002, 10000]
]

is_sorted_False_cases = [
    [2, 1],
    [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1],
    [2, 2, 4, 4, 1, 1, 1],
    [0, -9, 4, 29, 2, 3, 53, 5, 3, 36, 100, -100, 4, 5, 35]
]

def is_sorted(lst):
    """Returns True if lst is sorted, and False otherwise.
    [] is considered to be sorted.
    """
    n = len(lst)
    if n < 2:
        return True
    else:  # n >= 2
        for i in range(n-1):
            if lst[i] > lst[i+1]:
                return False
        return True

def test_is_sorted():
    print('Testing is_sorted ...')
    for case in is_sorted_True_cases:
        assert is_sorted(case)

    for case in is_sorted_False_cases:
        assert not is_sorted(case)

    print('... all is_sorted test cases passed')
    print()

test_is_sorted()

sorting_test_cases = [
    [], [1], [1, 2], [2, 1], [2, 2],
    [1, 2, 3], [1, 3, 2], [2, 1, 3],
    [2, 3, 1], [3, 1, 2], [3, 2, 1],
    [2, 2, 4, 4, 1, 1, 1],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [0, -9, 4, 29, 2, 3, 53, 5, 3, 36, 100, -100, 4, 5, 35]
]

def test_sort_fn(sort_fn):
    """Compares sort_fn to Python's built-in sort function on
    sorting_test_cases.
    """
    print(f'Testing sort function {sort_fn.__name__} ...')
    fail_count = 0
    for correct in sorting_test_cases:
        actual = correct[:]   # make a copy of the test data
        correct.sort()
        actual = sort_fn(actual)
        if correct == actual:
            print(actual)
            pass  # pass does nothing
        else:
            print(f'Error: expected {correct}')
            print(f'         actual {actual}')
            print()
            fail_count += 1

    print(f'... {sort_fn.__name__} testing done: ', end='')
    if fail_count == 0:
        print('all tests passed')
    else:
        n = len(sorting_test_cases)
        print(f'{fail_count} of {n} tests failed')
    print()

# def test_sort_fn(sort_fn):
#     """Compares sort_fn to Python's built-in sort function on
#     sorting_test_cases.
#     """
#     print(f'Testing sort function {sort_fn.__name__} ...')
#     fail_count = 0
#     for correct in sorting_test_cases:
#         actual = correct[:]   # make a copy of the test data
#         correct.sort()
#         sort_fn(actual)
#         if correct == actual:
#             print(actual)
#             pass  # pass does nothing
#         else:
#             print(f'Error: expected {correct}')
#             print(f'         actual {actual}')
#             print()
#             fail_count += 1

#     print(f'... {sort_fn.__name__} testing done: ', end='')
#     if fail_count == 0:
#         print('all tests passed')
#     else:
#         n = len(sorting_test_cases)
#         print(f'{fail_count} of {n} tests failed')
#     print()

#
# Selection sort
#
def selection_sort(lst_orig):
    """Returns a copy of lst with its items re-arranged into ascending order.
    Uses the selection sort algorithm.
    """
    lst = lst_orig[:]  # make a copy of the list
    result = []
    while len(lst) > 0:
        smallest = min(lst)
        result.append(smallest)
        lst.remove(smallest)
    return result

test_sort_fn(selection_sort)


#
# Here's a version of selection_sort that sorts the data in place without making
# a copy.
#
# def index_of_min(lst, start):
#     """Returns the index smallest element in lst[start:]
#     """
#     min_index = start
#     for i in range(start + 1, len(lst)):
#         if lst[i] < lst[min_index]:
#             min_index = i
#     return min_index
#
# def selection_sort(lst):
#     """Re-arranges the elements of lst in ascending sorted order.
#     Uses the selection sort algorithm.
#     """
#     n = len(lst)
#     for i in range(n-1):
#         mi = index_of_min(lst, i)
#         lst[i], lst[mi] = lst[mi], lst[i]
#


#
# Mergesort
#

import heapq

def merge(lst1, lst2):
    """Combines lst1 and lst2 into a new sorted list.
    lst1 and lst2 must both be in ascending sorted order.
    """
    return list(heapq.merge(lst1, lst2))


#
# Here's an alternative implementation of merge:
#
# def merge(A, B):
#     """Combines A and B into a new sorted list.
#     A and B must both be in ascending sorted order.

#     >>> merge([1, 4, 5], [-2, 0, 4, 6])
#     [-2, 0, 1, 4, 4, 5, 6]
#     """
#     n = len(A) + len(B)
#     result = []
#     a = 0
#     b = 0
#     for i in range(n):
#         if a >= len(A):
#             result.append(B[b])
#             b += 1
#         elif b >= len(B):
#             result.append(A[a])
#             a += 1
#         elif A[a] <= B[b]:
#             result.append(A[a])
#             a += 1
#         else:
#             result.append(B[b])
#             b += 1

#     return result

def mergesort(lst):
    """Returns a copy of lst with its items re-arranged into ascending order.
    Uses mergesort.
    """
    n = len(lst)
    if n < 2:
        return lst  # already sorted
    else:
        mid = n // 2
        left = lst[:mid]
        right = lst[mid:]
        left_sorted = mergesort(left)    # recursive call
        right_sorted = mergesort(right)  # recursive call
        return merge(left_sorted, right_sorted)

test_sort_fn(mergesort)


#
# Tests on sorting big lists
#
def rand_range(n):
    """Returns a new list with 0, 1, 2, ..., n-1 in random order.
    """
    result = list(range(n))
    random.shuffle(result)
    return result

def sort_compare():
    print('Comparing built-in sort to selection sort and mergesort ...')
    print('Generating random lists ...')
    #sizes = [10, 100, 1000, 10000, 100000]
    sizes = [100*n for n in range(1, 101)]
    data = [rand_range(n) for n in sizes]

    # test built-in sort
    built_in_times = []
    print(f'Testing built-in sort ...')
    for i in range(len(sizes)):
        lst = data[i][:]  # make a copy
        start = time.time_ns()
        lst.sort()
        sort_time = time.time_ns() - start
        built_in_times.append(sort_time)
    # print(built_in_times)

    # test mergesort
    mergesort_times = []
    print(f'Testing mergesort ...')
    for i in range(len(sizes)):
        lst = data[i][:]  # make a copy
        start = time.time_ns()
        mergesort(lst)
        sort_time = time.time_ns() - start
        mergesort_times.append(sort_time)
    # print(mergesort_times)

    # test selection sort
    selection_sort_times = []
    print(f'Testing selection sort ...')
    for i in range(len(sizes)):
        lst = data[i][:]  # make a copy
        start = time.time_ns()
        selection_sort(lst)
        sort_time = time.time_ns() - start
        selection_sort_times.append(sort_time)
    # print(selection_sort_times)

    # print results
    built_in_times = [t/(10**9) for t in built_in_times]
    mergesort_times = [t/(10**9) for t in mergesort_times]
    selection_sort_times = [t/(10**9) for t in selection_sort_times]

    print()
    print('n system mergesort selection')
    for i in range(len(sizes)):
        print(f'{sizes[i]} {built_in_times[i]} {mergesort_times[i]} {selection_sort_times[i]}')

#sort_compare()
