__author__ = 'saimanoj'

import sieve

def main():
    print 'Hello, Algorithms World!'


def sundaram_sieve_demo():
    primes = list(sieve.sundaram(10000))
    print len(primes)
    # print primes


if __name__ == "__main__":
    main()

