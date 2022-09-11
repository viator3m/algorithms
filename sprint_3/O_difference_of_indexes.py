from typing import List


def count_less(array: List[int], desired_diff: int) -> int:
    count = left = 0
    for right, x in enumerate(array):
        while x - array[left] > desired_diff:
            left += 1
        count += right - left
    return count


def smallest_distance(array: List[int], k: int) -> int:
    array.sort()
    low = 0
    high = array[-1] - array[0]
    while low < high:
        mid = (low + high) // 2
        count = count_less(array, mid)
        if count >= k:
            high = mid
        else:
            low = mid + 1

    return low


def main() -> None:
    _ = int(input())
    array = [int(i) for i in input().split()]
    k = int(input())
    print(smallest_distance(array, k))


if __name__ == '__main__':
    main()
