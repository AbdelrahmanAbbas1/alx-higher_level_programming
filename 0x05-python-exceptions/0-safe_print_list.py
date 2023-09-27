#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        [print(my_list[i], end="") for i in range(x)]
    except IndexError:
        k = 0
        for i in my_list:
            k += 1
        x = k
    finally:
        print()
        return x
