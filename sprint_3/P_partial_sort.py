from typing import List


def get_block(array: List[int]) -> int:
    block = values = indexes = 0
    for i in range(len(array)):
        values += array[i]
        indexes += i
        if values == indexes:
            block += 1
            values = indexes = 0
        i += 1
    return block


class Test:
    def test_1(self):
        a = [3, 2, 0, 1, 4, 6, 5]
        assert get_block(a) == 3

    def test_2(self):
        a = [0, 1, 3, 2]
        assert get_block(a) == 3

    def test_3(self):
        a = [3, 6, 7, 4, 1, 5, 0, 2]
        assert get_block(a) == 1


def main():
    _, array = int(input()), [int(i) for i in input().split()]
    print(get_block(array))


if __name__ == '__main__':
    main()
