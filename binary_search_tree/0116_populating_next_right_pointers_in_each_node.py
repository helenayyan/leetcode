"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def find_next(node):
            while node.next:
                if node.next.left:
                    return node.next.left
                if node.next.right:
                    return node.next.right
                node = node.next
            return

        if not root:
            return root

        if root.right and root.left:
            root.left.next = root.right
            root.right.next = find_next(root)

        elif root.right and not root.left:
            root.right.next = find_next(root)

        elif root.left and not root.right:
            root.left.next = find_next(root)

        root.right = self.connect(root.right)
        root.left = self.connect(root.left)

        return root
