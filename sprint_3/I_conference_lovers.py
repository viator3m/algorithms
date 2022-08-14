from typing import Tuple, List


def read_input() -> Tuple[int, List[int], int]:
    students = int(input())
    id_univers = [int(i) for i in input().split()]
    univers = int(input())
    return students, id_univers, univers


def counting_value(array: List[int]) -> List[List[int]]:
    counted_values = [[i, 0] for i in range(max(array) + 1)]
    for value in array:
        counted_values[value][1] += 1
    counted_values.sort(key=lambda x: x[1], reverse=True)
    return counted_values


def get_result(array: List[List[int]], k: int) -> None:
    for i in range(k):
        print(array[i][0], end=' ')


def main() -> None:
    students, id_univers, univers = read_input()
    counted_value = counting_value(id_univers)
    get_result(counted_value, univers)


if __name__ == '__main__':
    main()
