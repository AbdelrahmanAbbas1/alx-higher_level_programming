#!/usr/bin/python3
"""This module defines a function"""


def append_write(filename="", text=""):
    """This function append a text to a file

        Args:
            filename (str): The name of the file
            text (str): The text to be appended
        Return:
            The number of the characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        size = f.write(text)

    return size
