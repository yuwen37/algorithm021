#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i]第i天的历史最低价
        if len(prices) < 2: return 0
        n = len(prices)
        dp = [prices[0]] * n
        max_profit = 0
        for i, price in enumerate(prices[1:]):
            dp[i] = min(dp[i - 1], price)
            max_profit = max(max_profit, price - dp[i])
        return max_profit
# @lc code=end

