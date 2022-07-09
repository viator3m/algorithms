# id 69345566

from typing import List, Tuple


def read_input() -> Tuple[int, List[List[str]]]:
    k = int(input())
    keyboard = [list(map(str, input())) for line in range(4)]
    return k, keyboard


def trainer(k: int, keyboard: List[List[str]]) -> int:
    score = 0
    keys = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
            '6': 0, '7': 0, '8': 0, '9': 0, '0': 0, }
    for line in keyboard:
        for key in line:
            if key.isdigit():
                keys[key] += 1
    for t in range(0, 10):
        if keys[str(t)] and keys[str(t)] <= k + k:
            score += 1
    return score


def main() -> None:
    k, keyboard = read_input()
    print(trainer(k, keyboard))


if __name__ == '__main__':
    main()
