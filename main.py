__author__ = 'saimanoj'

import sieve


def main():
    primes = list(sieve.eratosthenes(100))  # 2m 58s
    print len(primes)


if __name__ == "__main__":
    main()

