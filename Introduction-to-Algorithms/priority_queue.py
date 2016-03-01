from heap_sort import max_heapify, build_heap


def heap_maximum(array):
    return array[0]


def heap_extract_max(array, heap_size):
    if heap_size < 1:
        raise ValueError

    max_value = array[0]
    array[0] = array[heap_size - 1]
    del array[heap_size - 1]
    heap_size -= 1
    max_heapify(array, heap_size, 0)

    return max_value


def heap_parent(i):
    return i / 2 if i != 2 else 0


def heap_increase_key(array, heap_size, i, key):
    if key < array[i]:
        raise ValueError

    array[i] = key
    while i > 0 and array[i] > array[heap_parent(i)]:
        array[i], array[heap_parent(i)] = array[heap_parent(i)], array[i]
        i = heap_parent(i)


def max_heap_insert(array, heap_size, key):
    heap_size += 1
    array.append(float('-inf'))
    heap_increase_key(array, heap_size, heap_size - 1, key)


if __name__ == '__main__':
    array = [i for i in range(10)]
    build_heap(array)

    assert heap_maximum(array) == 9

    value = heap_extract_max(array, len(array))
    assert value == 9
    assert len(array) == 9

    heap_increase_key(array, len(array), 5, 20)
    assert array[0] == 20

    max_heap_insert(array, len(array), 50)
    assert array[0] == 50
    assert len(array) == 10