# https://www.codewars.com/kata/514b92a657cdc65150000006
from unittest import TestCase


def solution(number):
    return sum((i for i in range(number) if 0 in [i % 3, i % 5]))


class Test(TestCase):
    def test_solution(self):
        print(solution(10))
        assert solution(10) == 23
        assert solution(4) == 3
        assert solution(6) == 8
        assert solution(3) == 0
        assert solution(5) == 3


