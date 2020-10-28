"""
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

"""
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len)  # sort the words by length of word
        shorter = set()  # create a set to store the available shorter words
        shorter.add(words[0])

        # recursively search inside one word to check if the parts can be divided with words in shorter
        def is_concatenated(s):
            # end recursion condition
            if not s:
                return True

            i = 0  # dividing pointer
            while i < len(s):
                if s[0:i + 1] in shorter and is_concatenated(s[i + 1:]):
                    return True
                else:
                    i += 1
            return False

        res = []
        for word in words[1:]:
            if is_concatenated(word):
                res.append(word)
            shorter.add(word)

        return res
