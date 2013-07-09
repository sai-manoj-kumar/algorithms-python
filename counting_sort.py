__author__ = 'saimanoj'


def sort(unsorted, k):
    counter = [0] * (k + 1)
    n = len(unsorted)
    result = [0] * n

    for j in range(n):
        counter[unsorted[j]] += 1
    for i in range(1, k + 1):
        counter[i] += counter[i - 1]
    for j in range(n - 1, -1, -1):
        result[counter[unsorted[j]] - 1] = unsorted[j]
        counter[unsorted[j]] -= 1

    return result

