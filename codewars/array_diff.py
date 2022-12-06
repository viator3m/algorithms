# https://www.codewars.com/kata/523f5d21c841566fde000009

def array_diff(a: list[int], b: list[int]) -> list:
    for i in b:
        while True:
            try:
                a.remove(i)
            except ValueError:
                break
    return a


def array_diff_good(a, b):
    return [x for x in a if x not in b]


def test():
    assert array_diff([], []) == []
    assert array_diff([1, 2, 2, 2, 3], []) == [1, 2, 2, 2, 3]
    assert array_diff([], [1, 2, 2, 2, 3]) == [1, 2, 2, 2, 3]
    assert array_diff([1, 2, 2, 2, 3], [2]) == [1, 3]
    assert array_diff([20, -20, -2, 12, 12, -14, 14, -12, -18, 2, 17, 1, -16, 2, -18], [-18, 6, -8, -5, -5, -5, 13, -11, -9, -5, 11, 7, 3, 15])

