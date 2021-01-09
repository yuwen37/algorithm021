#
# @lc app=leetcode.cn id=647 lang=python
#
# [647] 回文子串
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i][j] 表示从第i到第j个字符是否是回文子串，是返回1
        dp = [[0] * len(s) for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j + 1):
                if i == j:
                    dp[i][j] = 1
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                elif s[i] == s[j] and dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1
        return sum(map(sum, dp))
        
# @lc code=end

