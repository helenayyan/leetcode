"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4

Example 2:

Input: [0,1]
Output: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0 and n == 0:
            return 0

        count = 0

        while m < n:
            m = m >> 1
            n = n >> 1
            count += 1

        return m << count
