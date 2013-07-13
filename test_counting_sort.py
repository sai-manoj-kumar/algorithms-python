__author__ = 'saimanoj'

import unittest
from sorting import Sorting


class CountingSortTests(unittest.TestCase):
    def counting_sort_check(self, unsorted, expected, k):
        actual = Sorting.counting_sort(unsorted, k)
        # sorted is a built-in function, so using actual.
        self.assertEqual(actual, expected)

    def test_1_repetitions_counting_sort(self):
        unsorted = [4, 1, 3, 4, 3]
        expected = [1, 3, 3, 4, 4]
        self.counting_sort_check(unsorted, expected, 4)

    def test_2_unique_counting_sort(self):
        unsorted = [4, 1, 7, 2, 8, 6, 5, 3]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        self.counting_sort_check(unsorted, expected, 8)

    def test_3_already_sorted_counting_sort(self):
        unsorted = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        self.counting_sort_check(unsorted, expected, 8)

    def test_3_reverse_sorted_counting_sort(self):
        unsorted = [8, 7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        self.counting_sort_check(unsorted, expected, 8)

