#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    el_number = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            el_number += 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            break
    print()
    return el_number