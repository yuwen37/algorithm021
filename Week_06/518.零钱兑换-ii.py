#
# @lc app=leetcode.cn id=518 lang=python
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # dp[i] 总金额为i需要凑齐的硬币组合数
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    dp[i] = dp[i] + dp[i - coin]
        return dp[-1]
        
# @lc code=end

