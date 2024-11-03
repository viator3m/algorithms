# https://www.codewars.com/kata/52597aa56021e91c93000cb0/
from unittest import TestCase


def move_zeros(arr: list[int]) -> list[int]:
    num = [i for i in arr if i != 0]
    return num + ([0] * (len(arr) - len(num)))


class MyTest(TestCase):
    def test(self):
        assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
        assert move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        assert move_zeros([0, 0]) == [0, 0]
        assert move_zeros([0]) == [0]
