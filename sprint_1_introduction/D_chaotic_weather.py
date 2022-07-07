from typing import List, Tuple


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return n, temperatures


def get_weather_randomness(n: int, temperatures: List[int]) -> int:
    randomness = 0
    for i in range(1, n- 1):
        if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
            randomness += 1
    try:
        if temperatures[0] > temperatures[1]:
            randomness += 1
        if temperatures[-1] > temperatures[-2]:
            randomness += 1
    except IndexError:
        randomness += 1
    return randomness


def main():
    n, temperatures = read_input()
    result = get_weather_randomness(n, temperatures)
    print(result)


if __name__ == '__main__':
    main()
