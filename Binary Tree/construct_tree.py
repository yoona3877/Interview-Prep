class TreeNode:

    def __init__(self, val, left,right):
        self.val = val
        self.left = left
        self.right = right


class Construct:

    def construct_from_inorder_preorder(self, preorder, inorder):

        if len(inorder) == 0:
            return None

        rootIdx = inorder.index(preorder.pop())
        curr_node = TreeNode(inorder[rootIdx])
        curr_node.left = self.construct_from_inorder_preorder(preorder, inorder[:rootIdx])
        curr_node.right = self.construct_from_inorder_preorder(preorder, inorder[rootIdx+1:])

        return curr_node