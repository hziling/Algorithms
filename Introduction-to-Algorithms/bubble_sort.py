import unittest


def bubble_sort(array):
    for i in range(0, len(array)-1):
        for j in range(len(array)-1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]


class TestSort(unittest.TestCase):

    def test_empty(self):
        array = []
        bubble_sort(array)
        self.assertEqual(array, sorted(array))

    def test_sort(self):
        array = [3, 5, 7, 2, 3, 9, 23, 56, 32, 21]
        bubble_sort(array)
        self.assertEqual(array, sorted(array))


if __name__ == '__main__':
    unittest.main()
