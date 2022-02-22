class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = [[]]

        def dfs(constructed, remaining):

            if len(constructed) == len(nums):
                return
            for i, num in enumerate(remaining):
                ans.append(constructed + [num])
                dfs(constructed + [num], remaining[i + 1:])

        dfs([], nums)
        return ans