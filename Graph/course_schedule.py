from collections import defaultdict


class Solution(object):
    """
    Graph Traversal.
    Keep track of two data structures.
    One is hashset visited: keep track of all visited nodes
    Another important data structure is stack curStack that keep tracks of the vertices that has been visited
    in the current dfs.

    While traversing with dfs, if the neighbor node is in curStack, then return False
    """
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # build graph
        g = defaultdict(list)

        for i in range(numCourses):
            g[i] = []

        for item in prerequisites:
            g[item[1]].append(item[0])

        # detect cycle
        visited = set()
        curStack = []

        for node in g:
            if not self.dfs(node, g, visited, curStack):
                return False
        return True

    """
    dfs traverse through each node. In each dfs, if the neighboring node is already in curStack, return false
    """
    def dfs(self, node, g, visited, curStack):
        # If the node is already in the current stack, then return false
        if node in curStack:
            return False

        if node not in visited:
            visited.add(node) # similar to other dfs
            curStack.append(node) # this is what makes this question different.

            for neighbor in g[node]:
                if not self.dfs(neighbor, g, visited, curStack): # recursively check if the condition satisfied.
                    return False

            curStack.pop()
        return True