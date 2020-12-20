#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        return max(count.keys(), key=count.get)
        # 高级用法：max(可迭代对象， key=函数名)
# @lc code=end

