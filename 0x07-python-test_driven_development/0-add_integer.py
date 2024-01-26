#!/usr/bin/python3
"""
This module contains a function that adds 2 integers.
"""

def add_integer(a, b=98):
    """
    This function adds 2 integers or floats and returns an integer.
    If a or b are not integers or floats, it raises a TypeError exception.
    If a or b are floats, they are casted to integers before the addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
