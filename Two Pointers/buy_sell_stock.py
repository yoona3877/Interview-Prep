class Solution(object):
    """
    Two pointers

    if prices in the right pointer is greater or equal to the prices of the left pointer, update max and increment r
    if prices in the left pointer if bigger, than increment l
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        ans = 0
        if len(prices) < 2:
            return ans
        l, r = 0, 0

        while r < len(prices):
            # if r == l, then the prices will be the same, and thus increment r
            if prices[r] >= prices[l]:
                ans = max(ans, prices[r] - prices[l])
                r += 1

            # if prices[l] is bigger, it's going to be loss, and thus increment l
            else:
                l += 1
        return ans