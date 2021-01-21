#
# @lc app=leetcode.cn id=338 lang=python
#
# [338] 比特位计数
#

# @lc code=start
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] * (num+1)
        for i in range(1,num+1):
            dp[i] = dp[i&(i-1)] + 1
        return dp
        
# @lc code=end

