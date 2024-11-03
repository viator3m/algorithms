# https://leetcode.com/problems/palindrome-number/description/
from utils import assert_this


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        temp = x
        reverse = 0
        while temp:
            reverse = reverse * 10 + temp % 10
            temp = temp // 10

        return x - reverse == 0


if __name__ == '__main__':
    under_test = Solution().isPalindrome

    test_cases = [
        (under_test(121),  True),
        (under_test(-121), False),
        (under_test(10), False),
    ]

    for result, expected in test_cases:
        assert_this(result, expected)
