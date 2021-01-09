#
# @lc app=leetcode.cn id=91 lang=python
#
# [91] 解码方法
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i] 第i个数字前的解码方法
        if s[0] == '0': return 0
        n = len(s) + 1
        dp = [1] * n
        for i in range(2, n):
            if s[i - 1] == '0' and s[i - 2] not in '12':
                return 0
            elif s[i - 1] == '0' and s[i - 2] in '12':
                dp[i] = dp[i - 2]
            elif '10' < s[i - 2:i] <= '26':
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]

# @lc code=end

