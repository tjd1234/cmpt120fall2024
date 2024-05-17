# quiz.py

def count_odd(lst):
    """Returns the number of odd numbers in list lst.
    Constraint: Not allowed to use a for-loop!
    >>> count_odd([])
    0
    >>> count_odd([5, -3, 2, 1, 0])
    3
    """
    result = 0
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 1:
            result += 1
        i += 1
    return result

def count_odd_bonus(lst): 
    """A clever implementation using a generator expression.    
    Generator expressions like this are not part of the course. It's only an
    example of neat solution.
    """
    return sum(n for n in lst if n % 2 == 1)


def parity_split_1(lst_num):
    """Returns a list of even numbers, and odd numbers, in a list.
    Assumes lst is a list of 0 or more numbers.
    It returns a list contain two lists: 

    - the first list is all the even numbers that appear in lst, sorted in
      descending order (biggest to smallest)
    - the second list is all the odd numbers that appear in lst, sorted in
      descending order (biggest to smallest)

    >>> parity_split_1([])
    [[], []]
    >>> parity_split_1([1,2,3,4,5])
    [[4, 2], [5, 3, 1]]
    >>> parity_split_1([0, 3, 5, 6, 6, -4])
    [[6, 6, 0, -4], [5, 3]]
    """
    odds = []
    evens = []
    for n in lst_num:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)
    odds.sort()
    odds.reverse()
    evens.sort()
    evens.reverse()
    return [evens, odds]

def parity_split_2(num_lst):
    """Returns a list of even numbers, and odd numbers, in a list.    
    In this implementation, the entire list is sorted first at the beginning
    instead of at the end.

    >>> parity_split_2([])
    [[], []]
    >>> parity_split_2([1,2,3,4,5])
    [[4, 2], [5, 3, 1]]
    >>> parity_split_2([0, 3, 5, 6, 6, -4])
    [[6, 6, 0, -4], [5, 3]]
    """
    num_lst.sort()
    num_lst.reverse()
    odds = []
    evens = []
    for n in num_lst:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)

    return [evens, odds]
