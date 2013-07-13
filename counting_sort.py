__author__ = 'saimanoj'


def sort(unsorted, k):
    counter = [0] * (k + 1)
    n = len(unsorted)
    result = [0] * n

    for x in unsorted:
        counter[x] += 1
    for i in range(1, k + 1):
        counter[i] += counter[i - 1]
    for x in reversed(unsorted):
        result[counter[x] - 1] = x
        counter[x] -= 1

    return result

