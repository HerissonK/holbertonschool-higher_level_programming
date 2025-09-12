#!/usr/bin/python3
"""Defines a function to add 2 integers."""


def add_integer(a, b=98):
    """Add 2 integers or floats cast as integers.

    Args:
        a: first number (int or float)
        b: second number (int or float), default = 98

    Returns:
        int: the sum of a and b, casted as integers

    Raises:
        TypeError: if a or b are not int/float
    """
    if type(a) is bool or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if type(b) is bool or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
