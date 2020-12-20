#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 分治
        def valid(root, low, up):
            if not root: return True
            if root.val >= up or root.val <= low: return False
            if not valid(root.left, low, root.val): return False
            if not valid(root.right, root.val, up): return False
            return True
        return valid(root, float('-inf'), float('inf'))
# @lc code=end

