#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices and returns the result.

    Args:
        m_a: The first matrix. Must be a list of lists of integers or floats.
        m_b: The second matrix. Must be a list of lists of integers or floats.

    Returns:
        A new matrix that is the product of m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists, contains
        non-numeric elements, or has rows of different sizes.
        ValueError: If m_a or m_b is empty, or if m_a and m_b
        cannot be multiplied.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(
            isinstance(row, list) for row in m_b):
        raise TypeError(
                "m_a must be a list of lists or m_b must be a list of lists"
                )

    if not m_a or not m_b or not any(m_a) or not any(m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(
            isinstance(elem, (
                int, float)) for row in m_a for elem in row) or not all(
                        isinstance(
                            elem, (
                                int, float)) for row in m_b for elem in row):
        raise TypeError(
                """m_a should contain only integers or floats or m_b should
                contain only integers or floats"""
                )

    if not all(
            len(row) == len(m_a[0]) for row in m_a) or not all(
                    len(row) == len(m_b[0]) for row in m_b):
        raise TypeError(
                "each row of m_a must be of the same size or each row of m_b must be of the same size"
                )

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
