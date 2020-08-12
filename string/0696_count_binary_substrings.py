"""
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # math method: count nums of continuous 0/1 and add up
        if len(s) == 1:
            return 0

        count = 1
        nums = []
        num_start = s[0]
        for i, num in enumerate(s[1:]):
            if num_start == num:
                count += 1
            else:
                nums.append(count)
                num_start = num
                count = 1

        nums.append(count)  # don't forget last set of numbers

        result = 0
        for i, item in enumerate(nums[:-1]):
            result += min(item, nums[i + 1])

        return result
