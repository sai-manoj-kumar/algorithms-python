__author__ = 'saimanoj'


def sieve(n):
    numbers = range(2, n + 1)
    # print numbers
    p = 2
    while True:
        i = 2
        num_to_be_removed = p * i
        while num_to_be_removed <= numbers[-1]:
            if num_to_be_removed in numbers:
                numbers.remove(num_to_be_removed)
            i += 1
            num_to_be_removed = p * i
        if p < numbers[-1]:
            p = numbers[numbers.index(p) + 1]
        else:
            break

    print numbers
    return numbers

