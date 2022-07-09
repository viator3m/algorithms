# id 69348269

from typing import List, Tuple
from collections import Counter


def read_input() -> Tuple[int, List[List[str]]]:
    k = int(input())
    keyboard = [list(map(str, input())) for line in range(4)]
    return k, keyboard


def trainer(k: int, keyboard: List[List[str]]):
    keys = Counter(int(key) for row in keyboard for key in row if key != '.')
    score = sum(1 for t in range(0, 10) if keys[t] and keys[t] <= k + k)
    return score


def main() -> None:
    k, keyboard = read_input()
    print(trainer(k, keyboard))


if __name__ == '__main__':
    main()
