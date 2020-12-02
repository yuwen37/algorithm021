#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummp = tmp = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1:
            tmp.next = l1
        else:
            tmp.next = l2
        return dummp.next


        
# @lc code=end

