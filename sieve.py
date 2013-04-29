__author__ = 'saimanoj'


def eratosthenes(n):
    primes_bool = [True] * ((n - 1) / 2)  # True for Odd numbers from 3 to n.
    if n >= 2:
        yield 2

    for (index, is_prime) in enumerate(primes_bool):
        if is_prime:
            p = 2 * index + 3
            yield p

            x = p * p
            while x <= n:
                primes_bool[(x - 3) / 2] = False
                x += 2 * p

