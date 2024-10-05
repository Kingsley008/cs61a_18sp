"""Lab 2: Lambda Expressions and Higher Order Functions"""
# Lambda Functions

from operator import add

def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """
    def fuc1(x):
        def fuc2(y):
            return func(x, y)
        return fuc2
    return fuc1

curried_add = lambda_curry2(add)

add_three = curried_add(3)

add_three(5)
