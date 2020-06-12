"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：

nums = [-1, 0, 1, 2, -1, -4]，

Expect:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    size = len(nums)
    # special judgement
    if size < 3:
        return res

    for i, num in enumerate(nums[:-2]):
        if num > 0:
            break

        # delete duplicate cases
        if i > 0 and num == nums[i - 1]:
            continue

        left = i + 1
        right = size - 1
        # cannot be equal
        while left < right:
            add = num + nums[left] + nums[right]
            if add > 0:
                right -= 1
            elif add < 0:
                left += 1
            else:
                res.append([num, nums[left], nums[right]])
                # delete duplicate cases
                while left < right and nums[left + 1] == nums[left]:
                    left += 1
                while left < right and nums[right - 1] == nums[right]:
                    right -= 1
            left += 1
            right -= 1

    return res


if __name__ == '__main__':
    nums_eg = [-2, 0, 0, 2, 2]
    result = threeSum(nums_eg)
    assert result == [[-2, 0, 2]]
    print(result)
