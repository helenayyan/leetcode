"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""
import itertools
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        match_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        from itertools import product
        if not digits:
            return []
        return ["".join(char) for char in itertools.product(*(match_dict[digit] for digit in digits))]
