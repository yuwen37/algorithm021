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
        wordList = set(wordList)
        deq = deque([(beginWord, 1)])
        exist = set([beginWord])
        while deq:
            word, step = deq.popleft()
            if word == endWord: return step
            for i in range(len(beginWord)):
                for p in range(26):
                    tmp = word[:i] + chr(97 + p) + word[i + 1:]
                    if tmp in wordList and tmp not in exist:
                        # 这里是和接龙2本质区别的地方，这里的操作只能找到一条路径
                        exist.add(tmp)
                        deq.append((tmp, step + 1))
        return 0
# @lc code=end

