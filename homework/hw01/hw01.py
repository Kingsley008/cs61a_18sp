from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """

    def return_abs(c, d):
        return c + d * -1

    def return_normal(c, d):
        return c + d

    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """

    def square(a):
        return a * a

    if a <= b and a <= c:
        return square(b) + square(c)
    elif b <= a and b <= c:
        return square(a) + square(c)
    elif c <= a and c <= b:
        return square(a) + square(b)


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    max_factor = 1
    factor = 1
    while factor <= n - 1:
        if n % factor == 0:
            max_factor = factor
        factor = factor + 1
    return max_factor


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()


def with_if_function():
    return if_function(c(), t(), f())


def c():
    "*** YOUR CODE HERE ***"
    return True


def t():
    "*** YOUR CODE HERE ***"
    return 1


def f():
    "*** YOUR CODE HERE ***"
    return 0


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """

    "*** YOUR CODE HERE ***"
    count = 0
    while 1:
        print(n)
        count = count + 1
        if n % 2 == 0:
            n = n // 2
        elif n == 1:
            return count
        else:
            n = n * 3 + 1
