#
# @lc app=leetcode.cn id=190 lang=python
#
# [190] 颠倒二进制位
#

# @lc code=start


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        cnt = 31
        while n:
            ans += (n&1)<<cnt
            cnt-=1
            n>>=1
        return ans
        
# @lc code=end

