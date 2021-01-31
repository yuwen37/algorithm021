#
# @lc app=leetcode.cn id=115 lang=python
#
# [115] 不同的子序列
#

# @lc code=start
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m,n = len(s)+1, len(t)+1
        dp = [[0]*n for _ in range(m)]
        # dp[i][j] t的前j个字符能有s的前i个组成的个数
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

# @lc code=end
