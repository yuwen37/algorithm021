#
# @lc app=leetcode.cn id=917 lang=python
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = []
        for c in S:
            if c.isalpha():
                s.append(c)
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(s.pop())
            else:
                ans.append(c)
        return ''.join(ans) 

      
# @lc code=end

