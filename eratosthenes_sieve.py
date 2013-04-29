__author__ = 'saimanoj'


def sieve(n):
    numbers = range(n + 1)
    is_prime = [False, False] + [True] * (n - 1)
    assert len(numbers) == len(is_prime)
    p = 2
    while True:
        for x in range(p * p, n + 1, p):
            is_prime[x] = False

        if True in is_prime[p + 1:]:
            p = is_prime.index(True, p + 1)
        else:
            break

    primes = [x for x in numbers if is_prime[x]]
    print is_prime.count(True)
    return primes
