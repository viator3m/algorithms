# https://leetcode.com/problems/longest-common-prefix/
from utils import assert_this


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        ind = 0
        while True:
            try:
                if len(set([string[ind] for string in strs])) == 1:
                    prefix += strs[0][ind]
                else:
                    return prefix
            except IndexError:
                return prefix

            ind += 1


if __name__ == '__main__':
    under_test = Solution().longestCommonPrefix

    test_cases = [
        (under_test(["flower","flow","flight"]),  'fl'),
        (under_test(["dog","racecar","car"]), ''),
    ]

    for result, expected in test_cases:
        assert_this(result, expected)