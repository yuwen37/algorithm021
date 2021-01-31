#
# @lc app=leetcode.cn id=10 lang=python
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        def dp(i, j):
            if (i,j) in memo: return memo[(i,j)]
            if len(p) == j:return len(s) == i
            ismatch = i < len(s) and (p[j] in {'.', s[i]})
            if j+1<len(p) and p[j+1] == '*':
                ans = dp(i,j+2) or (ismatch and dp(i+1,j))
            else:
                ans = (ismatch and dp(i+1,j+1))
            memo[(i,j)] = ans
            return ans
        return dp(0,0)
# @lc code=end

