__author__ = 'saimanoj'

import sieve


def main():
    primes = list(sieve.sundaram(10000))
    print len(primes)
    # print primes


if __name__ == "__main__":
    main()

