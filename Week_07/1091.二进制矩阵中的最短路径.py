#
# @lc app=leetcode.cn id=1091 lang=python
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 双向BFS
        direction = ((1,0),(1,-1),(1,1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1))
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:return -1
        n = len(grid)
        if n == 1:return 1
        front = {(0,0)}
        back = {(n - 1,n - 1)}
        grid[0][0] = 1
        step = 0
        while front:
            step += 1
            front_next = set()
            for i,j in front:
                for x,y in direction:
                    x,y=x+i,y+j
                    # 注意：下面两句话只能写在这部分，不能往下也不能往上。
                    # 往上往下都不可能让(x,y)在back里，因此下面的grid[x][y] = 1去重了
                    if (x,y) in back:
                        return step + 1
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        front_next.add((x,y))
                        grid[x][y] = 1
            front = front_next
            if len(back) < len(front):
                front,back=back,front
        return -1

        # 双向BFS
        # direction = ((1,0),(1,-1),(1,1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1))
        # if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:return -1
        # n = len(grid)
        # front = {(0,0)}
        # back = {(n - 1,n - 1)}
        # visited = front | back
        # grid[0][0] = 1
        # step = 1
        # while front:
        #     front_next = set()
        #     for i,j in front:
        #         if (i,j) in back:
        #             return step
        #         for x,y in direction:
        #             x,y=x+i,y+j
        #             if (x,y) in back:
        #                 return step + 1
        #             if 0 <= x < n and 0 <= y < n and grid[x][y] == 0 and (x,y) not in visited:
        #                 front_next.add((x,y))
        #                 visited.add((x,y))
        #                 # grid[x][y] = 1
        #     front = front_next
        #     if len(back) < len(front):
        #         front,back=back,front
        #     step += 1
        # return -1

        # # BFS
        # direction = ((1,0),(1,-1),(1,1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1))
        # if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:return -1
        # deq = deque([(0,0,1)])
        # grid[0][0] = 1
        # n = len(grid)
        # while deq:
        #     for _ in range(len(deq)):
        #         i,j,step = deq.popleft()
        #         if (i,j) == (n-1,n-1):return step
        #         for x,y in direction:
        #             x,y=x+i,y+j
        #             if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
        #                 deq.append((x,y,step + 1))
        #                 grid[x][y] = 1
        # return -1
# @lc code=end

