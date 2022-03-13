# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diameter = [0]
        self.helper(root, diameter)
        return diameter[0]

    def helper(self, root, diameter):
        if not root:
            return 0

        left_height = self.helper(root.left, diameter)
        right_height = self.helper(root.right, diameter)
        diameter[0] = max(diameter[0], left_height + right_height)

        # you need to only return the max depth between left tree and right tree.
        # This is because to include the parent node in the path, you only need to connect to either tree
        # not both.
        return max(left_height, right_height) + 1