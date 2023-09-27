#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        [print(my_list[i], end="") for i in range(x)]
    except IndexError:
        x = len(my_list)
    finally:
        print()
        return x
