#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
    Returns a list of attributes and methods of the given object.
    param obj: Any Python object
    :return: List of attribute and method names
    """
    return dir(obj)
