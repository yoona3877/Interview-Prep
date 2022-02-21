class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))

        ans = [intervals[0]]

        for l, r in intervals[1:]:
            prevL, prevR = ans[-1]
            if prevL <= l and prevR >= r:
                continue
            ans.append([l, r])

        return len(ans)
