class Solution(object):
    """
    Simple, easy recursion
    """
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        prev = self.generate(numRows - 1)
        curr = [1]
        for i in range(1, len(prev[-1])):
            curr.append(prev[-1][i - 1] + prev[-1][i])
        curr.append(1)
        prev.append(curr)
        return prev


