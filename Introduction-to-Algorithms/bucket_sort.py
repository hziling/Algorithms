import unittest
import random

from insertion_sort import insertion_sort


def bucket_sort(array):
    bucket = [list() for i in range(10)]

    for i in range(len(array)):
        bucket[int(array[i] * 10)].append(array[i])

    for i in range(len(bucket)):
        insertion_sort(bucket[i])

    m = 0
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            array[m] = bucket[i][j]
            m += 1


class TestSort(unittest.TestCase):
    def test_empty(self):
        array = []
        bucket_sort(array)
        self.assertEqual(array, sorted(array))

    def test_sort(self):
        array = [random.random() for i in range(10)]
        bucket_sort(array)
        self.assertEqual(array, sorted(array))


if __name__ == '__main__':
    unittest.main()
