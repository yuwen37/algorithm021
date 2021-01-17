#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N 皇后
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 判断是否冲突
        def nonconflict(index, ans):
            for i in range(len(ans)):
                # 当前棋子和前面几行处在一条直线上
                if index == int(ans[i]): return False
                # 当前棋子和前面几行处在一条斜线上
                if abs(int(ans[i]) - index) == len(ans) - i: return False
            return True

        # 回溯
        def backtrack(ans):
            if len(ans) == n:
                res.append(ans)
                return
            for i in range(n):
                if nonconflict(i, ans): backtrack(ans + str(i))       
        res = []
        backtrack('')

        # 打印
        for ans_i,ans in enumerate(res):
            tmp = [['.']*n for _ in range(n)]
            for i in range(n):
                tmp[i][int(ans[i])] = 'Q'
            res[ans_i] = [''.join(x) for x in tmp]
        return res
   
            
# @lc code=end

