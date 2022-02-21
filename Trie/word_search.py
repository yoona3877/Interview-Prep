class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution(object):

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        # Implement Trie and add words
        trie = Trie()
        for word in words:
            trie.addWord(word)

        path = set()
        ans = set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r, c) in path or board[r][
                c] not in node.children:
                return
            else:
                path.add((r, c))
                node = node.children[board[r][c]]
                word += board[r][c]

                if node.isWord:
                    ans.add(word)

                dfs(r + 1, c, node, word)
                dfs(r - 1, c, node, word)
                dfs(r, c + 1, node, word)
                dfs(r, c - 1, node, word)
                path.remove((r, c))

        for i, row in enumerate(board):
            for j, col in enumerate(board[0]):
                dfs(i, j, trie.root, "")
        return set(ans)


















