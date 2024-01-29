#!/usr/bin/python3
def print_square(size):
    """Prints a square with the character #.

    Args:
        size: The size length of the square. Must be an integer.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    print("#" * size)
    for i in range(size - 2):
        print("#" + " " * (size - 2) + "#")

    if size > 1:
        print("#" * size)
