from collections import defaultdict


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        if src == dst:
            return 0

        # Initialize to infinite cost and set the source cost to 0
        prices = [float('inf')] * n
        prices[src] = 0

        # Bellman Ford algorithm
        # BFS. For V - 1 iterations, iterate through all the edges.
        for i in range(k + 1):
            temp = prices[:]

            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                else:
                    temp[d] = min(temp[d], p + prices[s])
            prices = temp

        if prices[dst] == float('inf'):
            return -1
        else:
            return prices[dst]

