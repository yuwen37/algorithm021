#
# @lc app=leetcode.cn id=188 lang=python
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # 动态规划
        # dp[i][0] 第i天初始化状态股票的最大收益
        # dp[i][2 * j + 1] 第i天第j + 1次持有股票的最大收益
        # dp[i][2 * j + 1] 第i天第j + 1次没有股票的最大收益
        # n = len(prices)
        # if n < 2: return 0
        # dp = [[0] * (2 * k + 1) for _ in range(n)]
        # dp[0][0] = 0
        # for j in range(k):
        #     dp[0][2 * j + 1] = -prices[0]
        #     dp[0][2 * j + 2] = 0
        # for i in range(1, n):
        #     dp[i][0] = 0
        #     for j in range(k):
        #         dp[i][2 * j + 1] = max(dp[i - 1][2 * j + 1], dp[i - 1][2 * j] - prices[i])
        #         dp[i][2 * j + 2] = max(dp[i - 1][2 * j + 2], dp[i - 1][2 * j + 1] + prices[i])
        # return max(dp[-1])

        # 同样用类似购买股票3的方式优化空间（用一维数组，但是我已经快看不懂了）
        n = len(prices)
        if n < 2: return 0
        dp = [0] * (2 * k + 1)
        dp[0] = 0
        for j in range(k):
            dp[2 * j + 1] = -prices[0]
            dp[2 * j + 2] = 0
        for i in range(1, n):
            dp[0] = 0
            for j in range(k):
                dp[2 * j + 1] = max(dp[2 * j + 1], dp[2 * j] - prices[i])
                dp[2 * j + 2] = max(dp[2 * j + 2], dp[2 * j + 1] + prices[i])
        return max(dp)
# @lc code=end

