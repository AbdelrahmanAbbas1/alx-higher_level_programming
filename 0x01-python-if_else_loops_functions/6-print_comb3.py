#!/usr/bin/python3
for i in range(0, 10):
    for n in range(0, 10):
        if n == i or n <= i:
            continue
        if n == 9 and i == 8:
            print("{}{}".format(i, n))
        else:
            print("{}{},".format(i, n), end=" ")
