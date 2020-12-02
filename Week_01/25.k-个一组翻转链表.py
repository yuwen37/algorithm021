#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head ,tail):
        """
        这一段完全类似反转链表的代码，可以照抄逻辑
        """
        pre = None
        cur = head
        # 这里和反转链表少许不同
        # 结束条件是反转到该段链表的结束
        while pre != tail: 
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return tail, head

    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        pre = dummy
        pre.next = head

        while True:
            tail = pre # 前一段链表的结尾
            # 判断下面是否还有k个节点
            # 如果没有了，说明不需要反转了，直接返回整个链表
            # 如果还有，那么tail刚好走k步到了当前这段链表的结尾
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            
            nex = tail.next # 记录一下结尾的下一个节点，方面后面连接
            head, tail = self.reverse(head, tail) # 反转链表
            # 反转完成后开始连接链表
            pre.next = head
            tail.next = nex

            # 初始化下一个链表的初始值
            pre = tail
            head = nex
        return dummy.next
        
# @lc code=end

