def sum_n(n, expression):
    i = 1
    total = 0
    while i <= n:
        total = total + expression(i)
        i = i + 1
    return total


def exp1(k):
    return pow(k, 3)

def exp2(k):
    return 8 / ((4*k - 3) * (4*k - 1))

def sum_cube(n):
    return sum_n(n, exp1)

def sum_exp2(n):
    return sum_n(n, exp2)

