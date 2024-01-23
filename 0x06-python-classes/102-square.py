#!/usr/bin/python3
class Square:
    """A square"""

    def __init__(self, size=0):
        """Instantiation with size"""
        self.size = size

    @property
    def size(self):
        """Property to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set size"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare two squares based on their area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare two squares based on their area"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare two squares based on their area"""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare two squares based on their area"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare two squares based on their area"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare two squares based on their area"""
        return self.area() >= other.area()
