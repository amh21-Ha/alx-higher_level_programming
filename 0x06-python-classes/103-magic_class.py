#!/usr/bin/python3
import math


class MagicClass:
    """A class that represents a circle.

    Attributes:
        __radius (float or int): The radius of the circle.
    """

    def __init__(self, radius=0):
        """Initializes a circle object with a given radius.

        Args:
            radius (float or int, optional): The radius of the circle.
            Defaults to 0.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
