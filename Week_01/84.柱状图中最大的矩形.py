#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # # 官方解
        # n = len(heights)
        # stack = [] # 存放柱的下标
        # left = [0] * n # 每根柱子的左边界
        # right = [n] * n # 每根柱子的右边界

        # for i in range(n):
        #     while stack and heights[stack[-1]] > heights[i]:
        #         right[stack[-1]] = i # 找到了stack[-1]的柱字的右边界
        #         stack.pop()
        #     left[i] = stack[-1] if stack else -1 # 找到左边界
        #     stack.append(i)
        
        # ans = 0
        # for i in range(n):
        #     ans = max(ans, (right[i] - left[i] - 1) * heights[i])
        # return ans

        # 另一种解
        heights = [0] + heights + [0] # 这一步处理的很妙,甚至有点觉得似懂非懂
        n = len(heights)
        stack = []
        ans = 0

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                # 这里计算的是i前面的那个柱子的面积
                ans = max(ans, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return ans


# @lc code=end

