class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # left sorted (i.e. pivot on the right)
            # [4,5,6,7,1,2,3]
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:  # nums[l] <= target <= nums[m]
                    r = m - 1
            # right sorted (i.e. pivot on the left)
            # [6,7,1,2,3,4,5]
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1