__author__ = 'saimanoj'

import test_counting_sort
import test_insertion_sort
import test_sieve


class AllSortingTests(test_sieve.SieveTests,
                      test_counting_sort.CountingSortTests,
                      test_insertion_sort.InsertionSortTests):
    pass
