#
# @lc app=leetcode.cn id=74 lang=python
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid // n][mid % n] == target:return True
            if matrix[mid // n][mid % n] < target:
                left = mid + 1
            else:
                right = mid
        return matrix[left // n][left % n] == target
# @lc code=end

