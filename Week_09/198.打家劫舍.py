#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] 偷了前i家房屋的最大收益
        n = len(nums)
        dp = nums
        if nums == []: return 0
        if n <= 2:return max(nums)
        dp[1] = max(dp[:2]) 
        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]

# @lc code=end

