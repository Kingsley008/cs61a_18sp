def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])


#############
# Questions #
#############

def replace_leaf(t, old, new):
    """Returns a new tree where every leaf value equal to old has
    been replaced with new.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('loki')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        loki
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    "*** YOUR CODE HERE ***"
    n_t = copy_tree(t)

    def helper(n_t, old, new):
        if is_leaf(n_t) and label(n_t) == old:
            n_t[0] = new
        else:
            for b in branches(n_t):
                helper(b, old, new)
        return n_t

    return helper(n_t, old, new)


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

    def TOH(n, start=1, cushion=2, end=3):
        if n == 1:
            print_move(start, end)
        else:
            TOH(n - 1, start, end, cushion)
            TOH(1, start, cushion, end)
            TOH(n - 1, cushion, start, end)

    TOH(n)


###########
# Mobiles #
###########

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree('mobile', [left, right])


def is_mobile(m):
    return is_tree(m) and label(m) == 'mobile'


def sides(m):
    """Select the sides of a mobile."""
    assert is_mobile(m), "must call sides on a mobile"
    return branches(m)


def is_side(m):
    return not is_mobile(m) and not is_weight(m) and type(label(m)) == int


def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])


def length(s):
    """Select the length of a side."""
    assert is_side(s), "must call length on a side"
    return label(s)


def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    assert is_side(s), "must call end on a side"
    return branches(s)[0]


def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return ['weight', [size]]


def size(w):
    """Select the size of a weight."""
    "*** YOUR CODE HERE ***"
    return w[1][0]


def is_weight(w):
    """Whether w is a weight, not a mobile."""
    "*** YOUR CODE HERE ***"
    return is_tree(w) and label(w) == 'weight'


def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a weight"
        return sum([total_weight(end(s)) for s in sides(m)])


def get_side(direction, m):
    assert is_mobile(m)
    if direction == 'right':
        return m[2][0]
    if direction == 'left':
        return m[1][0]


def get_side_len(s):
    assert is_side(s)
    return s[0]


def get_m_by_side(s):
    assert is_side(s)
    return s[1]


def get_left_side(m):
    assert is_mobile(m)
    return tree(m[1])


def get_right_side(m):
    assert is_mobile(m)
    return tree(m[2])


def next_side(tree):
    """return a list of branches """
    return tree[1:]


def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    "*** YOUR CODE HERE ***"

    # length multiplied by the total weight

    ls = []

    def weight_helper(m, side_fn=sides):
        if is_weight(m):
            return size(m)
        else:
            assert is_mobile(m), "must get total weight of a mobile or a weight"
            return sum([weight_helper(end(i)) for i in side_fn(m)])

    # def len_helper(s):
    #     assert is_side(s)
    #     ls.append(s[0])
    #     if is_mobile(get_m_by_side(s)):
    #         for s in next_side(next_side(s)[0]):
    #             len_helper(s)
    #     return sum(ls)

    def sub_helper(m):
        if is_mobile(m):
            for s in sides(m):
                if not balanced(end(s)):
                    return False
            return True
        else:
            return True

    if is_weight(m):
        return True
    total_weight_right = weight_helper(m, get_right_side)
    total_weight_left = weight_helper(m, get_left_side)
    total_len_right = get_side('right', m)
    total_len_left = get_side('left', m)

    if (total_weight_left * total_len_left) == (total_weight_right * total_len_right) and sub_helper(m):
        return True
    else:
        return False


#######
# OOP #
#######

class Account:
    """An account has a balance and a holder.

    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02

    >>> a.time_to_retire(10.25) # 10 -> 10.2 -> 10.404
    2
    >>> a.balance               # balance should not change
    10
    >>> a.time_to_retire(11)    # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """

    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0

        "*** YOUR CODE HERE ***"
        interest = self.interest
        day_count = 0
        balance_add_profit = self.balance
        while True:
            if balance_add_profit > amount:
                break
            else:
                balance_add_profit = balance_add_profit + balance_add_profit * interest
                day_count = day_count + 1
        return day_count


class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!

    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # First one's free
    'Insufficient funds'
    >>> ch.withdraw(3)    # And the second
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Ok, two free withdrawals is enough
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    'Insufficient funds'
    """
    withdraw_fee = 1
    free_withdrawals = 2
    "*** YOUR CODE HERE ***"

    def withdraw(self, amount):
        if self.free_withdrawals > 0:
            if amount > self.balance:
                self.free_withdrawals = self.free_withdrawals - 1
                return 'Insufficient funds'
            self.balance = self.balance - amount
            self.free_withdrawals = self.free_withdrawals - 1
            return self.balance
        else:
            if amount + self.withdraw_fee > self.balance:
                return 'Insufficient funds'
            else:
                self.balance = self.balance - amount - self.withdraw_fee
                return self.balance


############
# Mutation #
############

def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    "*** YOUR CODE HERE ***"
    count_ls = []
    obj = []

    def counter(n_obj):
        nonlocal count_ls
        nonlocal obj
        if n_obj not in obj:
            obj.append(n_obj)
            index = obj.index(n_obj)
            count_ls.append(1)
            return count_ls[index]
        elif n_obj in obj:
            index = obj.index(n_obj)
            count_ls[index] = count_ls[index] + 1
            return count_ls[index]

    return counter


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    "*** YOUR CODE HERE ***"
    n = 0

    def fib():
        nonlocal n
        if n == 0:
            n = n + 1
            return 0
        k = 0
        pre = 0
        cur = 1
        while k < n:
            cur, pre = cur + pre, cur
            k = k + 1
        n = n + 1
        return pre

    return fib


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    error_list = []

    def withdraw(amount, psw):
        nonlocal balance
        nonlocal error_list
        # check password
        if len(error_list) >= 3:
            return 'Your account is locked. Attempts: ' + str(error_list)
        elif psw != password:
            error_list.append(psw)
            return 'Incorrect password'
        else:
            if amount > balance:
                return 'Insufficient funds'
            else:
                balance = balance - amount
                return balance

    return withdraw


def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"

    ret = withdraw(0, old_password)
    passw = {}
    if type(ret) == int:
        passw[new_password] = old_password

        def process(amount, password):
            return withdraw(amount, passw.get(password, password))
        return process
    else:
        return ret






###################
# Extra Questions #
###################

def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]


def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]


def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))


def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)


def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = x[0] * y[0]
    p2 = x[0] * y[1]
    p3 = x[1] * y[0]
    p4 = x[1] * y[1]
    return [min(p1, p2, p3, p4), max(p1, p2, p3, p4)]


def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    "*** YOUR CODE HERE ***"
    p1_min = x[0] - y[1]
    p2_min = y[0] - x[1]
    p1_max = x[1] - y[0]
    p2_max = y[1] - x[0]

    return [min(p1_min,p2_min), max(p1_max, p2_max)]


def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    "*** YOUR CODE HERE ***"
    reciprocal_y = interval(1 / upper_bound(y), 1 / lower_bound(y))
    return mul_interval(x, reciprocal_y)


def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))


def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))


def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(1, 1)  # Replace this line!
    r2 = interval(1, 1)  # Replace this line!
    return r1, r2


def multiple_references_explanation():
    return """The multiple reference problem..."""


def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"


def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"
