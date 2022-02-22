import heapq
from collections import deque

class Solution(object):

    # Heap solution, Time exceeded
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < k:
            return [max(nums)]

        ans = []
        mem = []

        for i in range(len(nums)):
            heapq.heappush(mem, -1 * nums[i])

            if len(mem) == k:
                ans.append(-1 * heapq.nsmallest(1, mem)[0])
                mem.remove(-1 * nums[i - k + 1])
        return ans

    def maxSlidingWindowQueue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        l, r = 0, 0
        dq = deque()
        ans = []

        while r < len(nums):
            while len(dq) > 0 and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            if l > dq[0]:
                dq.popleft()

            if r + 1 >= k:
                ans.append(nums[dq[0]])
                l += 1
            r += 1
        return ans


