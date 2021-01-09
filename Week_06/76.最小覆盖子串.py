#
# @lc app=leetcode.cn id=76 lang=python
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 这道题似乎没有用到动态规划？
        find = defaultdict(int)
        for c in t:
            find[c] += 1
        min_len = float('inf')
        right = left = 0
        cnt = len(t) # 记录[left:right]区间内的涵盖t字符的数量
        ans = ''
        while right < len(s):
            if find[s[right]] > 0:
                cnt -= 1 
            find[s[right]] -= 1
            right += 1
            # 当cnt == 0，说明找到了全部的t
            while cnt == 0:
                if right - left < min_len:
                    min_len = right - left
                    ans = s[left:right]
                if find[s[left]] == 0:
                    cnt += 1
                find[s[left]] += 1
                left += 1
        return ans


# @lc code=end

