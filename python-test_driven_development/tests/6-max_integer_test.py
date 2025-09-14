#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """contains test functions for max_integer function"""

    def test_success_cases(self):
        """tests successful cases of max_integer"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertIsNone(max_integer([]))  # liste vide
        self.assertEqual(max_integer([1]), 1)  # un seul élément
        self.assertEqual(max_integer([1, 1, 3, 3, 3, 6, 8, 8]), 8)  # doublons
        self.assertEqual(max_integer([-1, -2, -3]), -1)  # nombres négatifs
        self.assertEqual(max_integer([1, 2, 3, 4, 3, 2, 1]), 4)  # max au milieu
        self.assertEqual(max_integer([100, 50, 25]), 100)  # max au début
        self.assertEqual(max_integer([-10, -50, -2]), -2)  # max négatif

    def test_type_errors(self):
        """tests errors raised by incorrect type arguments"""
        with self.assertRaises(TypeError):
            max_integer(["string", 1.73, 25, {2}])

    def test_no_argument(self):
        """tests when function is called without arguments"""
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
