HW_SOURCE_FILE = 'hw04.py'


###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st + ave) * (st + ave + 1) // 2 + ave


def street(inter):
    return w(inter) - avenue(inter)


def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2


w = lambda z: int(((8 * z + 1) ** 0.5 - 1) / 2)


def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    n1_x, n1_y = street(a), avenue(a)
    n2_x, n2_y = street(b), avenue(b)
    return abs(n1_x - n2_x) + abs(n1_y - n2_y)


def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"

    def square(x):
        return x * x

    def search(f, y):
        x = 0
        while True:
            if f(x):
                return x
            elif x > y:
                return False
            x = x + 1

    def inverse(f, y):
        return search(lambda x: f(x) == y, y)

    def find_x(s, f=square):
        ls = []
        for i in s:
            res = inverse(f, i)
            if res:
                ls.append(res)
        return ls

    return find_x(s)


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3 * g(n-3)


def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"

    pre_n1 = 1
    pre_n2 = 2
    pre_n3 = 3
    k = 3

    if n <= 3:
        return n
    elif n > 3:

        if n == 1:
            return pre_n1
        elif n == 2:
            return pre_n2
        elif n == 3:
            return pre_n3
        elif n > 3:
            while k < n:
                k = k + 1
                pre_n3, pre_n1, pre_n2 = pre_n3 + 2 * pre_n2 + 3 * pre_n1, pre_n2, pre_n3
            return pre_n3


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def increase(current_num, count_th):
        if count_th == n:
            return current_num
        elif has_seven(count_th):
            return decrease(current_num-1, count_th+1)
        return increase(current_num+1, count_th+1)

    def decrease(current_num, count_th):
        if count_th == n:
            return current_num
        elif has_seven(count_th):
            return increase(current_num+1, count_th+1)
        return decrease(current_num-1, count_th+1)
    return increase(1, 1)

def has_seven(k):

    if k % 7 == 0:
        return True
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"


###################
# Extra Questions #
###################

from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
