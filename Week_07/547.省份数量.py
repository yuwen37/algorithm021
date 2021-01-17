#
# @lc app=leetcode.cn id=547 lang=python
#
# [547] 省份数量
#

# @lc code=start
class UF(object):
    def __init__(self,size):
        self.p = [i for i in range(size)]
    
    def union(self, x, y):
        self.p[self.parent(x)] = self.parent(y)
    
    def parent(self, x):
        root = x
        while self.p[root] != root:
            root = self.p[root]
        while self.p[x] != root:
            self.p[x],x=root,self.p[x]
        return root

        
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        uf = UF(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
        return len({uf.parent(x) for x in uf.p})
                
# @lc code=end

