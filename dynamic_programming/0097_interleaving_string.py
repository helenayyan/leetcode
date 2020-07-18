"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/interleaving-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        # false when length does not add up
        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0 and (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]):
                    dp[i][j] = True
                if j > 0 and (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]):
                    dp[i][j] = True

        return dp[i][j]
