"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Nodene
        :rtype: Node
        """

        if not root:
            return root

        q = [[root]]

        while len(q) > 0:
            nodes = q.pop()
            temp = []
            for i in range(len(nodes)):
                # check if the node is not the last
                if i + 1 != len(nodes):
                    nodes[i].next = nodes[i + 1]
                    # we know that the tree is perfect. If the node has left child, it means it also has right.
                if nodes[i].left:
                    temp.append(nodes[i].left)
                    temp.append(nodes[i].right)

            if len(temp) > 0:
                q.append(temp)

        return root




