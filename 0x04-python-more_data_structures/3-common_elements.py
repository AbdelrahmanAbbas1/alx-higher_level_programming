#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_list = []
    for i in set_1:
        for x in set_2:
            if i == x:
                c_list.append(i)
            else:
                continue
    c_set = set(c_list)
    return c_set
