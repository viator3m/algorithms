from typing import List


def counting_sort(array: List[int], k: int = 3) -> None:
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1

    for color in range(k):
        print((str(color) + ' ') * counted_values[color], end='')


def main() -> None:
    _ = int(input())
    nums = [int(i) for i in input().strip().split()]
    counting_sort(nums)


if __name__ == '__main__':
    main()