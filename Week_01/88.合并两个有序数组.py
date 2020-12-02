#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 从后往前
        index = m + n - 1 
        index1 = m - 1
        index2 = n - 1
        while (index1>=0 and index2>=0):
            if nums1[index1] < nums2[index2]:
                nums1[index] = nums2[index2]
                index2 -= 1
            else:
                nums1[index] = nums1[index1]
                index1 -= 1
            index -= 1
        # 补尾
        if index2>=0:
            nums1[:index2 + 1] = nums2[:index2 + 1]

# @lc code=end

