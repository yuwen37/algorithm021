#
# @lc app=leetcode.cn id=52 lang=python
#
# [52] N皇后 II
#

# @lc code=start
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 位运算法
        def dfs(i,j,pie,na):
            if i == n:
                self.ans += 1
                return
            
            bit = (~(j|pie|na)&((1<<n)-1))
            # ~(j|pie|na)找到所有空位，空位为1，
            # x&((1<<n)-1) 可以把x的n位以上的数字归零
            while bit:
                p = bit & -bit # 取最小位1
                bit &= (bit-1) # 打掉最小位1    
                dfs(i+1,j|p,(pie|p)<<1,(na|p)>>1)
            
        if n < 1:return []
        self.ans = 0
        dfs(0,0,0,0)
        return self.ans
# @lc code=end

