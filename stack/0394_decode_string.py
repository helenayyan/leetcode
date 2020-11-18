"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

"""


class Solution:
    def decodeString(self, s: str) -> str:
        count = 0
        stack = []
        res = ''

        for item in s:
            if item == '[':
                stack.append([count, res])
                res = ''
                count = 0
            elif item == ']':
                add = stack.pop()
                res = add[1] + res * add[0]
                print(res)
            elif '0' <= item <= '9':
                count = count * 10 + int(item)
            else:
                res = res + item
        return res
