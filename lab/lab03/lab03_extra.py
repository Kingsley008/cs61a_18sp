""" Optional problems for Lab 3 """

from lab03 import *


## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"

    def calculate_mode(n):
        def calculate(x, f1=f1, f2=f2, f3=f3, count=n):
            first = f1
            second = f2
            third = f3
            if count == 0:
                return x
            if count > 0:
                x = first(x)
                first, second, third = second, third, first
                return calculate(x, first, second, third, count - 1)

        return calculate

    return calculate_mode


## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0

    def find_max(x, max=1):
        while x > 9:
            x = x // 10
            max = max * 10
        return max

    max_num = find_max(x)
    f = lambda x, max_num, current_v: x % 10 * max_num + current_v
    current_max = max_num
    while x > 0:
        x, y = x // 10, f(x, current_max, y)
        current_max = current_max // 10
    return y == n


## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_mul(n - 2)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"

    def helper(n, count=0, num_d=1):
        if n % num_d == 0:
            count = count + 1
        if num_d == n and count > 2:
            return False
        elif num_d == n and count == 2:
            return True
        return helper(n, count, num_d + 1)

    return helper(n)


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"

    def helper_odd(k=1, total=0):
        if k > n:
            return total
        else:
            total = total + odd_term(k)
            return helper_even(k + 1, total)

    def helper_even(k, total):
        if k > n:
            return total
        else:
            total = total + even_term(k)
            return helper_odd(k + 1, total)
    return helper_odd()


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def helper(count, n):

        return helper()
