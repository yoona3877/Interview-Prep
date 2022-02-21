from collections import defaultdict
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hm = defaultdict(int)

        for num in nums:
            hm[num] += 1

        toTuple = []
        for key, val in hm.items():
            toTuple.append((val, key))

        heapq.heapify(toTuple)

        kFrequent = heapq.nlargest(k, toTuple)
        return [tup[1] for tup in kFrequent]

if __name__ == "__main__":
    s = Solution()

    assert s.topKFrequent([1,1,1,2,2,3], 2) == [1,2]