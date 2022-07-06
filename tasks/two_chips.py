from typing import Optional, List, Tuple


def two_chips(array: List[int], target: int) -> Optional[Tuple[int, int]]:
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                return array[i], array[j]
    return None


def read_input() -> Tuple[List[int], int]:
    length = int(input())
    array = list(map(int, input().strip().split()))
    target = int(input())
    return array, target


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(' '.join(map(str, result)))


array, target = read_input()
print_result(two_chips(array, target))
