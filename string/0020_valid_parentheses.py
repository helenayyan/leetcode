"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false

"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        if not s:
            return True
        for item in s:
            if item == '(':
                stack.append(item)
            elif item == ')':
                if not stack:
                    return False
                prev = stack.pop()
                if prev != '(':
                    return False
            elif item == '[':
                stack.append(item)
            elif item == ']':
                if not stack:
                    return False
                prev = stack.pop()
                if prev != '[':
                    return False
            elif item == '{':
                stack.append(item)
            elif item == '}':
                if not stack:
                    return False
                prev = stack.pop()
                if prev != '{':
                    return False
        if not stack:
            return True
        return False