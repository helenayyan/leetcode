class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0

        sum_up = 0
        ans = nums[0]
        for n, item in enumerate(nums):
            if sum_up < 0:
                sum_up = item
            else:
                sum_up += item
            ans = max(ans, sum_up)
        return ans
