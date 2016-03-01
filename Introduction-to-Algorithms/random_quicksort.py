import unittest
import random

from quick_sort import partition


def random_quicksort(array, start, end):
    if start < end:
        mid = random_partition(array, start, end)
        random_quicksort(array, start, mid - 1)
        random_quicksort(array, mid + 1, end)



def random_partition(array, start, end):
    i = random.randint(start, end)
    array[i], array[end] = array[end],array[i]
    return partition(array, start, end)


class TestSort(unittest.TestCase):
    def test_empty(self):
        array = []
        random_quicksort(array, 0, 0)
        self.assertEqual(array, sorted(array))

    def test_sort(self):
        array = [random.randint(-10000, 10000) for i in range(random.randint(0, 100))]
        random_quicksort(array, 0, len(array) - 1)
        self.assertEqual(array, sorted(array))
