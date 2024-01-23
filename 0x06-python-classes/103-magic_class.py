#!/usr/bin/python3
import math


class MagicClass:
    """A magic class that does the same as the given bytecode"""

    def __init__(self, radius=0):
        """Initialize the magic class with the given radius"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return the area of the circle with the given radius"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle with the given radius"""
        return 2 * math.pi * self.__radius
