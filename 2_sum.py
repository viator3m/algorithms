from typing import List, Tuple, Optional
from howlong import how_long


@how_long
def twosum_naive(array: List[int], x: int) -> Optional[Tuple[int, int]]:
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == x:
                return array[i], array[j]
    return None


@how_long
def twowum_optimized(array: List[int], x: int) -> Optional[Tuple[int, int]]:
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] == x:
            return array[left], array[right]
        if array[left] + array[right] > x:
            right -= 1
        else:
            left += 1
    return None


@how_long
def twosum_with_set(array: List[int], x: int) -> Optional[Tuple[int, int]]:
    previous = set()
    for A in array:
        Y = x - A
        if Y in previous:
            return Y, A
        previous.add(A)
    return None

array = [-9, -7, -6, -1, -1, 3]
x = 2
print(twosum_naive(array, x))
print(twowum_optimized(array, x))
print(twosum_with_set(array, x))

