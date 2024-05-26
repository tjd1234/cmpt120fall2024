# Lecture 26 Notes

## The Binary Search Algorithm

**Binary search** is a divide-and-conquer search algorithm. Given a list of
values that is in ascending sorted order, it quickly finds the index of a target
value $x$ in the list, or returns -1 if $x$ is not in the list. It is much
faster than linear search, especially for large lists.

It works like this:
- Check if the middle-most element of the list is equal to $x$. If so, we're
  done.
- If $x$ is less than the middle element, then $x$ must be in the left half of
  the list. So we apply binary search to the left half.
- If $x$ is greater than the middle element, then $x$ must be in the right half
  of the list. So we apply binary search to the right half.

For example, suppose the list is `[0, 2, 3, 4, 8, 9, 10]` and you want to find
the number 5. We will use variables `lo` and `hi` to keep track of the current
sub-list that is being searched. Initially, we search the entire list:

```
looking for x = 5

[0, 2, 3, 4, 8, 9, 10]
 ^                  ^
 |                  |
lo                  hi
```

The middle element is 4. Since 5 is greater than 4, if 5 is in the list it must
be in the right half. So adjust `lo`:

```
looking for x = 5

[0, 2, 3, 4, 8, 9, 10]
             ^     ^
             |     |
            lo    hi
```

The middle element of the current sub-list is 9. Since 5 is less than 9, if 5 is
in the list it must be in the left half. So we adjust `hi`:

```
looking for x = 5

[0, 2, 3, 4, 8, 9, 10]
             ^
             |     
            lo, hi
```

Both `lo` and `hi` are pointing to the same element, and that element is not 5.
So we're done: 5 is not in the list.


Here is an implementation of binary search:

```python
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
```

Binary search is notoriously tricky to implement. The idea is not difficult once
you understand it, but getting every little detail exactly right is not so easy.
So be sure to carefully test it!

See [searching.py](../lecture25/searching.py) for an implementation.


## Comparing Linear Search and Binary Search

How fast are linear search and binary search? Here's the results of an
experiment showing how their real time performance compares:

![sorting time line graph for linear and binary search](searchRealTimeGraph_small.png)

This shows clearly that are linear search is much slower than both the built-in
`index` and binary search. The linear search graph is not perfectly smooth since
the computer running the experiment is doing other things at the same time, and
occasionally it slows down or speeds up.

When computer scientists study algorithms theoretically, *actual* running time
is usually *not* a good way to measure performance. Actual running time depends
too much on the speed of the computer, and whatever else it might be doing at
the same time. Instead, computer scientists simplify things by choosing a **key
instruction** in the code, and then count how many times that instruction is
executed. If you choose a good key instruction, the resulting performance graphs
have the same shape as the actual running time graphs.

For searching and sorting algorithms, experience shows that *comparisons* are a
good key instruction. For linear search, we count how many times `==` is
executed, and for binary search we count how many times `<=` is executed.

So when a computer scientists talks about the performance of linear search and
binary search, they usually mean *how many comparisons they do*.

Suppose you run `linear_search` on a list with 100 elements. Then:

- **Best case**: the *minimum* number of comparisons `linear_search` does is
  1, in the case where the first element is $x$
- **Worst case**: the *maximum* number of comparisons `linear_search` does is
  100, either when $x$ is the last element, or not in the list at all
- **Average case**: the *average* number of comparisons `linear_search` does is
  about $\frac{100}{2}=50$, assuming randomly ordered data; the reason for
  this is that you will find $x$ using a couple of comparisons just as often
  as you will find $x$ using around 100 comparisons, and overall it's as if
  you are searching half-way through the list each time

In general, for $n$ items linear search does 1 comparison in the best case,
$n$ comparisons in the worst case, and about $\frac{n}{2}$ in the average
case.

In practice, it's wise to always assume the worst case for linear search. The
best case happens rarely (about a 1 in $n$ chance), and the average and worst
cases are much more common. So we usually just say linear search does $n$
comparisons. Since the expression $n$ is a *linear expression*, we also say that
linear search is a **linear time** algorithm.

> We will follow the maxim "Hope for the best, but prepare for the worst". 

Assuming your list is in sorted order, binary search usually does vastly fewer
comparisons than linear search. In general, if your list has $n$ items then
binary search performs like this:

- **Best case**: the *minimum* number of comparisons `binary_search` does is
  1, in the case where the middle element is $x$
- **Worst case**: the *maximum* number of comparison `binary_search` does is
  about $\log_2 n$
- **Average case**: the *average* number of comparisons `binary_search` does
  is about $\log_2 n$

To get an idea of how much better binary search is, look at this table:

| **n**    | **log2 n** |
|----------|------------|
|    16    |      4     |
|    32    |      5     |
|    64    |      6     |
|    128   |      7     |
| 1048576  |     20     |

1048576 is $2^{20}$, which is just over a million. If you have a sorted list
of a million values, then, in the worst case, linear search would do 1048576
comparisons. But binary search would, in the worst case, only do about $\log_2
1000000 \approx 20$ comparisons. So if you have the choice, especially with
large amounts of data, you should always using binary search instead of linear
search.

See [searching.py](../lecture25/searching.py) for code that counts comparisons
of linear and binary search. 
