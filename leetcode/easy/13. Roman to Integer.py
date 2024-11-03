# https://leetcode.com/problems/roman-to-integer/
from utils import assert_this


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        length_roman_number = len(s)
        arabic_number = 0
        for ind, roman_num in enumerate(s):
            # Если это число последнее или оно больше, чем следующее, то прибавляем его к результату
            if ind == length_roman_number -1 or roman_numerals[roman_num] >= roman_numerals[s[ind + 1]]:
                arabic_number += roman_numerals[roman_num]
            # иначе вычитаем (например, IX. Один меньше девяти, значит -1 + 10 = 9)
            else:
                arabic_number -= roman_numerals[roman_num]
        return arabic_number

if __name__ == '__main__':
    under_test = Solution().romanToInt

    test_cases = [
        (under_test('III'),  3),
        (under_test('LVIII'), 58),
        (under_test('MCMXCIV'), 1994),
    ]

    for result, expected in test_cases:
        assert_this(result, expected)