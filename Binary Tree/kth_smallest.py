# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    """
    Cautious on making k global.
    To update k, need to intiialize as self variable.
    Also since the value can be returned internally, stored as self.res
    """
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        self.helper(root,k)
        return self.res

    def helper(self, root,k):
        if not root:
            return
        self.helper(root.left,k)
        self.k -=1
        if self.k == 0:
            self.res = root.val
            return
        self.helper(root.right,k)
