#
# @lc app=leetcode.cn id=36 lang=python
#
# [36] 有效的数独
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [defaultdict(int) for _ in range(9)]
        col = [defaultdict(int) for _ in range(9)]
        box = [defaultdict(int) for _ in range(9)]
        for i in range(9):
            for j in range(9):
                index = i // 3 * 3 + j // 3
                if board[i][j] != '.':
                    row[i][int(board[i][j])] += 1
                    col[j][int(board[i][j])] += 1
                    box[index][int(board[i][j])] += 1
                    if row[i][int(board[i][j])] > 1 or col[j][int(board[i][j])] > 1 or box[index][int(board[i][j])] > 1:
                        return False
        return True


# @lc code=end

