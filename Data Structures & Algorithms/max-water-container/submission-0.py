class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        l, r = 0, len(heights) - 1

        while l < r:
            currVol = (r-l) * min(heights[l], heights[r])
            maxVol = max(maxVol, currVol)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxVol
