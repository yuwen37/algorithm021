#
# @lc app=leetcode.cn id=621 lang=python
#
# [621] 任务调度器
#

# @lc code=start
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # 这似乎和动态规划没什么关系？
        cnt = Counter(tasks)
        max_cnt = max(cnt.values())
        ans = (max_cnt - 1) * (n + 1)
        for i in cnt.values():
            if i == max_cnt: ans += 1
        return max(ans, len(tasks))
# @lc code=end

