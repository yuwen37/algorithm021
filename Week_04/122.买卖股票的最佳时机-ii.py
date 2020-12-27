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
        # 贪心
        incomes = 0
        if len(prices) <= 1:return 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                incomes += prices[i + 1] - prices[i]
        return incomes
# @lc code=end

