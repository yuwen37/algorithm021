#
# @lc app=leetcode.cn id=387 lang=python
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = Counter(s)
        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i
        return -1
# @lc code=end

