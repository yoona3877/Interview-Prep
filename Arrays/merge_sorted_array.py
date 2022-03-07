class Solution(object):
    """
    Merge two sorted array.
    BUT do not return anything. Rather, change the nums1.
    num1 contains nums1 element followed by 0's with the length n.
    """
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        f, s = m - 1, n - 1
        p = len(nums1) - 1
        while f >= 0 and s >= 0:
            if nums1[f] > nums2[s]:
                nums1[p] = nums1[f]
                f -= 1
            else:
                nums1[p] = nums2[s]
                s -= 1
            p -= 1

        # If f != -1, you don't need to do anything because it's already filled out.
        # Only when s != -1, you need to do extra.
        if s != -1:
            # Since the current s position is not included in nums1, you need to include it by s + 1
            nums1[:s + 1] = nums2[:s + 1]

