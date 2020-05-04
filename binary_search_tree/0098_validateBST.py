# 98 验证二叉搜索树
"""给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def ds(root, min_limit, max_limit):
            if not root:
                return True
            if root.val < min_limit or root.val > max_limit:
                return False
            return ds(root.left, min_limit, root.val) and ds(root.right, root.val, max_limit)

        return ds(root, float("-inf"), float("inf"))
