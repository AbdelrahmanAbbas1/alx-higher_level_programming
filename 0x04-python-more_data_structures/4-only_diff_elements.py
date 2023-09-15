#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    d_list_1 = set_1 - set_2
    d_list_2 = set_2 - set_1
    d_list = list(d_list_1) + list(d_list_2)
    d_set = set(d_list)
    return d_set
