import sys
import time
from typing import List

from is_prime import is_prime


def read_input() -> int:
    return int(sys.stdin.readline().strip())


def print_result(result: List[int]) -> None:
    result = ' '.join(map(str, result))
    sys.stdout.write(result+'\n')


def prime_numbers(n: int) -> List[int]:
    list_of_numbers = []
    for i in range(2, n + 1):
        if is_prime(i):
            list_of_numbers.append(i)
    return list_of_numbers


def main():
    n = read_input()
    result = prime_numbers(n)
    print_result(result)


if __name__ == '__main__':
    start = time.time()
    main()
    sys.stdout.write(f'TIME TAKEN: {time.time() - start}')
