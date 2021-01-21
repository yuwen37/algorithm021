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

        # 方法一：位运算
        def dfs(i,j,pie,na,queen):
            if i == n:
                ans.append(queen)
                return
            bit = (~(j|pie|na)&((1<<n)-1))
            # ~(j|pie|na)找到所有空位，空位为1，
            # x&((1<<n)-1) 可以把x的n位以上的数字归零
            while bit:
                p = bit & -bit # 取最小位1
                bit &= (bit-1) # 打掉最小位1    
                dfs(i+1,j|p,(pie|p)<<1,(na|p)>>1,queen+[int(math.log(p, 2))])    
        if n < 1:return []
        ans = []
        dfs(0,0,0,0,[])
        return [["."*i + "Q" + "."*(n-i-1) for i in res] for res in ans]

        # # 方法二：最简单的方法
        # def dfs(queen, pie, na):
        #     row = len(queen)
        #     if row == n:
        #         ans.append(queen)
        #         return
        #     for col in range(n):
        #         if col not in queen and row+col not in pie and row-col not in na:
        #             dfs(queen + [col], pie + [row+col], na + [row-col])
        # ans = []
        # dfs([],[],[])
        # return [['.'*i+'Q'+'.'*(n-i-1) for i in res] for res in ans]

        # 方法一：最基础的方法
        # # 判断是否冲突
        # def nonconflict(index, ans):
        #     for i in range(len(ans)):
        #         # 当前棋子和前面几行处在一条直线上
        #         if index == int(ans[i]): return False
        #         # 当前棋子和前面几行处在一条斜线上
        #         if abs(int(ans[i]) - index) == len(ans) - i: return False
        #     return True

        # # 回溯
        # def backtrack(ans):
        #     if len(ans) == n:
        #         res.append(ans)
        #         return
        #     for i in range(n):
        #         if nonconflict(i, ans): backtrack(ans + str(i))       
        # res = []
        # backtrack('')

        # # 打印
        # for ans_i,ans in enumerate(res):
        #     tmp = [['.']*n for _ in range(n)]
        #     for i in range(n):
        #         tmp[i][int(ans[i])] = 'Q'
        #     res[ans_i] = [''.join(x) for x in tmp]
        # return res
   
            
# @lc code=end

