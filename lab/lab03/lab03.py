""" Lab 3: Recursion and Midterm Review """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if b == 0:
        return a
    if a >= b:
        res = a % b
        return gcd(b, res)
    elif a < b:
        res = b % a
        return gcd(a, res)

x = []

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

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
    print(n)
    if n == 1:
        x.append(1)
        return x.__len__()
    if n % 2 == 0:
        res = n // 2
        x.append(n)
        return hailstone(res)
    else:
        res = n * 3 + 1
        x.append(n)
        return hailstone(res)
