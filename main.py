__author__ = 'saimanoj'

import eratosthenes_sieve


def main():
    primes = eratosthenes_sieve.sieve(100)
    print len(primes)


if __name__ == "__main__":
    main()

