"""
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/24-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        res = 24
        ADD, MULTIPLY, SUBTRACT, DIVIDE = 0, 1, 2, 3

        def dfs(nums: List[float]) -> bool:
            n = len(nums)

            if not nums:
                return False

            if n == 1:
                return abs(nums[0] - res) < 1e-6

            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = list()
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        for opt in range(4):
                            if opt < 2 and i > j:
                                continue
                            if opt == ADD:
                                newNums.append(x + y)
                            elif opt == MULTIPLY:
                                newNums.append(x * y)
                            elif opt == SUBTRACT:
                                newNums.append(x - y)
                            elif opt == DIVIDE:
                                if abs(y) < 1e-6:
                                    continue
                                newNums.append(x / y)
                            if dfs(newNums):
                                return True
                            newNums.pop()
            return False

        return dfs(nums)
