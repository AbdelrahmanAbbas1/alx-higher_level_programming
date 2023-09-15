#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    u_dic = {}
    for x, y in a_dictionary.items():
        u_dic[x] = y ** 2
    return u_dic
