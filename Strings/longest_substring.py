class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, start_idx, hm = 0, 0, {}

        for i, c in enumerate(s):
            if c in hm:
                if hm[c] < start_idx:
                    hm[c] = i
                else:
                    ans = max(ans, i - start_idx)
                    start_idx = hm[c] + 1
                    hm[c] = i
            else:
                hm[c] = i
        ans = max(ans, len(s) - start_idx)
        return ans

    def lengthOfLongestSubstringPointers(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r, ans = 0, 0, 0

        hm = {}

        while r < len(s):
            c = s[r]
            if c in hm:
                if hm[c] < l:
                    hm[c] = r
                else:
                    ans = max(ans, r - l)
                    l = hm[c] + 1
                    hm[c] = r
            else:
                hm[c] = r
            r += 1
        ans = max(ans, len(s) - l)
        return ans