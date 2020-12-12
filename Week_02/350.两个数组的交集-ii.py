#
# @lc app=leetcode.cn id=350 lang=python
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        count = Counter(nums1)
        ans = []
        for i in range(len(nums2)):
            if count.get(nums2[i], 0) > 0:
                count[nums2[i]] -= 1
                ans.append(nums2[i])
        return ans
# @lc code=end

