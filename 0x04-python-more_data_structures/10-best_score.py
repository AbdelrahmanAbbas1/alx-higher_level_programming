#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    n = 0
    bs = None
    for x, y in a_dictionary.items():
        if y > n:
            n = y
            bs = x
    return bs
