from collections import defaultdict


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = defaultdict()
        memo[0] = 0

        self.helper(coins, amount, memo)
        return memo[amount]

    def helper(self, coins, amount, memo):
        if memo.get(amount):
            return memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        for coin in coins:
            prev_count = self.helper(coins, amount - coin, memo)
            if prev_count >= 0:
                count = prev_count + 1
                if not memo.get(amount):
                    memo[amount] = count
                else:
                    memo[amount] = min(memo[amount], count)

        if not memo.get(amount):
            memo[amount] = -1
        return memo[amount]

    def coinChangeTabulation(self, amount, coins):
        memo = [amount + 1 for i in range(amount + 1)]
        memo[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i -c >= 0:
                    memo[i] = min(memo[i], memo[i - c] + 1)

        if memo[amount] == amount + 1:
            return -1
        return memo[amount]