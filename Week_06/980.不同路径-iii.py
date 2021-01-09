#
# @lc app=leetcode.cn id=980 lang=python
#
# [980] 不同路径 III
#

# @lc code=start
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 本来想用动态规划的，但无奈官方题解以及有动态规划解析的答案都含有位运算，暂时还没学会
        # 等学会了再来看吧
        # 回溯方法
        direction = ((1,0),(-1,0),(0,1),(0,-1))
        def dfs(i, j, index):
            if grid[i][j] == 2:
                if index == cnt:
                    self.ans += 1
                return 
            for x, y in direction:
                x += i
                y += j
                if 0<= x < m and 0 <= y < n:
                    if grid[x][y] == 0:
                        grid[x][y] = 1
                        dfs(x, y, index + 1)
                        grid[x][y] = 0
                    elif grid[x][y] == 2:
                        dfs(x, y, index)
        self.ans = 0 # 记录路径数
        cnt = 0 # 统计所有需要走的格子数
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    cnt += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i ,j, 0) # 坐标及已经经过的格子
        return self.ans     
# @lc code=end

