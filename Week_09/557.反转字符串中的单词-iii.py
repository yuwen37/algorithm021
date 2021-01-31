#
# @lc app=leetcode.cn id=557 lang=python
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s = s.strip().split(' ')
        # for i in range(len(s)):
        #     s[i] = s[i][::-1]
        # return ' '.join(s)

        return ' '.join(s[::-1].split(' ')[::-1])
# @lc code=end

