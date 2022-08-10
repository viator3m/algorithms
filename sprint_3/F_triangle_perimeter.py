from typing import List


def get_biggest_perimeter(sides: List[int]):
    sides.sort(reverse=True)
    c, a, b = 0, 1, 2
    for _ in range(len(sides) - 2):
        if sides[c] < (sides[a] + sides[b]):
            return sides[a] + sides[b] + sides[c]
        c, a, b = c + 1, a + 1, b + 1


def main():
    _ = int(input())
    sides = [int(i) for i in input().split()]
    result = get_biggest_perimeter(sides)
    print(result)


if __name__ == '__main__':
    main()
