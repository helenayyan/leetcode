"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        fast-slow pointer with reversed linked list
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # exclude length smaller than 2
        if not head or not head.next:
            return True

        # fast-slow pointers to find the two symmetric side of a list
        slow, fast = head, head.next
        while True:
            if not (fast and fast.next):
                break
            else:
                fast = fast.next.next
                slow = slow.next

        fast = head  # reset fast back to the start of left side
        slow = slow.next  # slow pointing to the end of right side

        # reversed linked list on the right side to make slow also pinting at the start
        pre = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        slow = pre

        # directly compare if the two sides have the same values
        while slow:
            if fast.val != slow.val:
                return False
            else:
                fast, slow = fast.next, slow.next

        return True
