#
# @lc app=leetcode.cn id=312 lang=python
#
# [312] 戳气球
#

# @lc code=start
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i][j] 从第i个气球到第j个气球（i，j不戳破）全部戳破能获得的最大硬币
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for j in range(2, n):
            for i in range(j - 2, -1, -1):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i]*nums[j]*nums[k], dp[i][j])
        return dp[0][-1]
# @lc code=end

