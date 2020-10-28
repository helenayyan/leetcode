from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        alpha_plate = ""

        # string manipulation: pick out characters first
        for item in licensePlate:
            if item.isalpha():
                alpha_plate += item
        alpha_plate = alpha_plate.lower()

        def count_map(s):
            """create a dictionary key=character, value=count in s"""
            chars = dict()
            for char in s:
                if char in chars:
                    chars[char] += 1
                else:
                    chars[char] = 1
            return chars

        required = count_map(alpha_plate)
        res = []

        def match(dict_a, dict_b):
            """Check if the value in to dictionary matches"""
            for char, num in dict_a.items():
                if char not in dict_b or num > dict_b[char]:
                    return False
            return True

        for word in words:
            avail = count_map(word)
            if match(required, avail):
                res.append(word)

        # return the shortest completing word
        return min(res, key=len)
