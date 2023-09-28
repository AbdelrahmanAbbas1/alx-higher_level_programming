#!/usr/bin/python3
import calculator_1 as cal
from sys import argv
if __name__ == "__main__":
    if len(argv) != 4:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = {"+": cal.add, "-": cal.sub, "*": cal.mul, "/": cal.div}
    if argv[2] in ops:
        a = int(argv[1])
        b = int(argv[3])
        res = (ops[argv[2]](a, b))
        print("{} {} {} = {}".format(a, argv[2], b, res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
