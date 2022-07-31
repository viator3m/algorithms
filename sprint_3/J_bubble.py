from typing import List


def bubble(array: List[int], length: int) -> None:
    length -= 1
    printed = 0
    for i in range(length):
        sorted = 0
        for j in range(length - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                sorted += 1
        if sorted:
            printed += 1
            print(*array)
    if not printed:
        print(*array)


def main():
    length = int(input())
    array = list(map(int, input().strip().split()))
    bubble(array, length)


if __name__ == '__main__':
    main()
