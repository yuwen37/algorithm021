#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        s = lower(s)
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif  not s[j].isalnum():
                j -= 1
            else:
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
        return True
# @lc code=end

