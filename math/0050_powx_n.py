"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

说明:
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
"""


def myPow(x: float, n: int) -> float:
    # zero to the power of any number is zero
    if x == 0.0:
        return 0.0

    res = 1.0
    # convert minus problems to same method
    if n < 0:
        x = 1 / x
        n = -n

    while n:
        if n % 2 == 1:
            res *= x
        x *= x
        n >>= 1
    return res
