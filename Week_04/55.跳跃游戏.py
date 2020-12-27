#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        most = 0 # 最远可到达的地方
        for i in range(len(nums)):
            if i <= most:
                most = max(nums[i] + i, most)
                if most >= len(nums) - 1: return True
        return False

# @lc code=end

