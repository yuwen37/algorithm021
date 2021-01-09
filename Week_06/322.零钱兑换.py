#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[i] 总金额为i需要凑齐的最小硬币数
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] < amount + 1 else -1

# @lc code=end

