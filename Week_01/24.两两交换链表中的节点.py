#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 迭代
        dummyHead = ListNode(0)
        dummyHead.next = head
        tmp = dummyHead
        while tmp.next and tmp.next.next:
            pre = tmp.next
            cur = tmp.next.next
            tmp.next = cur
            pre.next = cur.next
            cur.next = pre
            tmp = pre
        return dummyHead.next

        # # 递归
        # if not head or not head.next:return head

        # tmp = head.next
        # head.next = self.swapPairs(head.next.next)
        # tmp.next = head
        # return tmp
        
# @lc code=end

