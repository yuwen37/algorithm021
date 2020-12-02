#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 快慢指针
        slow = ListNode(-1)
        slow.next = fast = head
        while fast and fast.next:
            if fast == slow:return True
            fast = fast.next.next
            slow = slow.next
        return False
        
# @lc code=end

