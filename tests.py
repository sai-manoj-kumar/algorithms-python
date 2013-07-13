__author__ = 'saimanoj'

import test_sieve
import test_counting_sort
import test_insertion_sort


class Tests(test_sieve.SieveTests, test_counting_sort.CountingSortTests,
            test_insertion_sort.InsertionSortTests):
    # Add more Test classes as base classes to this class for including them
    # in all Tests.
    pass

