class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        if len(intervals) == 0:
            return 0

        count = 0
        intervals.sort(key=lambda x: x[0])

        curr = intervals[0]

        i = 1
        while i < len(intervals):
            if intervals[i][0] < curr[1]:
                count += 1
                if intervals[i][1] < curr[1]:
                    curr = intervals[i]
            else:
                curr = intervals[i]
            i += 1
        return count

