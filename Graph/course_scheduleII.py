from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        self.st = []
        g = defaultdict(list)
        visited = set() # keep track of visited nodes. Ensure no duplicate visiting.
        curStack = [] # keep track of the current dfs. Use for cycle detection

        # Build graph
        for i in range(numCourses):
            g[i] = []

        # Build adjacency list
        for item in prerequisites:
            g[item[1]].append(item[0])

        # Return an empty list if cycle is detected
        # else, store the list of courses in the self.st
        for course in g:
            if not self.dfs(course, g, visited, curStack):
                return []
        return self.st[::-1] # Return the revere of the stack.

    # Return boolean. If cycle is detected, return False. Else, return True
    # Append the node after all neighboring nodes are visited.
    # When base case (node with all the neighbor nodes are visited) are reached, append it to the self.st
    def dfs(self, node, g, visited, curStack):
        # Detect cycle
        if node in curStack:
            return False

        if node not in visited:
            visited.add(node)
            curStack.append(node)

            for neighbor in g[node]:
                if not self.dfs(neighbor, g, visited, curStack):
                    return False
            self.st.append(node) # Append the node when all the neighboring nodes are visited.
            curStack.pop()
        return True
