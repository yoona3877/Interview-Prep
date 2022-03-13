class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        ch_idx = -1

        # find the last index in which the nums at current index is smaller than the subsequent number.
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                ch_idx = i

        # nums after ch_idx is all in descending order.
        # Find the index of a number that is minimum among all numbers that is greater than nums[ch_idx] after ch_idx
        sec = ch_idx + 1
        for i in range(ch_idx + 1, len(nums)):
            if nums[i] > nums[ch_idx]:
                sec = i

        # If index is found (i.e. original nums array is not in descending order)
        if ch_idx >= 0:
            # swap
            temp = nums[ch_idx]
            nums[ch_idx] = nums[sec]
            nums[sec] = temp

            # after swap, all numbers come after ch_idx need to be sorted.
            l, r = ch_idx + 1, len(nums) - 1
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1
        else: # if the nums are all in descending order, sort nums
            nums.sort()