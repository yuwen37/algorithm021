#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(tmp, nums):
            if len(tmp) == n:
                ans.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(tmp + [nums[i]], nums[:i] + nums[i + 1:])

        n = len(nums)
        ans = []
        backtrack([], nums)
        return ans
# @lc code=end

