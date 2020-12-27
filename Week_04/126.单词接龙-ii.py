#
# @lc app=leetcode.cn id=126 lang=python
#
# [126] 单词接龙 II
#

# @lc code=start
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        deq = deque([beginWord])
        visited = set([beginWord]) # 记录本层和之前层出现过的单词
        # 生成图
        graph = defaultdict(set)
        while deq:
            next_visited = set() # 记录下一层出现的单词
            for _ in range(len(deq)):
                word = deq.popleft()
                for i in range(len(beginWord)):
                    for p in range(26):
                        tmp = word[:i] + chr(97 + p) + word[i + 1:]
                        if tmp in wordList and tmp not in visited:
                            graph[word].add(tmp)
                            if tmp not in next_visited:
                                next_visited.add(tmp)
                                deq.append(tmp) # 在这里只需要加一遍
            visited = visited | next_visited

        # DFS调用所有路径
        ans = []
        def dfs(tmp, route):
            if tmp == endWord:
                ans.append(route)
                return
            for word in graph[tmp]:
                dfs(word, route + [word])
        dfs(beginWord, [beginWord])
        return ans
# @lc code=end

