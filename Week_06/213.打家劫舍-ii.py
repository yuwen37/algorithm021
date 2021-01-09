#
# @lc app=leetcode.cn id=213 lang=python
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 把问题分成偷nums[:-1]和nums[1:]
        def sub_rob(nums):
            # dp[i] 偷了前i家房屋的最大收益
            n = len(nums)
            if n == 0: return 0
            if len(nums) <= 2: return max(nums)
            dp = nums
            dp[1] = max(dp[:2])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]
        return max(sub_rob(nums[:-1]), sub_rob(nums[1:])) if len(nums) > 1 else nums[0]
# @lc code=end

