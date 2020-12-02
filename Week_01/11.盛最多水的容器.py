#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = (right - left) * min(height[left], height[right])
        while left < right:
            if  height[left] > height[right]:
                right -= 1
            else:
                left += 1
            area = max(area, (right - left) * min(height[left], height[right]))
        return area
# @lc code=end

