"""
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

 

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation:
The first missing number is 5.

"""
from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missings = []
        n = len(nums)
        if n == 1:
            return nums[0] + k

        for i, num in enumerate(nums[:-1]):
            between = nums[i + 1] - num - 1
            if between >= k:
                return num + k
            else:
                k -= between

        return nums[-1] + k
