#!/usr/bin/python3
"""This module contains a class that represents a square."""


class Square:
    """A class that represents a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple of int): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square object with an optional size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple of int, optional): The position of the square.
            Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a
            tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position of the square.

        Returns:
            tuple of int: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple of int): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(
                isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #.

        Prints an empty line if the size is 0.
        Uses spaces to adjust the position of the square.

        Args:
            None
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
