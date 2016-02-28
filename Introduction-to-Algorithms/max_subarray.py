def find_max_crossing_subarray(array, low, mid, high):
    left = mid
    left_sum = 0
    max_left_sum = 0
    for i in range(mid, low - 1, -1):
        left_sum += array[i]
        if max_left_sum < left_sum:
            max_left_sum = left_sum
            left = i

    right = mid + 1
    right_sum = 0
    max_right_sum = 0
    for j in range(mid + 1, high + 1):
        right_sum += array[j]
        if max_right_sum < right_sum:
            max_right_sum = right_sum
            right = j

    return left, right, (max_left_sum + max_right_sum)


def find_max_subarray(array, low, high):
    mid = (low + high) / 2
    if low == high:
        return low, high, array[low]
    else:
        left_low, left_high, left_sum = find_max_subarray(array, low, mid)
        right_low, right_high, right_sum = find_max_subarray(array, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(array, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


if __name__ == '__main__':
    array = [1, -2, 3, 10, -4, 7, 2, -5]
    # array =[]
    assert array != []
    low, high, sum = find_max_subarray(array, 0, len(array) - 1)
    print 'max_subarray = {0}, sum = {1}'.format(array[low:high + 1], sum)  # max_subarray = [3, 10, -4, 7, 2], sum = 18
