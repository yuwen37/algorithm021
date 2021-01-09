#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] 完全平方数
#

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[j] 代表组合成正整数j需要的最小完全平方数个数
        dp = [i for i in range(n + 1)]
        for j in range(2, n + 1):
            for i in range(int(sqrt(j) + 1)):
                dp[j] = min(dp[j], dp[j - i*i] + 1)
        return dp[-1]

# @lc code=end

