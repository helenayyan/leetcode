"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def helper(i, j):
            nonlocal res
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                res += 1

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return res
