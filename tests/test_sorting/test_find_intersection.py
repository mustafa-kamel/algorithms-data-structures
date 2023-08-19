import random
from unittest import TestCase

from sorting import find_smallest_item, selection_sort


class TestFindSmallestItem(TestCase):
    def test_positive_integers(self):
        # Tests that the function returns the index of the smallest item in a list of positive integers
        unsorted_list = [5, 3, 7, 1, 9]
        expected_index = 3
        self.assertEqual(find_smallest_item(unsorted_list), expected_index)

    def test_negative_integers(self):
        # Tests that the function returns the index of the smallest item in a list of negative integers
        unsorted_list = [-5, -3, -7, -1, -9]
        expected_index = 4
        self.assertEqual(find_smallest_item(unsorted_list), expected_index)

    def test_duplicate_integers(self):
        # Tests that the function returns the index of the first occurrence of the smallest item in a list of
        # duplicate integers
        unsorted_list = [5, 3, 7, 1, 1]
        expected_index = 3
        self.assertEqual(find_smallest_item(unsorted_list), expected_index)

    def test_empty_list(self):
        # Tests that the function raises an IndexError when given an empty list
        unsorted_list = []
        with self.assertRaises(IndexError):
            find_smallest_item(unsorted_list)

    def test_none_values(self):
        # Tests that the function raises a TypeError when given a list of None values
        unsorted_list = [None, None, None]
        with self.assertRaises(TypeError):
            find_smallest_item(unsorted_list)

    def test_large_integers(self):
        # Tests that the function returns the index of the smallest item in a list of large integers
        unsorted_list = [
            1000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
            20000000000000000000000000000000000000000000000000000000000000000000000000000000000,
            30000000000000000000000000000000000000000,
        ]
        expected_index = 2
        self.assertEqual(find_smallest_item(unsorted_list), expected_index)

    def test_random_integers(self):
        # Tests that the function returns the index of the smallest item in a list of random integers
        unsorted_list = [5, 3, 7, 1, 9, 2, 4, 6, 8]
        expected_index = 3
        self.assertEqual(find_smallest_item(unsorted_list), expected_index)

    def test_repeated_largest_integers(self):
        # Tests that the function returns the index of the first occurrence of the smallest item in a list of
        # repeated largest integers
        unsorted_list = [10, 10, 10, 10, 10]
        expected_index = 0
        self.assertEqual(find_smallest_item(unsorted_list), expected_index)

    def test_ascending_order_integers(self):
        # Tests that the function returns the index of the smallest item in a list of ascending order integers
        unsorted_list = [1, 2, 3, 4, 5]
        expected_index = 0
        self.assertEqual(find_smallest_item(unsorted_list), expected_index)

    def test_descending_order_integers(self):
        # Tests that the function returns the index of the smallest item in a list of descending order integers
        unsorted_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected_index = 8
        self.assertEqual(find_smallest_item(unsorted_list), expected_index)

    def test_very_small_integers(self):
        # Tests that the function returns the index of the smallest item in a list of very small integers
        unsorted_list = [1, 0, -1, -2, -3]
        expected_index = 4
        self.assertEqual(find_smallest_item(unsorted_list), expected_index)


class TestSelectionSort(TestCase):
    def test_ascending_order(self):
        # Tests that the function sorts a list of integers in ascending order
        unsorted_list = [5, 8, 3, 2, 9, 1, 4, 7, 55]
        sorted_list = selection_sort(unsorted_list.copy())
        self.assertEqual(sorted_list, sorted(unsorted_list))

    def test_random_order(self):
        # Tests that the function sorts a list of integers in random order
        unsorted_list = [random.randint(i, i * 999) for i in range(1, 999)]
        sorted_list = selection_sort(unsorted_list.copy())
        self.assertEqual(sorted_list, sorted(unsorted_list))

    def test_empty_list(self):
        # Tests that the function returns an empty list when given an empty list
        unsorted_list = []
        sorted_list = selection_sort(unsorted_list.copy())
        self.assertEqual(sorted_list, [])

    def test_single_item_list(self):
        # Tests that the function returns the same list when given a list with a single item
        unsorted_list = [1]
        sorted_list = selection_sort(unsorted_list.copy())
        self.assertEqual(sorted_list, unsorted_list)

    def test_negative_integers(self):
        # Tests that the function sorts a list of negative integers
        unsorted_list = [-5, -8, -3, -2, -9, -1, -4, -7, -55]
        sorted_list = selection_sort(unsorted_list.copy())
        self.assertEqual(sorted_list, sorted(unsorted_list))

    def test_positive_and_negative_integers(self):
        # Tests that the function sorts a list of both positive and negative integers
        unsorted_list = [5, -8, 3, -2, 9, 1, -4, 7, 55]
        sorted_list = selection_sort(unsorted_list.copy())
        self.assertEqual(sorted_list, sorted(unsorted_list))

    def test_identical_integers(self):
        # Tests that the function returns the same list when given a list of identical integers
        unsorted_list = [5, 5, 5, 5, 5]
        sorted_list = selection_sort(unsorted_list.copy())
        self.assertEqual(sorted_list, unsorted_list)

    def test_large_integers(self):
        # Tests that the function sorts a list of large integers
        unsorted_list = [random.randint(i, i * 999) for i in range(1, 9999)]
        sorted_list = selection_sort(unsorted_list.copy())
        self.assertEqual(sorted_list, sorted(unsorted_list))

    def test_string_sorting(self):
        # Tests that the selection_sort function can sort a list of strings in ascending order
        unsorted_list = ["apple", "banana", "cherry", "date", "elderberry"]
        sorted_list = selection_sort(unsorted_list.copy())
        self.assertEqual(sorted_list, sorted(unsorted_list))

    def test_floating_point_numbers(self):
        # Tests that selection_sort sorts a list of floating point numbers in ascending order
        unsorted_list = [3.14, 2.71, 1.41, 1.62, 0.99]
        sorted_list = selection_sort(unsorted_list.copy())
        self.assertEqual(sorted_list, sorted(unsorted_list))
