from collections import defaultdict
import heapq

class Solution(object):

    # First solution: Bellman Ford
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        cost = [float('inf')] * n
        cost[k - 1] = 0

        for i in range(n - 1):
            temp = cost[:]

            for s, d, t in times:
                if cost[s - 1] == float('inf'):
                    continue
                else:
                    temp[d - 1] = min(temp[d - 1], cost[s - 1] + t)
            cost = temp

        maxTime = max(cost)

        if maxTime == float('inf'):
            return -1
        else:
            return maxTime

    # BFS using mean heap.
    def networkDelayTime_Dij(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        visited = set()

        g = defaultdict()
        for i in range(1, n + 1):
            g[i] = []

        for s, d, t in times:
            g[s].append((t, d))

        hp = [(0, k)]
        ans = 0
        while len(hp) > 0 and len(visited) != n:
            cost, node = heapq.heappop(hp)
            if node not in visited:
                visited.add(node)
                ans = max(ans, cost)
                for c, neighbor in g[node]:
                    heapq.heappush(hp, (cost + c, neighbor))

        if len(visited) != n:
            return -1
        else:
            return ans



