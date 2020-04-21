# 88 合并两个有序数组
def merge(nums1: [int], m: int, nums2: [int], n: int) -> None:
    """
    Merge two list together in order
    给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。

    说明:
    初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

    输入:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3

    输出: [1,2,2,3,5,6]

    Do not return anything, modify nums1 in-place instead.
    """
    # set two pointers
    p1 = 0
    p2 = 0

    # get nums1's elements and make a copy, then empty nums1
    nums1_copy = nums1[:m]
    nums1[:] = []

    # start comparing elements in nums1 and nums2
    while p1 < m and p2 < n:
        if nums1_copy[p1] <= nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1

    # add in the left elements
    if p1 < m:
        nums1[p1 + p2:] = nums1_copy[p1:]
    if p2 < n:
        nums1[p1 + p2:] = nums2[p2:]
