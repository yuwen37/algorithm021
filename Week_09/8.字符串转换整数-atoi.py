#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s.strip())
        if len(s)==0:return 0
        sign = -1 if s[0] == '-' else 1
        if s[0] in '-+':
            s.pop(0)
        ans = 0
        for c in s:
            if c.isdigit():
                ans = ans * 10 + int(c)
            else:
                break 
        return max(min(sign*ans, 2**31-1), -2**31)
# @lc code=end

