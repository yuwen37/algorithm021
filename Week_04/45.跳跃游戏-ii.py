#
# @lc app=leetcode.cn id=45 lang=python
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        most = 0 # 每一个数字最远可到达的地方
        step_most = 0 # 每一步最远可到达的地方
        count = 0 # 记录步数
        # 如果访问最后一个元素，在边界正好为最后一个位置的情况下，
        # 我们会增加一次「不必要的跳跃次数」，因此我们不必访问最后一个元素。
        for i in range(len(nums) - 1):
            if i <= most:
                most = max(nums[i] + i, most)
                if i == step_most:
                    step_most = most
                    count += 1               
        return count
# @lc code=end

