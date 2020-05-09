# 69 x的平方根（二分法）
"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


def mySqrt(x: int) -> int:
    left = 0
    right = x // 2 + 1
    while left < right:
        # take right-mid as the final int ans <= float ans
        mid = left + (right - left) // 2 + 1
        if mid * mid == x:
            return mid
        # right definitely not in the range, is not ans
        if mid * mid > x:
            right = mid - 1
        # left may be the ans
        else:
            left = mid
    return left
