__author__ = 'saimanoj'


def sort(unsorted):
    n = len(unsorted)

    for j in range(1, n):
        key = unsorted[j]
        i = j - 1
        while i >= 0 and unsorted[i] > key:
            unsorted[i + 1] = unsorted[i]
            i -= 1
        unsorted[i + 1] = key
    result = unsorted

    return result

