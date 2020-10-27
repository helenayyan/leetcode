"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = head  # store the head node

        while head and head.next:
            pre, cur = head, head.next
            pre.val, cur.val = cur.val, pre.val  # swap value of the pair
            head, head.next = pre, cur  # assign the value back
            head = cur.next  # move to the next pair

        return dummy
