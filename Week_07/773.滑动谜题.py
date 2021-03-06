#
# @lc app=leetcode.cn id=773 lang=python
#
# [773] 滑动谜题
#

# @lc code=start
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # 双向BFS
        dic = {0:(1,3),1:(0,2,4),2:(1,5),3:(0,4),4:(1,3,5),5:(2,4)}
        board = tuple(board[0] + board[1])
        if board == (1,2,3,4,5,0):return 0
        front = {board}
        back = {(1,2,3,4,5,0)}
        step = 0
        visited = front | back
        while front:
            step += 1
            next_front = set()
            for board in front:
                zero = board.index(0)
                for zero_next in dic[zero]:
                    next_board = list(board)
                    next_board[zero_next],next_board[zero] = next_board[zero],next_board[zero_next]
                    next_board = tuple(next_board)
                    if next_board in back:
                        return step
                    if next_board not in visited:
                        visited.add(next_board)
                        next_front.add(next_board)
            front = next_front
            if len(front) > len(back):
                front, back = back, front
        return -1


        # # BFS
        # dic = {0:(1,3),1:(0,2,4),2:(1,5),3:(0,4),4:(1,3,5),5:(2,4)}
        # board = tuple(board[0] + board[1])
        # deq = deque([(board, board.index(0), 0)])
        # visited = set()
        # visited.add(board)
        # while deq:
        #     board, zero, step = deq.popleft()
        #     if board == (1,2,3,4,5,0):
        #         return step
        #     for next_zero in dic[zero]:
        #         next_board = list(board)
        #         next_board[zero],next_board[next_zero] = next_board[next_zero],next_board[zero]
        #         next_board = tuple(next_board)
        #         if next_board not in visited:
        #             deq.append((next_board, next_zero, step + 1))
        #             visited.add(next_board)
        # return -1
# @lc code=end

