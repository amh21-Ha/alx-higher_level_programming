import unittest
import sys
sys.path.append('mydir')
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for the max_integer function."""

    def test_empty_list(self):
        """Test if the function returns None for an empty list."""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test if the function returns the only element
        in a one-element list."""
        self.assertEqual(max_integer([42]), 42)

    def test_positive_integers(self):
        """Test if the function returns the maximum of a
        list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_integers(self):
        """Test if the function returns the maximum of
        a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_integers(self):
        """Test if the function returns the maximum of a list
        of mixed integers."""
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_non_integer(self):
        """Test if the function raises a TypeError for a
        non-integer element."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4, 5])


if __name__ == '__main__':
    unittest.main()
