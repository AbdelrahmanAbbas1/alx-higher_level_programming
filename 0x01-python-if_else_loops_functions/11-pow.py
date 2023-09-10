#!/usr/bin/python3
def pow(a, b):
    if b > 0:
        return a ** b
    elif b < 0:
        return 1 / (a ** (-b))
    else:
        return 1
