#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # dp[i] 以第i个数字的最长递增子序列
        # n = len(nums)
        # dp = [1] * n
        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        # # 二分查找（使用库函数）
        # dp = []
        # for num in nums:
        #     pos = bisect.bisect_left(dp, num)
        #     if pos == len(dp):
        #         dp.append(num)
        #     else:
        #         dp[pos] = num
        # return len(dp)

        # 二分查找(基于上述库函数思路)
        dp = [float('-inf')]
        for num in nums:
            left = 0
            right = len(dp)
            while left < right:
                mid = (left+right)>>1
                if dp[mid] >= num:
                    right = mid
                else:
                    left = mid + 1
            if right == len(dp):
                dp.append(num)
            else:
                dp[right] = num
        return len(dp) - 1
            
# @lc code=end

