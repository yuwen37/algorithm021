#
# @lc app=leetcode.cn id=493 lang=python
#
# [493] 翻转对
#

# @lc code=start
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def merge(nums,left,mid,right):
            i, j = left, mid+1
            while i <= mid and j <= right:
                if nums[i] > 2*nums[j]:
                    self.cnt += mid-i+1
                    j += 1
                else:
                    i += 1

            i, j = left, mid+1
            tmp=[]
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
            if i > mid:
                tmp += nums[j:right+1]
            else:
                tmp += nums[i:mid+1]
            nums[left:right+1] = tmp

        def merge_sort(nums,left,right):
            if left >= right:return
            mid = (left + right) >> 1
            merge_sort(nums, left, mid)
            merge_sort(nums, mid+1, right)
            merge(nums, left, mid, right)

        self.cnt = 0
        merge_sort(nums,0,len(nums)-1)
        return self.cnt
# @lc code=end

