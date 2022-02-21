class TreeNode:

    def __init__(self, val, left,right):
        self.val = val
        self.left = left
        self.right = right


class BST:

    def validate_bst(self, root):
        if not root:
            return True
        treeArr = self.inorderTraversal(root)

        for i in range(len(treeArr) -1):
            if treeArr[i] >= treeArr[i+1]:
                return False
        return True

    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def validate_bst_2(self, root, minval=float('-inf'), maxval=float('inf')):
        if not root:
            return True
        if root.val <= minval or root.val >= maxval:
            return False
        return self.validate_bst_2(root.left, minval, root.val) and self.validate_bst_2(root.right, root.val, maxval)
