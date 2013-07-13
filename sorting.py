__author__ = 'saimanoj'


class Sorting:
    @staticmethod
    def counting_sort(unsorted, k):
        """
        Sorts the given list of "integers" ranging from "1 to k" using counting
        sort algorithm.
        :param unsorted: unsorted list of integers.
        :param k: Maximum value of integers in the given list starting from 1.
        :return: Returns sorted list.
        """
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


    @staticmethod
    def insertion_sort(unsorted):
        """
        Sorts given list of numbers using insertion sort algorithm.
        :param unsorted: unsorted list of numbers
        :return: sorted list of numbers
        """
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

