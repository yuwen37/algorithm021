#
# @lc app=leetcode.cn id=433 lang=python
#
# [433] 最小基因变化
#

# @lc code=start
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # 双向BFS
        bank = set(bank)
        if end not in bank: return -1
        front = {start}
        back = {end}
        n = len(start)
        step = 0
        while front:
            step += 1
            front_next = set()
            for word in front:
                for i in range(n):
                    for j in 'AGCT':
                        neww = word[:i] + j + word[i + 1:]
                        if neww in back:
                            return step
                        if neww in bank:
                            front_next.add(neww)
                            bank.remove(neww)
            front = front_next
            if len(front) > len(back):
                front,back = back,front 
        return -1

        # 单向BFS
        # possible = ['A', 'G', 'C', 'T']
        # bank = set(bank)
        # deq = deque([(start, 0)])
        # exist = set([start])
        # while deq:
        #     word, step = deq.popleft()
        #     if word == end: return step
        #     for i in range(len(start)):
        #         for p in possible:
        #             tmp = word[:i] + p + word[i + 1:]
        #             if tmp in bank and tmp not in exist:
        #                 exist.add(tmp)
        #                 deq.append((tmp, step + 1))
        # return -1
                
# @lc code=end

