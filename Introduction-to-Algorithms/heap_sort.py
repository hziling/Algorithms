import unittest


def max_heapify(array, heap_size, i):
    if i == 0:
        left, right = 1, 2
    else:
        left, right = i << 1, (i << 1) + 1

    largest = i
    if left <= heap_size - 1 and array[left] > array[i]:
        largest = left
    if right <= heap_size - 1 and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, heap_size, largest)


def build_heap(array):
    heap_size = len(array)
    for i in range(heap_size / 2, -1, -1):
        max_heapify(array, heap_size, i)

    return heap_size


def heap_sort(array):
    heap_size = build_heap(array)
    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heap_size -= 1
        max_heapify(array, heap_size, 0)


class TestSort(unittest.TestCase):
    def test_empty(self):
        array = []
        heap_sort(array)
        self.assertEqual(array, sorted(array))

    def test_sort(self):
        array = [3, 5, 7, 2, 3, 9, 23, 56, 32, 21]
        heap_sort(array)
        self.assertEqual(array, sorted(array))


if __name__ == '__main__':
    unittest.main()
