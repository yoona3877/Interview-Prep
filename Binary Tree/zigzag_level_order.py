# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    Return a zigzag level-order traversal of a binary tree.
    Zigzag means left to right in the odd height, and right to left in the even height

    This problem is very similar to regular level order traversal.
    The only difference comes from a boolean, which keeps track of whether to add elements left to right or right to left.

    """
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        ans = []
        if not root:
            return ans

        # Similar to regular level order, keep track of a stack.
        q = [[root]]

        # zig True means traverse left to right. Otherwise, traverse right to left
        zig = True
        while len(q) > 0:
            nodes = q.pop()
            if zig:
                ans.append([node.val for node in nodes])
            else:
                ans.append([node.val for node in nodes][::-1])
            temp = []
            for node in nodes:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            # need to check whether temp is empty or not. If empty, must not add it to the stack
            # Otherwise, it's recursion error.
            if len(temp) > 0:
                q.append(temp)

            # reverse to another zigzag position.
            zig = not zig
        return ans

