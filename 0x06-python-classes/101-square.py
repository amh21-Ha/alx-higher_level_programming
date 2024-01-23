#!/usr/bin/python3
class Square:
    """A square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and optional position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter to set position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """Printing a Square instance should have the same behavior as my_print()"""
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            result += "\n" * self.__position[1]
            for i in range(self.__size):
                result += " " * self.__position[0]
                result += "#" * self.__size + "\n"
        return result[:-1]
