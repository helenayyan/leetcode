"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        mid = n // 2
        for l in range(mid + 1, -1, -1):
            if n - l >= l:
                left_part = s[:l]
                right_part = s[l:]
                rerightpart = right_part[::-1]
                if n - 2 * l > 0 and rerightpart[n - 2 * l - 1:n - l - 1] == left_part:
                    return rerightpart[:n - l - 1] + right_part
                elif rerightpart[n - 2 * l:] == left_part:
                    return rerightpart + right_part
