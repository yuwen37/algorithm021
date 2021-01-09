#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # # 贪心
        # incomes = 0
        # if len(prices) <= 1:return 0
        # for i in range(len(prices) - 1):
        #     if prices[i] < prices[i + 1]:
        #         incomes += prices[i + 1] - prices[i]
        # return incomes

        # 动态规划
        # dp[i][0] 第i天手里持有股票的最大收益
        # dp[i][1] 第i天手里没有股票的最大收益
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return dp[-1][1]
# @lc code=end

