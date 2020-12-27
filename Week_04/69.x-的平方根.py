#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 方法一(套模板的写法如下)
        left, right = 0, x
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid * mid == x: return mid
            if mid * mid < x:
                left = mid
            else:
                right = mid - 1
        return left

        # 方法二（对于上面的判断可以合并成如下）
        left, right = 0, x
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid * mid <= x:
                left = mid
            else:
                right = mid - 1
        return left
# @lc code=end

