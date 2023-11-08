#!/usr/bin/python3
"""This module defines a function"""


def write_file(filename="", text=""):
    """This function write a string to a file

        Args:
            filename (str): The name of the file
            text (str): The text to be written in the file

        Retrun:
            The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        size = f.write(text)
    return size
