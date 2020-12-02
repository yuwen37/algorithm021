#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 方法一：韦恩图思想, 思想简单, 代码简单, 过目难忘
        s1 = s2 = 0
        max1 = max2 = 0
        n = len(height)
        for i in range(n):
            if max1 < height[i]:
                max1 = height[i]
            if max2 < height[n - 1 - i]:
                max2 = height[n - 1 - i]
            s1 += max1
            s2 += max2
        ans = s1 + s2 - n * max1 - sum(height)
        return ans
# @lc code=end

