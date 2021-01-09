#
# @lc app=leetcode.cn id=363 lang=python
#
# [363] 矩形区域不超过 K 的最大数值和
#

# @lc code=start
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(n):
            nums = [0] * m
            for right in range(left, n):
                for i in range(m):
                    nums[i] += matrix[i][right]
                arr = [0] # 只能初始化0,没有想通为什么
                cum = 0
                for num in nums:
                    cum += num
                    loc = bisect.bisect_left(arr, cum - k)
                    if loc < len(arr):
                        res = max(cum - arr[loc], res)
                    bisect.insort(arr, cum)
        return res

# @lc code=end

