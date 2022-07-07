from typing import List


def read_input() -> str:
    _ = int(input())
    line = input()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


def get_longest_word(text: str) -> str:
    text = text.strip().split()
    longest = 0
    for i in range(1, len(text)):
        if len(text[i]) > len(text[longest]):
            longest = i
    return text[longest]


def main() -> None:
    text = read_input()
    result = get_longest_word(text)
    print_result(result)


if __name__ == '__main__':
    main()
