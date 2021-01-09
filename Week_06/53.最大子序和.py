#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] 表示第i个字符结尾的最大连续子数组和
        n = len(nums)
        if n == 0: return 0
        dp = [nums[0]] * n
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)
# @lc code=end

