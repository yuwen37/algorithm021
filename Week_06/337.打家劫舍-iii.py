#
# @lc app=leetcode.cn id=337 lang=python
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root: return 0, 0 # 偷和不偷的最大金额
            left = dfs(root.left)
            right = dfs(root.right)
            do = root.val + left[1] + right[1]
            undo = max(left) + max(right)
            return do, undo
        return max(dfs(root))
# @lc code=end

