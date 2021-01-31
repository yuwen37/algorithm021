#
# @lc app=leetcode.cn id=541 lang=python
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        flag = True
        res = ''
        for i in range(0, len(s), k):
            res += s[i:i+k][::-1] if flag else s[i:i+k]
            flag = not flag
        return res

# @lc code=end

