__author__ = 'saimanoj'

import unittest
import sieve


class SieveTests(unittest.TestCase):
    def test_emptylist_n_1(self):
        self.assertEqual([], list(sieve.eratosthenes(1)))

    def test_1_is_not_prime(self):
        self.assertNotIn(1, list(sieve.eratosthenes(-10)))

    def test_2_is_prime(self):
        self.assertEqual(list(sieve.eratosthenes(2)), [2])

    def test_primes_in_100(self):
        self.assertEqual(list(sieve.eratosthenes(100)),
                         [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                          47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])


