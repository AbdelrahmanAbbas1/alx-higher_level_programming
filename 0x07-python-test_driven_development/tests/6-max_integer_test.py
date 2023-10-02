#!/usr/bin/python3
"""Unittest for max_integers([...])
"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([...])"""

    def test_empty(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_max_num(self):
        """Test a list with negative integers"""
        self.assertEqual(max_integer([123, 0, 122, -4, 40]), 123)

    def test_one_el(self):
        """Test a list with one element"""
        self.assertEqual(max_integer([9]), 9)

    def test_int_and_float(self):
        """Test a list with int and float"""
        self.assertEqual(max_integer([1, 15, 15.3, 15.4, 15.7]), 15.7)

    def test_string(self):
        """Test a string"""
        self.assertEqual(max_integer("Hello"), "o")

    def test_list_string(self):
        """Test a list with strings"""
        self.assertEqual(max_integer(["Yes", "Is", "my", "no"]), "no")

    def test_empty_string(self):
        """Test an empty string"""
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
