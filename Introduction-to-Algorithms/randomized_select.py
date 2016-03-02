import unittest
import random
from heapq import nsmallest

from random_quicksort import random_partition


def randomized_select(array, start, end, i):
    if start == end:
        return array[start]

    q = random_partition(array, start, end)
    k = q - start + 1
    if i == k:
        return array[q]
    elif i < k:
        return randomized_select(array, start, q - 1, i)
    else:
        return randomized_select(array, q + 1, end, i - k)


class TestSelect(unittest.TestCase):
    def test_select(self):
        array = range(10)
        random.shuffle(array)
        result = randomized_select(array, 0, len(array) - 1, 5)
        self.assertEqual(result, nsmallest(5, array)[-1])


if __name__ == '__main__':
    unittest.main()

