#
# @lc app=leetcode.cn id=264 lang=python
#
# [264] 丑数 II
#

# @lc code=start
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:return 1
        isexsit = {1}
        hp = [1]
        ans = []
        for _ in range(1690):
            cur = heappop(hp)
            ans.append(cur)
            for i in [2, 3, 5]:
                new = i * cur
                if new not in isexsit:
                    heappush(hp, new)
                    isexsit.add(new)
        return ans[n - 1]
        
# @lc code=end

