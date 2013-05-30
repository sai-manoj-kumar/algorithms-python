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


def make_odd(x):
    return 2 * x + 1


def sundaram(n):
    n = (n - 1) / 2
    primes = range(n + 1)
    for i in xrange(1, n + 1):
        for j in xrange(1, n + 1):
            if 1 <= i <= j and i + j + 2 * i * j <= n:
                primes[i + j + 2 * i * j] = None
    primes = filter(None, primes)
    primes = map(make_odd, primes)
    return [2] + primes

