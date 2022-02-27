# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [float('-inf')]
        self.helper(root, ans)
        return ans[0]

    """
    Post-order traversal
    At each node, update the maximum of the seen path so far. 
    When returning, only return the maximum of those that contains root node.
    This is because the path needs to be connected. 
    
    Since we already update the maximum so far in "ans", it's okay to only return the paths that contain the root node. 
    """
    def helper(self, root, ans):
        if not root:
            return float('-inf')

        # Recurse through the left and right
        leftPathSum = self.helper(root.left, ans)
        rightPathSum = self.helper(root.right, ans)

        # Update the maximum sum that has been traversed so far
        ans[0] = max(ans[0], root.val, leftPathSum, rightPathSum,
                     root.val + leftPathSum, root.val + rightPathSum,
                     root.val + leftPathSum + rightPathSum)

        # When returning the value, that path must contain the root nodes since path needs to be connected.
        return max(root.val, root.val + leftPathSum, root.val + rightPathSum)