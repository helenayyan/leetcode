"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

"""
class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        s = s.split(' ')[::]
        for item in s:
            item = item[::-1]
            result = result + item + " "
        return result[:-1]