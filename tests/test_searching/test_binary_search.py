from unittest import TestCase

from searching import binary_search


class TestBinarySearch(TestCase):
    # Tests that binary_search returns the correct index when the needle is in the middle of the haystack.
    def test_middle_needle(self):
        lookup = 5000
        search_list = list(range(1, 10000))
        index = binary_search(lookup, search_list)
        self.assertEqual(index, 4999)

    # Tests that binary_search returns the correct index when the needle is at the beginning of the haystack.
    def test_beginning_needle(self):
        lookup = 1
        search_list = list(range(1, 10000))
        index = binary_search(lookup, search_list)
        self.assertEqual(index, 0)

    # Tests that binary_search returns the correct index when the needle is at the end of the haystack.
    def test_end_needle(self):
        lookup = 9999
        search_list = list(range(1, 10000))
        index = binary_search(lookup, search_list)
        self.assertEqual(index, 9998)

    # Tests that binary_search returns None when the haystack is empty.
    def test_empty_haystack(self):
        lookup = 1
        search_list = []
        index = binary_search(lookup, search_list)
        self.assertIsNone(index)

    # Tests that binary_search returns the correct index when the haystack has only one element.
    def test_one_element_haystack(self):
        lookup = 1
        search_list = [1]
        index = binary_search(lookup, search_list)
        self.assertEqual(index, 0)

    # Tests that binary_search returns None when the needle is not in the haystack.
    def test_needle_not_in_haystack(self):
        lookup = 10000
        search_list = list(range(1, 9999))
        index = binary_search(lookup, search_list)
        self.assertIsNone(index)

    # Tests that binary_search works correctly with a large haystack.
    def test_large_haystack(self):
        haystack = list(range(1, 1000000))
        needle = 500000
        index = binary_search(needle, haystack)
        self.assertEqual(index, 499999)

    # Tests that binary_search works correctly with a negative needle.
    def test_negative_needle(self):
        haystack = list(range(1, 10000))
        needle = -1
        index = binary_search(needle, haystack)
        self.assertIsNone(index)

    # Tests that binary_search returns the correct index when the haystack has duplicate elements.
    def test_duplicate_elements(self):
        haystack = [1, 2, 2, 3, 4, 5]
        needle = 2
        index = binary_search(needle, haystack)
        self.assertIn(index, [1, 2])

    # Tests that binary_search returns the correct index when searching for an element in a tuple haystack.
    def test_tuple_needle(self):
        lookup = 2
        search_tuple = tuple(range(1, 9999))
        index = binary_search(lookup, search_tuple)
        self.assertEqual(index, 1)
