"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

"""
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        n = len(S)
        table = dict()  # key: character; value: last appear position

        for i, s in enumerate(S):
            if s in table:
                table[s] = max(table[s], i)
            else:
                table[s] = i

        res = []
        start, i, end = 0, 0, 0
        while start < n:
            end = table[S[start]]
            i = start
            # check the character within the initial [start, end]
            while i <= end:
                end = max(end, table[S[i]])
                i += 1

            res.append(end - start + 1)
            start = end + 1  # move start to the next interval

        return res
