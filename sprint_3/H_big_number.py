from typing import List


def compare(obj_1: str, obj_2: str) -> bool:
    if int(obj_1 + obj_2) < int(obj_2 + obj_1):
        return True
    return False


def get_big_number(array: List[str]) -> str:
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and compare(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
    return ''.join(array[::-1])


def main() -> None:
    _ = int(input())
    array = [i for i in input().strip().split()]
    print(get_big_number(array))


if __name__ == '__main__':
    main()