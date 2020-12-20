#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(left, right, tmp):
            if left == n and right == n:
                ans.append(tmp)
            if left < n: backtrack(left + 1, right, tmp + "(")
            if right < left: backtrack(left, right + 1, tmp + ")")
        ans = []
        backtrack(0, 0, '')
        return ans
# @lc code=end

