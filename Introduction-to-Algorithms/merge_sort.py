import unittest


def merge(array, start, mid, end):
    m = mid - start + 1
    n = end - mid

    # let L[start, mid], R[mid + 1, end] to be new arrays
    L, R = [], []
    for i in range(m):
        L.append(array[start + i])
    for j in range(n):
        R.append(array[mid + 1 + j])

    i, j = 0, 0
    for k in range(start, end + 1):
        if j >=n or i < m and L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1


def merge_sort(array, start, end):
    if start < end:
        mid = (start + end) / 2
        merge_sort(array, start, mid)
        merge_sort(array, mid + 1, end)
        # print array[start:mid+1], array[mid+1:end+1]
        merge(array, start, mid, end)


class TestSort(unittest.TestCase):

    def test_empty(self):
        array = []
        merge_sort(array, 0, 0)
        self.assertEqual(array, sorted(array))

    def test_sort(self):
        array = [3, 5, 7, 2, 3, 9, 23, 56, 32, 21]
        merge_sort(array, 0, len(array)-1)
        self.assertEqual(array, sorted(array))


if __name__ == '__main__':
    unittest.main()