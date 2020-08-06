"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []

        def isPalindrome(s: str, left: int, right: int) -> bool:
            # if the string is palindrome
            return s[left:right + 1] == s[left:right + 1][::-1]

        # store the palindrome string into a hash table for search later
        hash_table = {}
        for i, word in enumerate(words):
            hash_table[word[::-1]] = i

        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                # also need to take empty string as a palindrome

                # 前缀
                if isPalindrome(word, j, m - 1):
                    left_id = hash_table.get(word[0:j], -1)
                    if left_id != -1 and left_id != i:
                        # existed and not itself
                        result.append([i, left_id])

                # 后缀
                if j and isPalindrome(word, 0, j - 1):
                    right_id = hash_table.get(word[j:m], -1)
                    if right_id != -1 and right_id != i:
                        result.append([right_id, i])

        return result
