#!/usr/bin/python3
"""This module contains a class that represents a square."""


class Square:
    """A class that represents a square.

    Attributes:
        __size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes a square object with an optional size.

        Args:
            size (float or int, optional): The size of the square.
            Defaults to 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Returns the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Compares two squares for equality based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares have the same area, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Compares two squares for inequality based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares have different areas, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Compares two squares for greater than relation based on their
        areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the first square has a larger area than the
            second, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Compares two squares for greater than or equal to relation based
        on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the first square has a larger or equal area than
            the second, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compares two squares for less than relation based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the first square has a smaller area than the second,
            False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Compares two squares for less than or equal to relation based
        on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the first square has a smaller or equal area than
            the second, False otherwise.
        """
        return self.area() <= other.area()
