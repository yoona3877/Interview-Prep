# Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
from collections import defaultdict


class Solution(object):
    """
    Preorder traversal, keep track of level and pos for each node
    After traversal, iterate level by level and find the level with the maximum width.
    """
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        self.widths = defaultdict(list)

        self.helper(root, 0, 0)

        ans = 1
        for h, v in self.widths.items():
            ans = max(v[-1] - v[0] + 1, ans)

        return ans

    def helper(self, root, level, pos):
        if not root:
            return

        self.widths[level].append(pos)

        self.helper(root.left, level + 1, 2 * pos + 1)
        self.helper(root.right, level + 1, 2 * pos + 2)
