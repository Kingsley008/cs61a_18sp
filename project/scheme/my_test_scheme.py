import scheme_reader
from cs61a.lab.lab11.lab11 import naturals
from scheme_reader import *
from collections import Iterable
from scheme import *

env = create_global_frame()
from collections import Iterable

str1 = '(define x 5)'


# expr1 = read_line(str1)
# a = scheme_eval(expr1, env)


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


z = zip_generator([1, 2, 3], [4, 5, 6], [7, 8])

for i in z:
    print(i)
