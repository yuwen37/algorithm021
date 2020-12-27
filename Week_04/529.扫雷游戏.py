#
# @lc app=leetcode.cn id=529 lang=python
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        direction = ((1, 1), (1, 0), (1, -1), (0, 1),
                     (0, -1), (-1, 1), (-1, 0), (-1, -1))
        i, j = click
        # 判断当前点击点是否有雷
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        m, n = len(board), len(board[0])
        def check(i, j):
            count = 0
            for x, y in direction:
                if (0 <= x + i <= m - 1 and 0 <= y + j <= n - 1 and 
                    board[i + x][j + y] == 'M'):
                    count += 1
            return count
        def dfs(i, j):
            # 检查周围有几颗雷
            count = check(i, j)
            if count == 0:
                board[i][j] = 'B'
                for x, y in direction:
                    if (0 <= x + i <= m - 1 and 0 <= y + j <= n - 1 and 
                        board[i + x][j + y] == 'E'):
                        dfs(x + i, y + j)
            else:
                board[i][j] = str(count)
        dfs(i, j) # 递归的揭露
        return board
# @lc code=end

