from typing import List

n = 4
flowers = [[7, 8], [2, 3], [7, 8], [6, 10]]


def merge_flower_beds(beds):
    start, end = beds[0]
    next_beds = 1
    result = []
    while next_beds < len(beds):
        next_start, next_end = beds[next_beds]
        if (start <= next_start <= end or
                start <= next_end <= end):
            start, end = min(start, next_start), max(end, next_end)
        else:
            result.append([start, end])
            start, end = beds[next_beds]
        next_beds += 1
    result.append([start, end])

    return result


def merge_sort(flowers):
    if len(flowers) == 1:
        return flowers

    left: List[int] = merge_sort(flowers[0: len(flowers) // 2])
    right: List[int] = merge_sort(flowers[len(flowers) // 2: len(flowers)])

    result: List = [] * len(flowers)

    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1

    return result


def main():
    lines = int(input())
    flower_beds = [[int(i) for i in input().split()] for line in range(lines)]
    result = merge_flower_beds(merge_sort(flower_beds))
    [print(*i) for i in result]


if __name__ == '__main__':
    main()
