class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [1 for i in range(len(nums) + 1)]
        curr_max = 1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    memo[j] = max(memo[j], memo[i] + 1)
                    curr_max = max(memo[j], curr_max)

        return curr_max