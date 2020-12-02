#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tail = []
        # 满9进一
        while digits and digits[-1] == 9:
            digits.pop()
            tail.append(0)
        # 加上尾部的0
        if digits == []:
            return [1] + tail
        else:
            digits[-1] += 1
            return digits + tail
        
# @lc code=end

