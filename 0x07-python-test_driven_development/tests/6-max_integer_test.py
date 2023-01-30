#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_int(self):
        """Test positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_neg(self):
        """Test negative integers"""
        self.assertEqual(max_integer([-16, -8, -2, -25]), -2)

    def test_empty(self):
        """Test empty list"""
        self.assertEqual(max_integer([]), None)

    def test_float(self):
        """Test floating numbers"""
        self.assertEqual(max_integer([2.1, -1.4, -3.777, 0.1], 2.1)

    def test_single(self):
        """Test single input"""
        self.assertEqual(max_integer([21]), 21)

    def test_string(self):
        """Test string"""
        self.assertEqual(max_integer("Mignolet"), 't')

    def test_string_list(self):
        """Test list of strings"""
        self.assertEqual(max_integer(["Mane", "Firmino", "Salah"]), "Salah")

if __name__ == '__main__':
    unittest.main()
