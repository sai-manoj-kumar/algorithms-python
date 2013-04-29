__author__ = 'saimanoj'

import eratosthenes


def main():
    primes = list(eratosthenes.sieve(500000000))  # 2m 58s
    print len(primes)


if __name__ == "__main__":
    main()

