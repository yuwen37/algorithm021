#
# @lc app=leetcode.cn id=1122 lang=python
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # 计数排序
        upper = max(arr1) + 1
        freq = [0]*upper
        for x in arr1:
            freq[x] +=1
        arr = []
        for x in arr2:
            arr.extend([x]*freq[x])
            freq[x] = 0
        for x in range(upper):
            arr.extend([x]*freq[x])
        return arr

# @lc code=end

