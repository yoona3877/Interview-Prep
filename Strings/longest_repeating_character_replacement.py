from collections import defaultdict


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l, r, ans = 0, 0, 0
        hm = defaultdict(int)

        while r < (len(s)):
            hm[s[r]] += 1

            while r - l + 1 - max(hm.values()) > k:
                hm[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)
            r += 1

        return ans