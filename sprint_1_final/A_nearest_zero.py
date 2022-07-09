# id 69348708

from typing import Tuple, List


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    street = list(map(int, input().strip().split()))
    return street, n


def get_nearest_zero(street: List[int], n: int) -> str:
    result = [-1] * len(street)
    zero_list = [i for i in range(n) if street[i] == 0]

    for house in range(0, zero_list[0] + 1):
        result[house] = zero_list[0] - house

    for pos in range(len(zero_list) - 1):
        zero_1, zero_2 = zero_list[pos], zero_list[pos + 1]
        for house in range(zero_1, zero_2):
            result[house] = min(house - zero_1, zero_2 - house)

    for house in range(zero_list[-1], len(street)):
        result[house] = house - zero_list[-1]

    return ' '.join(map(str, result))


def main() -> None:
    street, n = read_input()
    print(get_nearest_zero(street, n))


if __name__ == '__main__':
    main()
