class Solution(object):
    """
    Greedy solution
    """
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        # if sum of the gas cannot cover the sum of the cost, there is no solution.
        if sum(gas) < sum(cost):
            return -1

        # Now we guarantee that there is a solution
        total = 0
        res = 0

        # There exists only one solution.
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            # when total dips below 0, then start with a new index
            if total < 0:
                total = 0
                res = i + 1

        return res


    """
    Inefficient O(n^2) solutions
    """
    def canCompleteCircuit2(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        N = len(gas)
        for i in range(N):
            remaining = 0
            temp_gas = gas[i:] + gas[:i]
            temp_cost = cost[i:] + cost[:i]
            can_travel = True
            for j in range(N):
                remaining = remaining + temp_gas[j] - temp_cost[j]
                if remaining < 0:
                    can_travel = False
                    break
            if can_travel:
                return i
        return -1