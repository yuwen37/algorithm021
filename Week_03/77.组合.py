#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(tmp, index):
            if len(tmp) == k:
                ans.append(tmp)
                return
            for i in range(index, n):
                backtrack(tmp + [i + 1], i + 1)
        ans = []
        backtrack([], 0)
        return ans
# @lc code=end

