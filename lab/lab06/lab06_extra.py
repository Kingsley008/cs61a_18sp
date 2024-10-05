def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    "*** YOUR CODE HERE ***"
    snacks_list = list(snacks)
    snacks_list.reverse()

    def cast_snack():
        nonlocal snacks_list
        if len(snacks_list) == 0:
            snacks_list = list(snacks)
            snacks_list.reverse()
        return snacks_list.pop()

    return cast_snack
