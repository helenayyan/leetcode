# 704 二分查找
"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，
如果目标值存在返回下标，否则返回 -1。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def search(nums: [int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        # take left-mid
        """重点：to avoid （left + right） overflow from the range of numbers"""
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        # move left or right pointers
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # double-check if target is in the list or not
    if nums[left] == target:
        return left
    else:
        return -1
