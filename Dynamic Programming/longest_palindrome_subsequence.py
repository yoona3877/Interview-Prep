class Solution(object):
    """
    Dyniamic Programming that involved 2-D matrix.

    """
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        memo = [[0] * n for _ in range(n)]

        if len(s) < 2:
            return len(s)

        for i in range(n):
            memo[i][i] = 1

        for start in range(1, n):
            for left in range(n - start):
                right = left + start
                if s[left] == s[right]:
                    memo[left][right] = 2 + memo[left + 1][right -1]
                else:
                    memo[left][right] = max(memo[left+1][right], memo[left][right-1])
                right +=1

        return memo[0][-1]
