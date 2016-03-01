import unittest
import random


def quick_sort(array, start, end):
    if start < end:
        mid = partition(array, start, end)
        quick_sort(array, start, mid - 1)
        quick_sort(array, mid + 1, end)


def partition(array, start, end):
    key = array[end]
    i = start - 1

    for j in range(start, end):
        if key > array[j]:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]

    return i + 1


class TestSort(unittest.TestCase):
    def test_empty(self):
        array = []
        quick_sort(array, 0, 0)
        self.assertEqual(array, sorted(array))

    def test_sort(self):
        array = [random.randint(-10000, 10000) for i in range(random.randint(0, 100))]
        quick_sort(array, 0, len(array) - 1)
        self.assertEqual(array, sorted(array))
