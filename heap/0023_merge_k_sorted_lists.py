# Definition for singly-linked list.
from heapq import heappush, heappop
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummyhead = ListNode()
        curr = dummyhead
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        while heap:
            val, i = heappop(heap)

            curr.next = ListNode(val)
            curr = curr.next

            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        return dummyhead.next
