#
# @lc app=leetcode.cn id=1021 lang=python
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        ans = ''
        stack = []
        for c in S:
            if c == "(":
                if stack:
                    ans += c
                stack.append(c)
            else:
                stack.pop()
                if stack:
                    ans += c
        return ans

# @lc code=end

