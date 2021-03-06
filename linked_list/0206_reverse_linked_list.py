"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head: ListNode) -> ListNode:
    pre = None
    curr = head
    while curr:
        tmp = curr.next
        curr.next = pre
        pre = curr
        curr = tmp
    return pre
