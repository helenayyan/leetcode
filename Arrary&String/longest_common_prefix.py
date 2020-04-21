# 14 最长公共前缀
def longestCommonPrefix(s: [str]) -> str:
    """
    编写一个函数来查找字符串数组中的最长公共前缀。

    如果不存在公共前缀，返回空字符串 ""。

    实现方法：
    zip() 合并项
    set() remove duplicated
    """
    res = ''
    list_s = list(zip(*s))
    for i in list_s:
        if len(set(i)) == 1:
            res += i[0]
        else:
            break
    return res
