#!/usr/bin/python3
def pow(a, b):
    res = 1
    if b > 0:
        for i in range(b):
            res = res * a
    elif b < 0:
        b = b * -1
        for i in range(b):
            res = res * (1 / a)
    else:
        res = 1
    return res
