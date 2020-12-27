#
# @lc app=leetcode.cn id=153 lang=python
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # 这是循环前升序排列的数，左边的数小，右边的数大，
            # 而且我们要找的是最小值，要偏向左找，目标值右边的情况会比较简单
            # 目的就是让最终停留的点是最小值点
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
        return nums[left]

# @lc code=end

