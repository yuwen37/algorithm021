#
# @lc app=leetcode.cn id=212 lang=python
#
# [212] 单词搜索 II
#

# @lc code=start
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # dfs搜索
        def dfs(i,j,word,root):
            if '#' in root:
                ans.add(word)
            tmp = board[i][j] # 备份
            board[i][j] = 0 # 标记走过的路径
            for x,y in direction:
                x,y=x+i,y+j
                if 0 <= x < m and 0 <= y < n and board[x][y] in root:
                    dfs(x,y,word + board[x][y], root[board[x][y]])
            board[i][j] = tmp
        # 生成Trie
        root = {} 
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = '#'
        
        m,n = len(board), len(board[0])
        direction = ((1,0),(-1,0),(0,1),(0,-1))
        ans = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(i,j,board[i][j],root[board[i][j]])
        return list(ans)

# @lc code=end

