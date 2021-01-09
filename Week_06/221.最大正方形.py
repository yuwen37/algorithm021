#
# @lc app=leetcode.cn id=221 lang=python
#
# [221] 最大正方形
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # dp[i][j]表示以(i,j)为右下角的最大正方形边长
        m, n = len(matrix), len(matrix[0])
        dp = matrix
        for i in range(m):
            dp[i][0] = int(dp[i][0])
        for j in range(n):
            dp[0][j] = int(dp[0][j])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0
        return max(map(max, dp))**2
# @lc code=end

