#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i] 代表以第i个字符结尾的字符串最长有效括号长度
        n = len(s)
        dp = [0] * n
        for i in range(n):
            if i > 0 and s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                else:
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2
        dp.append(0)
        return max(dp)
# @lc code=end

