class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights) - 1
        l, r = 0, n

        maxv = 0

        while l <= r:
            vol = min(heights[r],heights[l]) * abs(r-l)
            maxv = max(maxv, vol)

            if heights[l] <= heights[r]:
                l += 1

            elif heights[l] > heights[r]:
                r -= 1

        
        return maxv