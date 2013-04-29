__author__ = 'saimanoj'

import eratosthenes_sieve


def main():
    primes = list(eratosthenes_sieve.sieve(100000000))
    print len(primes)


if __name__ == "__main__":
    main()

