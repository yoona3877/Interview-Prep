# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.res = TreeNode(0)
        self.helper(root, p, q)
        return self.res

    def helper(self, root, p, q):
        if not root:
            return False
        leftFound = self.helper(root.left, p, q)
        rightFound = self.helper(root.right, p, q)
        midFound = root == p or root == q

        if (leftFound and rightFound) or (leftFound and midFound) or (rightFound and midFound):
            self.res = root

        return midFound or leftFound or rightFound

    def lowestCommonAncestor2(self, root, p, q):
        if not root:
            return
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor2(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor2(root.right, p, q)
        else:
            return root