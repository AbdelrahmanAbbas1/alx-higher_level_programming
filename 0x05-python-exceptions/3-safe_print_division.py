#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        sum = a / b
    except ZeroDivisionError:
        sum = None
    finally:
        print("Iniside result: {}".format(sum))
        return sum
