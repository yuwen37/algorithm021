#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        ans = []
        def dfs(root):
            if root:
                dfs(root.left)
                ans.append(root.val)
                dfs(root.right)
        dfs(root)
        return ans
        
# @lc code=end

