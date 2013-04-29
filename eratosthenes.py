__author__ = 'saimanoj'


def sieve(n):
    primes_bool = [False, False] + [True] * (n - 1)
    for (p, is_prime) in enumerate(primes_bool):
        if is_prime:
            yield p
            x = p * p
            while x <= n:
                primes_bool[x] = False
                x += p

