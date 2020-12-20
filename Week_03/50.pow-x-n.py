#
# @lc app=leetcode.cn id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 分治
        if n == 0: return 1
        if x == 0: return 0
        if n < 0: x, n = 1 / x, -n
        def recur(x, n):
            if n == 1:return x
            half = recur(x, n // 2)
            if n % 2 == 1: 
                return half * half * x
            else:
                return half * half
        return recur(x, n)

# @lc code=end

