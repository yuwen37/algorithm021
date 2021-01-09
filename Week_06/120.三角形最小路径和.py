#
# @lc app=leetcode.cn id=120 lang=python
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # dp[i][j] 从下到上（i，j）的最小路径和
        dp = triangle
        for i in range(len(dp) - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]
# @lc code=end

