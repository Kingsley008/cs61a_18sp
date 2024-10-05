""" Optional Questions for Lab 11 """
from lab11 import *

# Q5
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while True:
        if n == 1:
            yield n
            break
        elif n % 2 == 0:
            yield n
            n = n // 2
        else:
            yield n
            n = 3 * n + 1

# Q6
def repeated(t, k):
    """Return the first value in iterable T that appears K times in a row.

    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(trap(s, 7), 2)
    4
    >>> repeated(trap(s, 10), 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    count = 1
    pre = ' '
    t = iter(t)
    while True:
        i = next(t)
        if i == pre:
            count = count + 1
            if count == k:
                return pre
        else:
            pre = i


# Q7
def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1, removing
    repeats. Assume that s0 and s1 have no repeats. s0 or s1 may be infinite
    sequences.

    >>> m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    >>> def big(n):
    ...    k = 0
    ...    while True: yield k; k += n
    >>> m = merge(big(2), big(3))
    >>> [next(m) for _ in range(11)]
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0, None), next(i1, None)
    "*** YOUR CODE HERE ***"
    while True:
        if e0 is None and e1 is None:
            return
        elif e0 is None:
            yield e1
            e1 = next(i1, None)
            continue
        elif e1 is None:
            yield e0
            e0 = next(i0, None)
            continue
        if e0 == e1:
            yield e0
            e0, e1 = next(i0, None), next(i1, None)
        elif e0 > e1:
            yield e1
            e1 = next(i1, None)
            continue
        elif e1 > e0:
            yield e0
            e0 = next(i0, None)
            continue


# Q8
def remainders_generator(m):
    """
    Takes in an integer m, and yields m different remainder groups
    of m.

    >>> remainders_mod_four = remainders_generator(4)
    >>> for rem_group in remainders_mod_four:
    ...     for _ in range(3):
    ...         print(next(rem_group))
    0
    4
    8
    1
    5
    9
    2
    6
    10
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    total = 0

    def higher_fuc(n):
        num = 0
        while True:
            if n == 0:
                yield num * m
            else:
                yield num*m + n
            num = num + 1

    for _ in range(m):
        yield higher_fuc(total)
        total = total + 1

# Q9
def zip_generator(*iterables):
    """
    Takes in any number of iterables and zips them together.
    Returns a generator that outputs a series of lists, each
    containing the nth items of each iterable.
    >>> z = zip_generator([1, 2, 3], [4, 5, 6], [7, 8])
    >>> for i in z:
    ...     print(i)
    ...
    [1, 4, 7]
    [2, 5, 8]
    """
    "*** YOUR CODE HERE ***"
    # *iterables is a tuple
    iters = [iter(x) for x in iterables]
    while True:
        index = 0
        ls = []
        for x in iters:
            try:
                ls.append(next(x))
            except Exception as e:
                return
        yield ls
        index = index + 1
