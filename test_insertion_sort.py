__author__ = 'saimanoj'

import unittest
import insertion_sort


class InsertionSortTests(unittest.TestCase):
    def test_1_repetitions_insertion_sort(self):
        unsorted = [4, 1, 3, 4, 3]
        expected = [1, 3, 3, 4, 4]
        sorted_list = insertion_sort.sort(unsorted)
        # sorted is a built-in function, so sorted_list.
        self.assertEqual(sorted_list, expected)

    def test_2_unique_insertion_sort(self):
        unsorted = [4, 1, 7, 2, 8, 6, 5, 3]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        sorted_list = insertion_sort.sort(unsorted)
        self.assertEqual(sorted_list, expected)

    def test_3_already_sorted_insertion_sort(self):
        unsorted = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        sorted_list = insertion_sort.sort(unsorted)
        self.assertEqual(sorted_list, expected)

    def test_3_reverse_sorted_insertion_sort(self):
        unsorted = [8, 7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        sorted_list = insertion_sort.sort(unsorted)
        self.assertEqual(sorted_list, expected)

