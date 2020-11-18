"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

"""

from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return False

        downwards = False
        i = 1
        while i < n:
            if not downwards:
                if (A[i] <= A[i - 1] and i == 1) or A[i] == A[i - 1]:
                    return False
                elif A[i] < A[i - 1]:
                    downwards = True
            else:
                if A[i] >= A[i - 1]:
                    return False
            i += 1

        return downwards
