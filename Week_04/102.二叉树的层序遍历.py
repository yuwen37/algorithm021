#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS
        if not root: return []
        deq = deque([root])
        ans = []
        while deq:
            tmp = []
            for _ in range(len(deq)):
                node = deq.popleft()
                tmp.append(node.val)
                if node.left: deq.append(node.left)
                if node.right: deq.append(node.right)
            ans.append(tmp)
        return ans

        # DFS
        def dfs(root, index):
            if len(ans) - 1 < index:
                ans.append([])
            ans[index].append(root.val)
            if root.left: dfs(root.left, index + 1)
            if root.right: dfs(root.right, index + 1)     
        if not root: return []
        ans = []
        dfs(root, 0)
        return ans
# @lc code=end

