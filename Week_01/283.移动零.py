#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = 0 # 记录非零元素改填入的位置
        for i in range(len(nums)):
            if nums[i] != 0:
                # 答案提供的思路
                # nums[index] = nums[i]
                # if i != index:
                #     nums[i] = 0
                # index += 1

                # 自己思考后的答案（本质上是双指针）
                nums[index], nums[i]= nums[i], nums[index]
                index += 1
        return nums
# @lc code=end

