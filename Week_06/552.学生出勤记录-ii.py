#
# @lc app=leetcode.cn id=552 lang=python
#
# [552] 学生出勤记录 II
#

# @lc code=start
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] 代表不考虑A的情况下，可被奖励的的记录数
        # dp[i - 1] 代表以P为最后一个数字
        # dp[i - 2] 代表以PL为最后两个数字
        # dp[i - 3] 代表以PLL为最后三个数字
        dp = [0] * max(n + 1, 3) # 考虑了n = 0,1,2的情况
        mod = 10**9+7
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod
        res = dp[n]
        # A可以替换1-n个数字中的任意一个，所以从1遍历到n
        for i in range(1, n + 1):
            res += (dp[i - 1] * dp[n - i]) % mod
        return res % mod

# @lc code=end

