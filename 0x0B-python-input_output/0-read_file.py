#!/usr/bin/python3
"""This module defines a function"""


def read_file(filename=""):
    """This function reads a file

        Args:
            filename (str): The name of the file to be read
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
