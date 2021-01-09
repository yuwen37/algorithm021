#
# @lc app=leetcode.cn id=309 lang=python
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 动态规划
        # dp[i][0] 第i天(非卖出日)不持有股票的最大收益
        # dp[i][1] 第i天持有股票的最大收益
        # dp[i][2] 第i天卖出股票的最大收益
        if len(prices) < 2: return 0
        n = len(prices)
        dp = [[0]*3 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]
        return max(dp[-1])

# @lc code=end

