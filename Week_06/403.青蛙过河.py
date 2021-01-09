#
# @lc app=leetcode.cn id=403 lang=python
#
# [403] 青蛙过河
#

# @lc code=start
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)
        # dp[i] 表示：跳到第 i 个石头的最后一步距离是 need 时能否成功。need是dp[i]里面的数字
        dp = [set() for _ in range(n)]
        dp[0].add(0)
        for i in range(1, n):
            for j in range(i):
                need = stones[i] - stones[j]
                # if need in dp[j] or need + 1 in dp[j] or need - 1 in dp[j]:
                if (set((need, need + 1, need - 1)) & dp[j]) != set():
                    dp[i].add(need)
        return dp[-1] != set()
# @lc code=end

