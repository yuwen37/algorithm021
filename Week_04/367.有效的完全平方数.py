#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 方法一、这道题本质上和69.x的平方根没什么区别，用其思路可以写成如下
        left, right = 0, num
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid * mid <= num:
                left = mid
            else:
                right = mid - 1
        return left * left == num 

        # 方法二、由于这道题有提前返回条件mid * mid == num,所以可以写成如下
        left, right = 0, num
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid * mid == num: return True
            if mid * mid < num:
                left = mid
            else:
                right = mid - 1
        return False 
# @lc code=end

