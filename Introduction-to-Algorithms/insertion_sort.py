import unittest
import random


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


class TestSort(unittest.TestCase):
    def test_empty(self):
        array = []
        insertion_sort(array)
        self.assertEqual(array, sorted(array))

    def test_sort(self):
        array = [random.randint(-10000, 10000) for i in range(random.randint(0, 100))]
        insertion_sort(array)
        self.assertEqual(array, sorted(array))


if __name__ == '__main__':
    unittest.main()
