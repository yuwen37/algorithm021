#
# @lc app=leetcode.cn id=37 lang=python
#
# [37] 解数独
#

# @lc code=start
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        nums = set('123456789')
        blank = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    blank.append((i,j))
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[i // 3 * 3 + j // 3].add(board[i][j])

        def dfs(n):   
            if n == len(blank):
                return True
            i,j = blank[n]
            rest = nums - row[i] - col[j] - box[i // 3 * 3 + j // 3] # 还剩的可以填的数字
            if not rest:
                return False

            for num in rest:
                board[i][j] = num
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[i // 3 * 3 + j // 3].add(board[i][j])
                if dfs(n + 1):
                    return True
                row[i].remove(board[i][j])
                col[j].remove(board[i][j])
                box[i // 3 * 3 + j // 3].remove(board[i][j])
                board[i][j] = '.'
        
        dfs(0)
# @lc code=end

