#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:return len(nums)
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]     
            fast += 1
        return slow + 1
# @lc code=end

