#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    prev_value = 0
    roman_num = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
            }
    if not isinstance(roman_string, str) or None:
        return 0
    for i in reversed(roman_string):
        value = roman_num.get(i, 0)
        if value >= prev_value:
            res = res + value
        else:
            res = res - value
        prev_value = value
    return res
