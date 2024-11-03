# https://leetcode.com/problems/valid-parentheses/description/
from utils import assert_this

"""
Если скобка открывается, то добавляем её во временный список
Если список не пустой и скобка закрывает последнюю скобку в списке, то удаляем последнюю скобку в списке
Иначе (скобка закрывающая, но она не закрывает последнюю скобку в списке) добавляем её в список

Если список в итоге пустой, то возвращаем True
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets_map = {'(': ')', '[': ']', '{': '}'}
        seq = list()
        for bracket in s:
            if bracket in brackets_map.keys():
                seq.append(bracket)
            elif bool(seq) and bracket == brackets_map[seq[-1]]:
                seq.pop()
            else:
                seq.append(bracket)
                break
        return not bool(seq)

if __name__ == '__main__':
    under_test = Solution().isValid

    test_cases = [
        (under_test("()"),  True),
        (under_test("(()[[]{}])"), True),
        (under_test("(]"), False),
        (under_test("([])"), True),
    ]

    for result, expected in test_cases:
        assert_this(result, expected)