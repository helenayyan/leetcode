import collections
from heapq import heapify, heappop
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapify(heap)
        while k > 0:
            res.append(heappop(heap)[1])
            k -= 1

        return res