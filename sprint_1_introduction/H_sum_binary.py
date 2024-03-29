from itertools import zip_longest
from typing import Tuple


def sum_binary(x: str, y: str) -> str:
    summ = ''
    carry_one = 0

    for arr in zip_longest(x[::-1], y[::-1], fillvalue='0'):
        temp_sum = int(arr[0]) + int(arr[1]) + carry_one
        summ += str(temp_sum % 2)
        carry_one = temp_sum // 2
    if carry_one:
        summ += '1'
    return summ[::-1]


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(sum_binary(first_number, second_number))
