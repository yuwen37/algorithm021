#
# @lc app=leetcode.cn id=714 lang=python
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # 动态规划
        # dp[i][0] 第i天手里持有股票的最大收益
        # dp[i][1] 第i天手里没有股票的最大收益
        # 和买卖股票2唯一的区别就是卖出减去个手续费就行了，其他一样
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)
        return dp[-1][1]
# @lc code=end

