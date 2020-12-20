#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(tmp, nums):
            if len(tmp) == n:
                ans.append(tmp)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:continue
                backtrack(tmp + [nums[i]], nums[:i] + nums[i + 1:])

        n = len(nums)
        ans = []
        nums.sort()
        backtrack([], nums)
        return ans
# @lc code=end

