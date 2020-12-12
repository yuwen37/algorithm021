#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node'):
        # 递归
        ans = []
        def dfs(root):
            if not root:return
            for child in root.children:
                dfs(child)
            ans.append(root.val)
        dfs(root)
        return ans

        # # 迭代1
        # if not root:return []
        # ans = []
        # stack = [root]
        # while stack:
        #     root = stack.pop()
        #     if isinstance(root, int):
        #         ans.append(root)
        #     elif root:
        #         stack.append(root.val)
        #         stack.extend(root.children[::-1])
        # return ans

        # # 迭代2
        # if not root:return []
        # ans = []
        # stack = [root]
        # while stack:
        #     root = stack.pop()
        #     if root:
        #         ans.append(root.val)
        #         stack.extend(root.children)
        # return ans[::-1]
# @lc code=end

