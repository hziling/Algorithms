import unittest
import random


def counting_sort(A, B, k):
    # init C
    C = [0 for i in range(k + 1)]

    for i in range(len(A)):
        C[A[i]] += 1
    # C[i] now contains the number of elements equal to i.

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    # C[i] now contains the number of elements less or equal to i.

    for i in range(len(A)):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1


class TestSort(unittest.TestCase):
    def test_empty(self):
        array = []
        result = [0 for i in range(len(array))]
        counting_sort(array, result, 10)
        self.assertEqual(array, sorted(array))

    def test_sort(self):
        array = [random.randint(0, 10) for i in range(10)]
        result = [0 for i in range(len(array))]
        counting_sort(array, result, 10)
        self.assertEqual(result, sorted(array))