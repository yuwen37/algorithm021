#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        # # 迭代1
        # if not root:return []
        # ans = []
        # stack = [root]
        # while stack:
        #     root = stack.pop()
        #     if isinstance(root, int):
        #         ans.append(root)
        #     elif root:
        #         stack.extend(root.children[::-1])
        #         stack.append(root.val)
        # return ans
        # # 迭代2
        # if not root:return []
        # ans = []
        # stack = [root]
        # while stack:
        #     root = stack.pop()
        #     if root:
        #         ans.append(root.val)
        #         stack.extend(root.children[::-1])
        # return ans

        # 递归
        ans = []
        def dfs(root):
            if not root:return
            ans.append(root.val)
            for child in root.children:
                dfs(child)
        dfs(root)
        return ans

# @lc code=end

