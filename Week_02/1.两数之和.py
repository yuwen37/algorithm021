#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # dic = {}
        # for i in range(len(nums)):
        #     if target - nums[i] not in dic:
        #         dic[nums[i]] = i
        #     else:
        #         return [dic[target - nums[i]], i]

        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [dic[target - nums[i]], i]
            dic[nums[i]] = i

# @lc code=end

