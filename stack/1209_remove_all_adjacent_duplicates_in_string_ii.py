"""
Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
"""
from collections import deque


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()  # stack for the current queue
        counts = deque()  # number of tail objects
        for item in s:
            if not stack or stack[-1] != item:
                counts.append(1)
                stack.append(item)
            else:
                counts[-1] += 1
                stack.append(item)
                if counts[-1] == k:
                    for _ in range(k):
                        stack.pop()
                    counts.pop()

        return ''.join(stack)
