from typing import List, Tuple


def read_input() -> Tuple[List[int], int]:
    _ = int(input())
    x = list(map(int, input().split()))
    k = int(input())
    return x, k


def get_list_form(x: List[int], k:int) -> str:
    x_number = int(''.join(map(str, x)))
    k += x_number
    k_list = list(map(int, str(k)))
    return ' '.join(map(str, k_list))


x, k = read_input()
print(get_list_form(x, k))
