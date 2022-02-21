class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        nums.sort()

        def dfs(constructed, remaining):
            if len(constructed) == len(nums):
                ans.append(constructed)
            prev = None
            for i, num in enumerate(remaining):
                if num != prev:
                    dfs(constructed + [num], remaining[:i] + remaining[i + 1:])
                prev = num

        dfs([], nums)
        return ans

    def permute(self, nums):

        ans = []

        def dfs(constructed, remaining):
            if len(constructed) == len(nums):
                ans.append(constructed)
                return
            for i, num in enumerate(remaining):
                dfs(constructed + [num], remaining[:i], remaining[i+1:])

        dfs([], nums)
        return ans

