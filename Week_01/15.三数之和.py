#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        if len(nums) < 3:return []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            j = i + 1
            k = len(nums) - 1 
            while j < k:
                sum_3 = nums[i] + nums[j] + nums[k]
                if sum_3 == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                if sum_3 > 0:
                    k -= 1
                if sum_3 < 0:
                    j += 1
                # 判重
                while j < k and j - 1 > i and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and k + 1 < len(nums) and nums[k] == nums[k + 1]:
                    k -= 1
        return res
 
# @lc code=end

