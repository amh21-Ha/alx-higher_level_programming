#!/urs/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies two matrices using numpy.matmul
    Args:
        m_a: a list of lists representing a matrix
        m_b: a list of lists representing a matrix
    Returns:
        a numpy array representing the matrix product of m_a and m_b
    Raises:
        TypeError: if m_a or m_b are not lists or if their elements are not
        lists
        ValueError: if m_a or m_b are empty or if their shapes are not
        compatible for multiplication
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be a list of lists")

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a and m_b can't be empty")

    for row in m_a + m_b:
        if not isinstance(row, list):
            raise TypeError("m_a and m_b should contain only lists")

    m_a = np.array(m_a)
    m_b = np.array(m_b)

    if m_a.shape[1] != m_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)
