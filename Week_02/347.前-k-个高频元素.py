#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 小根堆可以得出前k个最大的数字
        count = Counter(nums)
        count_value = count.values()
        hp = count_value[:k]
        heapq.heapify(hp)
        for i in count_value[k:]:
            if i > hp[0]:
                heappop(hp)
                heappush(hp, i)
        ans = []
        for key, value in count.items():
            if value >= hp[0]:
                ans.append(key)
        return ans

# @lc code=end

