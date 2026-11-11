class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)
        maxc = 0

        for i in h:
            if i - 1 not in h:
                c = 1

                while i + 1 in h:
                    c += 1
                    i += 1

                maxc = max(maxc, c)

        return maxc
