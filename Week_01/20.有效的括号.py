#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '[':']','{':'}'}
        stack = []
        for i in s:
            if stack and i == dic.get(stack[-1],0):
                stack.pop()
            else :
                stack.append(i)
        return not stack
# @lc code=end

