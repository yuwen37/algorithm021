#
# @lc app=leetcode.cn id=297 lang=python
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root: return '[]'
        ans = []
        deq = deque([root])
        while deq:
            node = deq.popleft()
            if node:
                ans.append(str(node.val))
                deq.extend([node.left, node.right])
            else:
                ans.append('null')
        # print(ans)
        return '[{}]'.format(','.join(ans))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return []
        data = data[1:-1].split(',')
        root = TreeNode(int(data[0]))
        deq = deque([root])
        i = 1
        while deq:
            node = deq.popleft()
            if data[i] != 'null':
                node.left = TreeNode(int(data[i]))
                deq.append(node.left)
            i += 1
            if data[i] != 'null':
                node.right = TreeNode(int(data[i]))
                deq.append(node.right)
            i += 1 
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

