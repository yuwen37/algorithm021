#
# @lc app=leetcode.cn id=874 lang=python
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # 记录当前方向
        di = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        # 变为集合，方便查找
        obstacles = set(map(tuple, obstacles))
        ans = 0
        x = y = 0
        for cmd in commands:
            if cmd == -2:
                di = (di - 1) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacles:
                        x += dx[di]
                        y += dy[di]
            ans = max(ans, x**2 + y**2)
        return ans
# @lc code=end

