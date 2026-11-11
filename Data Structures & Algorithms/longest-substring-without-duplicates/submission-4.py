class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        l = 0
        maxl = 0

        for r in range(len(s)):
            if s[r] in h:
                l = max(h[s[r]] + 1, l)

            h[s[r]] = r
            maxl = max(maxl, r - l + 1)

        return maxl
