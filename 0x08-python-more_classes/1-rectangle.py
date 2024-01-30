#!/urs/bin/python3


class Rectangle:
    def __init__(self, width=0, height=0):
        # Instantiation with optional width and height
        self.width = width
        self.height = height

    @property
    def width(self):
        # Property to retrieve the width
        return self.__width

    @width.setter
    def width(self, value):
        # Property setter to set the width
        # Width must be an integer, otherwise raise a TypeError exception
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        # Width must be >= 0, otherwise raise a ValueError exception
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        # Property to retrieve the height
        return self.__height

    @height.setter
    def height(self, value):
        # Property setter to set the height
        # Height must be an integer, otherwise raise a TypeError exception
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        # Height must be >= 0, otherwise raise a ValueError exception
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
