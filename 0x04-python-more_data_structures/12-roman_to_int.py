#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    roman_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if roman_string is None:
        return 0
    for i in roman_string:
        for x, y in roman_num.items():
            if i == x:
                num = num + y
            else:
                continue
    return num
