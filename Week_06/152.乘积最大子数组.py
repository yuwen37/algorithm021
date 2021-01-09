#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i][0] 前i个子数组中的最大连续子数组乘积
        # dp[i][1] 前i个子数组中的最小连续子数组乘积
        n = len(nums)
        dp = [[nums[0]] * 2 for _ in range(n)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
            dp[i][1] = min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
        return max(map(lambda x:x[0], dp))
# @lc code=end

