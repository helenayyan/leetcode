from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False

        def neighbor(i, j):
            q = []
            if i - 1 >= 0:
                q.append((i - 1, j))
            if i + 1 < m:
                q.append((i + 1, j))
            if j - 1 >= 0:
                q.append((i, j - 1))
            if j + 1 < n:
                q.append((i, j + 1))
            return q

        def search(i, j, word, index):
            if index == len(word):  # 递归结束条件
                return True
            for loc in neighbor(i, j):
                l = loc[0]
                k = loc[1]
                if (l, k) not in used and board[l][k] == word[index]:
                    used.append((l, k))  # 已走过位置加入状态集
                    if search(l, k, word, index + 1):
                        return True  # 剪枝，从此一路返回，后面所有的节点都不在搜寻
                    used.remove((l, k))  # 如果没有执行上一行，代表没有发生剪枝，也就是当前节点的所有下一步节点均不满足，那么这条分支也就自然不满足，
                    # 去除该节点，以后的分支可能会继续使用
            return False  # 代表搜寻完所有可能分支均没有找到满足条件

        m = len(board)
        n = len(board[0])
        used = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    used.append((i, j))
                    flag = search(i, j, word, 1)
                    if flag: return True
                    used.remove((i, j))
        return False
