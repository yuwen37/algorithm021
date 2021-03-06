#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # DFS
        def dfs(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or grid[i][j] == '0':return
            grid[i][j] = '0'
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i - 1, j)
            dfs(i + 1, j)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j) # 把i，j的岛屿归零，同时把周围的岛屿归零
                    count += 1
        return count

        # BFS
        def bfs(i, j):
            deq = deque([(i, j)])
            while deq:
                i, j = deq.popleft()
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    deq.extend([(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)])
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1
        return count
# @lc code=end

