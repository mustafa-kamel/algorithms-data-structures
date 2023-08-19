from unittest import TestCase

from recursion import binary_search


class TestBinarySearch(TestCase):
    # Tests that the function can correctly find an element that exists in the middle of the list
    def test_middle_element_exists(self):
        haystack = [1, 2, 3, 4, 5]
        needle = 3
        result = binary_search(needle, haystack)
        self.assertEqual(result, 2)

    # Tests that the function can correctly find an element that exists at the beginning of the list
    def test_first_element_exists(self):
        haystack = [1, 2, 3, 4, 5]
        needle = 1
        result = binary_search(needle, haystack)
        self.assertEqual(result, 0)

    # Tests that the function can correctly find an element that exists at the end of the list
    def test_last_element_exists(self):
        haystack = [1, 2, 3, 4, 5]
        needle = 5
        result = binary_search(needle, haystack)
        self.assertEqual(result, 1)

    # Tests that the function can correctly find an element that exists in a list of odd length
    def test_element_exists_odd_length(self):
        haystack = [1, 2, 3, 4, 5, 6, 7]
        needle = 4
        result = binary_search(needle, haystack)
        self.assertEqual(result, 3)

    # Tests that the function can correctly find an element that exists in a list of even length
    def test_element_exists_even_length(self):
        haystack = [1, 2, 3, 4, 5, 6]
        needle = 3
        result = binary_search(needle, haystack)
        self.assertEqual(result, 0)

    # Tests that the function returns None when searching for an element that does not exist in the list
    def test_element_does_not_exist(self):
        haystack = [1, 2, 3, 4, 5]
        needle = 6
        result = binary_search(needle, haystack)
        self.assertIsNone(result)

    # Tests that the function returns None when searching in an empty list
    def test_empty_list(self):
        haystack = []
        needle = 1
        result = binary_search(needle, haystack)
        self.assertIsNone(result)

    # Tests that the function can correctly find an element in a tuple
    def test_element_in_tuple(self):
        haystack = (1, 2, 3, 4, 5)
        needle = 3
        result = binary_search(needle, haystack)
        self.assertEqual(result, 2)

    # Tests that the function can correctly find an element in a set
    def test_element_in_set(self):
        haystack = [1, 2, 3, 4, 5]
        needle = 4
        result = binary_search(needle, haystack)
        self.assertEqual(result, 0)

    # Tests that the function can correctly find an element in a list with duplicate values
    def test_element_in_list_with_duplicates(self):
        haystack = [1, 2, 2, 3, 4, 5]
        needle = 2
        result = binary_search(needle, haystack)
        self.assertEqual(result, 1)

    # Tests that the function can correctly find an element in a list with negative values
    def test_element_in_list_with_negative_values(self):
        haystack = [-5, -4, -3, -2, -1]
        needle = -3
        result = binary_search(needle, haystack)
        self.assertEqual(result, 2)

    # Tests that the function can correctly find an element in a list with floating point values
    def test_element_in_list_with_float_values(self):
        haystack = [1.1, 2.2, 3.3, 4.4, 5.5]
        needle = 4.4
        result = binary_search(needle, haystack)
        self.assertEqual(result, 0)
