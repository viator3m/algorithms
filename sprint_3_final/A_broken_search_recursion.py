from typing import List


def broken_search(nums: List[int], target: int, left: int = 0,
                  right: int = None) -> int:
    if right is None:
        right = len(nums) - 1
    if left > right:
        return -1
    middle = (left + right) // 2
    for index in [middle, left, right]:
        if target == nums[index]:
            return index  # TODO: trick for test №1

    if nums[left] < nums[middle]:
        if nums[left] <= target <= nums[middle]:
            return broken_search(nums, target, left, middle - 1)
        return broken_search(nums, target, middle + 1, right)
    if nums[middle] <= target <= nums[right]:
        return broken_search(nums, target, middle + 1, right)
    return broken_search(nums, target, left, middle - 1)


def main():
    length = int(input())
    target = int(input())
    arr = [int(i) for i in input().strip().split()]
    print(broken_search(arr, target))


def test():
    array = [5, 1]
    result = broken_search(array, 1)
    assert result == 1  # TODO: test failed

    array = [3, 5, 6, 7, 9, 1, 2]
    result = broken_search(array, 4)
    assert result == -1

    array = [1]
    result = broken_search(array, 4)
    assert result == -1

    array = [1, 2, 3, 5, 6, 7, 9, 0]
    result = broken_search(array, 3)
    assert result == 2

    array = [1, 2, 3, 5, 6, 7, 9, 0]
    result = broken_search(array, 3)
    assert result == 2


if __name__ == '__main__':
    main()
