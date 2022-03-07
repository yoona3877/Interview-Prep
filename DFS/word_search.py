class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        # keep track of the visited nodes
        visited = set()
        row, col = len(board), len(board[0])

        # iterate over all elements in the board
        for i in xrange(row):
            for j in xrange(col):
                if self.dfs(board, word, visited, i, j):
                    return True
        return False

    def dfs(self, board, word, visited, i, j):
        if word == "":
            return True
        if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or (i, j) in visited or word[0] != board[i][j]:
            return False
        visited.add((i, j)) # add visited node
        one = self.dfs(board, word[1:], visited, i + 1, j)
        two = self.dfs(board, word[1:], visited, i - 1, j)
        three = self.dfs(board, word[1:], visited, i, j + 1)
        four = self.dfs(board, word[1:], visited, i, j - 1)
        visited.remove((i, j)) # at the end of the search, must remove the node from the visited.
        return one or two or three or four



