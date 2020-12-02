#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 双端队列
        deq = collections.deque() # 存放下标
        ans = []
        for i in range(len(nums)):
            # 当deq的第一个数字下标越界，则清除deq的第一个数
            if deq and deq[0] + k <= i:
                deq.popleft()
            # 当deq[-1]的数字小于当前i的数字，则直接去掉deq[-1]
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            # 清除掉所有不满足的数字后，就可以添加新的元素了
            # 注意：这里加入的是下标，而不是nums的元素
            deq.append(i)
            # 当i>k的时候就可以更新答案了
            if i >= k - 1:
                ans.append(nums[deq[0]])
        return ans
# @lc code=end

