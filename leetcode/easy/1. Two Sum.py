# https://leetcode.com/problems/two-sum/description/
from utils import assert_this


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

if __name__ == '__main__':
    under_test = Solution().twoSum

    test_cases = [
        (under_test([2, 7, 11, 15], 9),  [0, 1]),
        (under_test([3, 2, 4], 6), [1, 2]),
        (under_test([3, 3], 6), [0, 1]),
    ]

    for result, expected in test_cases:
        assert_this(result, expected)
