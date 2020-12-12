#
# @lc app=leetcode.cn id=429 lang=python
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        # 递归
        ans = []
        def dfs(root, index):
            if not root:return
            if len(ans) <= index:
                ans.append([])
            ans[index].append(root.val)
            for child in root.children:
                dfs(child, index + 1)
        dfs(root, 0)
        return ans

        # 迭代
        # import collections
        if not root:return []
        ans = []
        deq = deque([root])
        while deq:
            tmp = []
            for _ in range(len(deq)):
                root = deq.popleft()
                if root:
                    tmp.append(root.val)
                    deq.extend(root.children)
            ans.append(tmp)
        return list(ans)
                      
# @lc code=end

