# id 69605614
from typing import List


def broken_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if target == nums[middle]:
            return middle

        if nums[left] <= nums[middle]:
            if nums[left] <= target <= nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

        else:
            if nums[middle] <= target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
    return -1


def main():
    _ = int(input())
    target = int(input())
    arr = [int(i) for i in input().strip().split()]
    print(broken_search(arr, target))


if __name__ == '__main__':
    main()

