
class TreeNode:

    def __init__(self, val, left,right):
        self.val = val
        self.left = left
        self.right = right

class Treversal:

    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def inorder_iter(self, root):
        if not root:
            return []

        curr, ans, st = root, [], []

        while (curr is not None) or (len(st) > 0):
            while curr is not None:
                st.append(curr)
                curr = curr.left

            temp = st.pop()
            ans.append(temp.val)
            curr = temp.right

        return ans

    def postorder(self, root):
        if not root:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
