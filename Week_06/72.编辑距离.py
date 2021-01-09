#
# @lc app=leetcode.cn id=72 lang=python
#
# [72] 编辑距离
#

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp[i][j] 表示从word1的前i个字符变成word2的前j个字符需要的最少操作数
        m, n = len(word1) + 1, len(word2) + 1
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if 0 in (i, j):
                    dp[i][j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]
# @lc code=end

