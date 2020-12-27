#
# @lc app=leetcode.cn id=515 lang=python
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
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
            ans.append(max(tmp))
        return ans
# @lc code=end

