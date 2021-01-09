#
# @lc app=leetcode.cn id=410 lang=python
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # 这道题用动态规划超时
        # # 动态规划
        # n = len(nums)
        # # f[i][j] 表示将数组的前 i 个数分割为 j 段所能得到的最大连续子数组和的最小值。
        # f = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        # sub = [0]
        # for elem in nums:
        #     sub.append(sub[-1] + elem)
        # # print(sub) 
        # f[0][0] = 0
        # for i in range(1, n + 1):
        #     for j in range(1, min(i, m) + 1):
        #         for k in range(j - 1,i):
        #             f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
        # return f[n][m]

        # 二分法
        def split(mid):
        # 计算以mid为数组和上界，划分数组的个数
            cnt = 1 # 划分数组个数
            s = 0
            for num in nums:
                if s + num > mid:
                    s = num
                    cnt += 1
                else:
                    s += num
            return cnt
        # mid表示 m 个子数组各自和的最大值最小值
        left = max(nums)
        right = sum(nums)
        while left < right:
            # 这道题的关键是要找最小值，因此需要把right向left偏移，mid = left + (right - left) // 2
            # 可以与69题x的平方根对比，这道题是求平方数不超过x的最大数，需要让left向right便宜，mid = left + (right - left + 1) // 2
            # 这两道题竟然结合在了一起，值得思考
            mid = left + (right - left) // 2
            cnt = split(mid)
            # 如果cnt>m,说明mid太小了，划分的数组太少了
            if cnt > m:
                left = mid + 1
            else:
                right = mid
        return left
# @lc code=end

