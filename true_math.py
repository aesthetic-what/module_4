from math import inf


def true_divide(a, b):
    if b == 0:
        return inf
    else:
        res = a / b
        return res

