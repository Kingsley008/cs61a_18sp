HW_SOURCE_FILE = 'hw02.py'

def square(x):
    return x * x

def identity(x):
    return x

triple = lambda x: 3 * x

increment = lambda x: x + 1

add = lambda x, y: x + y

mul = lambda x, y: x * y

def product(n, term):
    """Return the product of the first n terms in a sequence.
    n    -- a positive integer
    term -- a function that takes one argument

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    count = 0
    total = 1
    while count < n:
        count = count + 1
        total = total * term(count)
    return total

# The identity function, defined using a lambda expression!
identity = lambda k: k

def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)
    24
    >>> factorial(6)
    720
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'factorial', ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n >= 0:
        return product(n, identity)
    else:
        return Exception

def make_adder(n):
    """Return a function that takes an argument K and returns N + K.

    >>> add_three = make_adder(3)
    >>> add_three(1) + add_three(2)
    9
    >>> make_adder(1)(2)
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda k: k+n
    # def adder(k):
    #     return n + k
    # return adder
