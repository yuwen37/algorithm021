#
# @lc app=leetcode.cn id=127 lang=python
#
# [127] 单词接龙
#

# @lc code=start
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # 双向BFS
        wordList = set(wordList)
        if endWord not in wordList: return 0
        front = {beginWord}
        back = {endWord}
        n = len(beginWord)
        step = 1
        while front:
            step += 1
            front_next = set()
            for word in front:
                for i in range(n):
                    for j in range(26):
                        neww = word[:i] + chr(97 + j) + word[i + 1:]
                        if neww in back:
                            return step
                        if neww in wordList:
                            front_next.add(neww)
                            wordList.remove(neww)
            front = front_next
            if len(front) > len(back):
                front,back = back,front
        return 0

        # 单向BFS
        # wordList = set(wordList)
        # deq = deque([(beginWord, 1)])
        # exist = set([beginWord])
        # while deq:
        #     word, step = deq.popleft()
        #     if word == endWord: return step
        #     for i in range(len(beginWord)):
        #         for p in range(26):
        #             tmp = word[:i] + chr(97 + p) + word[i + 1:]
        #             if tmp in wordList and tmp not in exist:
        #                 # 这里是和接龙2本质区别的地方，这里的操作只能找到一条路径
        #                 exist.add(tmp)
        #                 deq.append((tmp, step + 1))
        # return 0
# @lc code=end

