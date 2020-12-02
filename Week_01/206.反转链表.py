#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代法
        pre = None
        cur = head
        while cur:
            # tmp = cur.next
            # cur.next = pre
            # pre = cur
            # cur = tmp
            cur.next,pre,cur = pre,cur,cur.next
        return pre

        # # 递归法(有点难理解)
        # if not head or not head.next:
        #     return head
        # cur = self.reverseList(head.next) # 这里返回的是反序的链表, cur指向表头
        # head.next.next = head
        # head.next = None
        # return cur

# @lc code=end

