import unittest


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key


class TestSort(unittest.TestCase):

    def test_empty(self):
        array = []
        insertion_sort(array)
        self.assertEqual(array, sorted(array))

    def test_sort(self):
        array = [3, 5, 7, 2, 3, 9, 23, 56, 32, 21]
        insertion_sort(array)
        self.assertEqual(array, sorted(array))


if __name__ == '__main__':
    unittest.main()