#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(tmp, index):
            ans.append(tmp)
            for i in range(index, n):
                backtrack(tmp + [nums[i]], i + 1)
        ans = []
        n = len(nums)
        backtrack([], 0)
        return ans
# @lc code=end

