In these notes, we are doing an experiment to test what is the most efficient
way to do linear in Python. [search_test.py](search_test.py) contains all the
functions and test code.

Recall the following facts about searching and sorting:

- When looking for a target item $$x$$ on a list with $$n$$ items, **linear
  search** checks the items one at a time, usually in order from left to right.
  So in the *worst* it will do $$n$$ comparisons. On average, it will do about
  $$n/2$$ comparisons. Thus the running time of linear search is proportional to
  the $$n$$, the length of the list.

- When looking for a target item $$x$$ on a *sorted* list with $$n$$ items,
  **binary search**, in the *worst* case, runs in time proportional to $$\log_2
  n$$. This is much faster than $$n$$ in general, and so, if you have the
  choice, you should use binary search instead of linear search. However,
  getting the data into sorted order is more expensive than sorting, e.g. a fast
  sorting algorithm like **mergesort** runs in time proportional to $$n\log_2
  n$$, which is slower than calling binary search.


## Multiple Implementations

6 different implementations of a "contains" function that tests if some value
`x` is in a list. There are two important exceptions to be aware of:

  - `contains_recursive_linear` is a simple recursive implementation of linear
    search that only works if the list being searched has less than about 1000
    items. If the list has too many items, then Python automatically stops it.

  - `contains_recursive_binary` is a recursive implementation of *binary*
    search, so it requires that the list items be in ascending sorted order.

## Correctness Testing

In [search_test.py](search_test.py), the function `test_contains(contains)`
checks that the passed-in `contains` function works correctly by checking that
few cases return the correct answer:

```python
def test_contains(contains):
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
```

Note a couple of things:

- `test_contains` does **unit testing**, i.e. it tests the single function
  *contains* on its own, and not inside some larger program. Many of the test
  test cases are "edge" cases, i.e. they test values near the start/end of the
  list. Bugs often hide in such places.

- It's possible that `test_contains` could return "passed" for a `contains`
  function that has a bug in it. That's because no reasonable *finite* amount of
  testing can prove that a function like this works correctly. It's always
  possible that it fails for a case we didn't think of.

- In Python, if `f` is a function then `f.__name__` is the name of the function
  when it was defined. This is a neat trick that makes it easy to print which
  function is being tested.


## Performance Testing

When we have multiple implementations of a function that we know are correct,
then we may still want to know which one is fastest. So
[search_test.py](search_test.py) contains this function:

```python
def test_performance():
    contains_functions = [contains_builtin, 
                          contains_for_each, 
                          contains_for_range, 
                          contains_while, 
                          #contains_recursive_linear,  
                          contains_recursive_binary]

    lst = list(range(1000000))
    print()
    for contains in contains_functions:
        print(f'testing:  {contains.__name__:25}  ', end='')
        start = time.time()
        for i in range(10):
            contains(-1, lst)
        elapsed_time = time.time() - start
        print(f'{elapsed_time:.2f} seconds')
```

Some things to note:

- In Python, functions are values, and so you can store them in a list as is
  done here. This makes it easy to loop through the list and test each function
  individually.

- The function `contains_recursive_linear` is commented out because it gets
  stopped by Python after about 1000 recursive calls, and so it can't run on a
  large list like `lst`.

- We always search for the value -1, which is guaranteed to *not* be on the
  list. This forces the functions to do the same amount of work.

- The function `time.time()` returns the current time in seconds. Calling it
  before and after running the tests lets us calculate the total elapsed time.

Here's the output on my computer:

```
testing:  contains_builtin           0.06 seconds
testing:  contains_for_each          0.16 seconds
testing:  contains_for_range         0.29 seconds
testing:  contains_while             0.82 seconds
testing:  contains_recursive_binary  0.07 seconds
```

The built-in `in` function is the fastest, followed by the recursive binary
search. The comparison is unfair, though: they are using very different
algorithms to solve the same problem. The implementation of binary search in
[search_test.py](search_test.py) is not very efficient because it uses list
slicing, and each slice makes a copy. Despite the inefficiency of slicing,
binary search does so much less work than linear search that the overall running
time is comparable to the built-in `in` function.

Of course, the [achilles heel](https://en.wikipedia.org/wiki/Achilles%27_heel)
of binary search is that it only works if the list is sorted, and getting the
list into sorted order takes more work than just searching it.
