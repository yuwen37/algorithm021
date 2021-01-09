#
# @lc app=leetcode.cn id=123 lang=python
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # # 动态规划
        # # dp[i][0] 第i天初始化状态股票的最大收益
        # # dp[i][1] 第i天第一次持有（含买入）股票的最大收益
        # # dp[i][0] 第i天第一次不持有(含卖出)股票的最大收益
        # # dp[i][1] 第i天第二次持有（含买入）股票的最大收益
        # # dp[i][0] 第i天第二次不持有(含卖出)股票的最大收益
        # n = len(prices)
        # dp = [[0] * 5 for _ in range(n)]
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        # dp[0][2] = 0
        # dp[0][3] = -prices[0]
        # dp[0][4] = 0
        # for i in range(1, n):
        #     dp[i][0] = 0
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        #     dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
        #     dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
        #     dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        # return max(dp[-1])

        # 可优化
        n = len(prices)
        dp = [[0] * 5 for _ in range(n)]
        dp0 = 0
        dp1= -prices[0]
        dp2 = 0
        dp3 = -prices[0]
        dp4 = 0
        for i in range(1, n):
            dp0 = 0
            dp1 = max(dp1, dp0 - prices[i])
            dp2 = max(dp2, dp1 + prices[i])
            dp3 = max(dp3, dp2 - prices[i])
            dp4 = max(dp4, dp3 + prices[i])
        return max(dp1,dp2,dp3,dp4)
# @lc code=end

