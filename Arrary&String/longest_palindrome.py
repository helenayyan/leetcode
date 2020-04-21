# 5 最长回文子串
def longestPalindrome(s: str) -> str:
    """
    给定一个字符串s，找到s中最长的回文子串。你可以假设s的最大长度为1000。

    示例
    1：
    输入: "babad"    输出: "bab"
    注意: "aba"也是一个有效答案。

    示例
    2：
    输入: "cbbd"  输出: "bb"

    方法：中心拓展法
    """

    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    n = len(s)
    if n <= 0:
        return ""
    start, end = 0, 0
    for count in range(0, n):
        palindrome1 = expand_around_center(s, count, count)
        palindrome2 = expand_around_center(s, count, count + 1)
        palindrome = max(palindrome1, palindrome2)
        if palindrome > end - start:
            start = count - (palindrome - 1) // 2
            end = count + palindrome // 2
    print(start, end)
    s = s[start:end + 1]
    return s
