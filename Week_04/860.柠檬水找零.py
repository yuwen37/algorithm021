#
# @lc app=leetcode.cn id=860 lang=python
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count = [0] * 2 # 记录收入5、10圆的数量
        for c in bills:
            if c == 5:
                count[0] += 1
            if c == 10:
                if count[0] == 0: return False
                count[0] -= 1
                count[1] += 1
            if c == 20:
                if count[1] > 0 and count[0] > 0:
                    count[1] -= 1
                    count[0] -= 1
                elif count[0] > 2:
                    count[0] -= 3
                else:
                    return False
        return True
# @lc code=end

