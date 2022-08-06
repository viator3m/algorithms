from typing import List


def merge(array: list, left: int, mid: int, right: int) -> List[int]:
    array_1 = array[left: mid]
    array_2 = array[mid: right]
    i = j = 0
    k = left

    while i < len(array_1) and j < len(array_2):
        if array_1[i] <= array_2[j]:
            array[k] = array_1[i]
            i += 1
        else:
            array[k] = array_2[j]
            j += 1
        k += 1

    while i < len(array_1):
        array[k] = array_1[i]
        i += 1
        k += 1
    while j < len(array_2):
        array[k] = array_2[j]
        j += 1
        k += 1
    return array


def merge_sort(arr, left, right):
    if right - left <= 1:
        return
    else:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
