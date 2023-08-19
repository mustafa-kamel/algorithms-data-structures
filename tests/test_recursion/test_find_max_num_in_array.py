from unittest import TestCase

from recursion import find_max_num_in_array


class TestFindMaxNumInArray(TestCase):
    def test_positive_integers(self):
        # Tests that the function correctly finds the maximum number in an array of positive integers
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_max_num_in_array(arr), 5)

    def test_mixed_integers(self):
        # Tests that the function correctly finds the maximum number in an array of mixed positive and negative integers
        arr = [-5, 3, -1, 2, -4]
        self.assertEqual(find_max_num_in_array(arr), 3)

    def test_identical_integers(self):
        # Tests that the function correctly finds the maximum number in an array of identical integers
        arr = [5, 5, 5, 5, 5]
        self.assertEqual(find_max_num_in_array(arr), 5)

    def test_two_integers(self):
        # Tests that the function correctly finds the maximum number in an array of two integers
        arr = [3, 2]
        self.assertEqual(find_max_num_in_array(arr), 3)

    def test_empty_array(self):
        # Tests that the function returns 0 when given an empty array
        arr = []
        self.assertEqual(find_max_num_in_array(arr), 0)

    def test_array_one_integer(self):
        # Tests that the function correctly finds the maximum number in an array of one integer
        arr = [5]
        self.assertEqual(find_max_num_in_array(arr), 5)

    def test_non_integer_elements(self):
        # Tests that the function correctly handles an array of non-integer elements
        arr = [1, 2, 3]
        self.assertEqual(find_max_num_in_array(arr), 3)

    def test_array_with_even_integers(self):
        # Tests that the function correctly finds the maximum number in an array containing only even integers
        arr = [2, 4, 6, 8, 10]
        self.assertEqual(find_max_num_in_array(arr), 10)
