#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 自定义字典
        dic_s = defaultdict(int)
        dic_t = defaultdict(int)
        for i in s:
            dic_s[i] += 1
        for j in t:
            dic_t[j] += 1
        return dic_s == dic_t

        # 用库定义字典
        dic_s = collections.Counter(s)
        dic_t = collections.Counter(t)
        return dic_s == dic_t
# @lc code=end

