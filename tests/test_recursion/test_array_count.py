from unittest import TestCase

from recursion import array_count


class TestArrayCount(TestCase):
    def test_empty_array(self):
        # Tests that the function returns 0 when given an empty array
        arr = []
        result = array_count(arr)
        self.assertEqual(result, 0)

    def test_array_length_1(self):
        # Tests that the function returns 0 when given an array of length 1
        arr = [1]
        result = array_count(arr)
        self.assertEqual(result, 1)

    def test_array_length_greater_than_1(self):
        # Tests that the function returns 0 when given an array of length greater than 1
        arr = [1, 2, 3]
        result = array_count(arr)
        self.assertEqual(result, 3)

    def test_none_input_fixed(self):
        # Tests that the function returns 0 when given None as input
        arr = None
        result = array_count(arr)
        self.assertEqual(result, 0)

    def test_nested_list_input(self):
        # Tests that the function returns 2 when given a nested list input
        arr = [[1, 2], [3, 4]]
        result = array_count(arr)
        self.assertEqual(result, 2)

    def test_list_only_none_values_fixed(self):
        # Tests that the function returns 3 when given a list containing only None values
        arr = [None, None, None]
        result = array_count(arr)
        self.assertEqual(result, 3)

    def test_list_only_empty_lists(self):
        # Tests that the function returns 3 when given a list containing only empty lists
        arr = [[], [], []]
        result = array_count(arr)
        self.assertEqual(result, 3)

    def test_list_only_non_integer_values(self):
        # Tests that the function returns 3 when given a list containing only non-integer values
        arr = ["a", "b", "c"]
        result = array_count(arr)
        self.assertEqual(result, 3)

    def test_list_with_integers_and_non_integers(self):
        # Tests that the function returns the correct count when given a list containing both integers and non-integers
        arr = [1, "a", 2, "b", "c"]
        result = array_count(arr)
        self.assertEqual(result, 5)
