"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    rev = head  # start point of reverse part
    start = None  # store the list before the reverse part
    rev_length = n - m
    if m == n:
        return head

    for _ in range(m - 1):
        start = rev
        rev = rev.next

    rev_tail = rev  # store the tail of reverse part after reverse

    # reverse: the reversed part
    # tail: the head of part following the reversed part
    reverse, tail = reverseList(rev, rev_length)
    rev_tail.next = tail

    # added up three part
    if start:
        start.next = reverse
    else:
        head = reverse

    return head


def reverseList(head: ListNode, length: int):
    pre = None
    curr = head
    count = 0
    while count <= length:
        tmp = curr.next
        curr.next = pre
        pre = curr
        curr = tmp
        count += 1
    return pre, curr
