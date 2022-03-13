class Solution(object):
    """
    Efficient solutions with O(m*n)
    Reverse thinking: Starts from the board with "O" traverse and converts every connected "O" to T.
    Then, iterate the board and convert "O" to "X" since the remaining "O" are now surrounded
    Finally, revert all "T" (i.e. unsurrounded regions) back to "O"
    """
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i == ROWS or j == COLS or board[i][j] != "O":
                return
            else:
                board[i][j] = "T"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i in [0, ROWS - 1] or j in [0, COLS - 1]):
                    dfs(i, j)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"

            for i in range(ROWS):
                for j in range(COLS):
                    if board[i][j] == "T":
                        board[i][j] = "O"

    """
    Inefficient solutions with duplicate dfs.
    Time exceeded but answers are correct.
    """
    def solve2(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        visited = set()
        memo = set()

        def dfs(i, j):
            # base case
            # 1) If board[i][j] == "X": do nothing, return False
            # 2) If board[i][j] == "O": if O in the boader, not capture, if True
            #                           if O not in the board, traverse
            # keep track of visited nodes
            if board[i][j] == "X" or i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or (i, j) in visited:
                return False

            visited.add((i, j))
            # check if it's in the boarder
            if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1 or (i, j) in memo:
                visited.remove((i, j))
                return True
            else:
                if dfs(i + 1, j) or dfs(i - 1, j) or dfs(i, j + 1) or dfs(i, j - 1):
                    memo.add((i, j))
                    visited.remove((i, j))
                    return True
                else:
                    visited.remove((i, j))
                    return False

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if not dfs(i, j):
                    # You need to change after all the dfs is done to modify one cell.
                    # memoization didn't help a lot
                    board[i][j] = "X"

input = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
output = Solution().solve(input)
print(output)