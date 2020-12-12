#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # # 迭代
        # if not root:return []
        # stack = [root]
        # ans = []
        # while stack:
        #     root = stack.pop()
        #     if isinstance(root, int):
        #         ans.append(root)
        #     elif root:
        #         stack.append(root.right)
        #         stack.append(root.left)
        #         stack.append(root.val)
        # return ans

        # 递归
        ans = []
        def dfs(root):
            if not root:return
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans
 
# @lc code=end

