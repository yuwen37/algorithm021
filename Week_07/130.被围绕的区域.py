#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#

# @lc code=start
class UF(object):
    def __init__(self,size):
        self.p = [i for i in range(size + 1)]
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
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:return
        direction = ((1,0),(-1,0),(0,1),(0,-1))
        m, n = len(board),len(board[0])
        dummy = m*n
        uf = UF(dummy)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i in (0,m-1) or j in (0,n-1):
                        uf.union(i*n+j,dummy)
                    else:
                        for x,y in direction:
                            x,y=x+i,y+j
                            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                                uf.union(i*n+j,x*n+y)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and uf.parent(i*n+j) != uf.parent(dummy):
                    board[i][j] = 'X'
# @lc code=end

