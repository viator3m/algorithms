from typing import List


def read_input() -> List[int]:
    _ = int(input())
    street = list(map(int, input().strip().split()))
    return street


def get_nearest_zero(street: List[int]) -> str:
    result = []
    zero_index_list = {i for i in range(len(street)) if street[i] == 0}
    for index in range(len(street)):
        if street[index]:
            min_distance = len(street)
            for zero_index in zero_index_list:
                distance = max(index, zero_index) - min(index, zero_index)
                if distance < min_distance:
                    min_distance = distance
            result.append(min_distance)
        else:
            result.append(0)
    return ' '.join(map(str, result))


def main() -> None:
    street = read_input()
    print(get_nearest_zero(street))


if __name__ == '__main__':
    main()
