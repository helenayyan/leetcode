from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        if not nums:
            return res

        nums.sort()
        num_dict = dict.fromkeys(nums)
        num_list = list(num_dict)

        for num in num_list:
            num_dict[num] = nums.count(num)

        num_tup = [(k, v) for k, v in num_dict.items()]
        num_tup.sort(key=lambda tup: tup[1])
        num_tup = num_tup[::-1]
        for i in range(k):
            res.append(num_tup[i][0])

        return res
