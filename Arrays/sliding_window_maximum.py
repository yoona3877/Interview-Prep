from collections import deque


class Solution(object):
    """
    Use deque for storing the maximum.
    The deque will store the index of element in nums
    dq[0] will always be the maximum of the current sliding window.

    """
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l, r, ans = 0,0, []
        dq = deque()

        while r < len(nums):
            # pop the elements in dq if it's smaller than the current element
            while len(dq) > 0 and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            # if dq[0] is out of bound of sliding window, pop the element
            if l > dq[0]:
                dq.popleft()

            # Check if the the current right-index is greater than k.
            # only update left pointer if this conditions satisfied.
            if r+ 1 >= k:
                ans.append(nums[dq[0]])
                l +=1
            r +=1
        return ans
