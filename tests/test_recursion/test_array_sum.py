from unittest import TestCase

from recursion import array_sum


class TestArraySum(TestCase):
    def test_positive_integers(self):
        # Tests that the function correctly sums an array of positive integers
        arr = [1, 2, 3, 4, 5]
        result = array_sum(arr)
        self.assertEqual(result, 15)

    def test_negative_integers(self):
        # Tests that the function correctly sums an array of negative integers
        arr = [-1, -2, -3, -4, -5]
        result = array_sum(arr)
        self.assertEqual(result, -15)

    def test_mixed_integers(self):
        # Tests that the function correctly sums an array of mixed positive and negative integers
        arr = [1, -2, 3, -4, 5]
        result = array_sum(arr)
        self.assertEqual(result, 3)

    def test_length_1(self):
        # Tests that the function correctly sums an array of length 1
        arr = [10]
        result = array_sum(arr)
        self.assertEqual(result, 10)

    def test_length_2(self):
        # Tests that the function correctly sums an array of length 2
        arr = [10, 20]
        result = array_sum(arr)
        self.assertEqual(result, 30)

    def test_empty_array(self):
        # Tests that the function returns 0 when given an empty array
        arr = []
        result = array_sum(arr)
        self.assertEqual(result, 0)

    def test_all_zeros(self):
        # Tests that the function correctly sums an array of all zeros
        arr = [0, 0, 0, 0, 0]
        result = array_sum(arr)
        self.assertEqual(result, 0)

    def test_large_positive_integers(self):
        # Tests that the function correctly sums an array of very large positive integers
        arr = [1000000, 2000000, 3000000, 4000000, 5000000]
        result = array_sum(arr)
        self.assertEqual(result, 15000000)

    def test_large_negative_integers(self):
        # Tests that the function correctly sums an array of very large negative integers
        arr = [-1000000, -2000000, -3000000, -4000000, -5000000]
        result = array_sum(arr)
        self.assertEqual(result, -15000000)

    def test_float_numbers(self):
        # Tests that the function correctly sums an array of floating point numbers
        arr = [1.5, 2.5, 3.5, 4.5, 5.5]
        result = array_sum(arr)
        self.assertEqual(result, 17.5)
