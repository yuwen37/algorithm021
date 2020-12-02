#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # # 动态规划
        # # dp[i] 爬第i层楼梯有多少中方法
        # if n < 2: return 1
        # dp = [1]*(n + 1) 
        # dp[1] = 1
        # for i in range(2,n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[-1]

        # 降低空间复杂度
        if n < 2: return 1
        dp0, dp1 = 1, 1
        for i in range(2,n + 1):
            dp2 = dp0 + dp1
            dp0, dp1 = dp1, dp2
        return dp2
# @lc code=end

