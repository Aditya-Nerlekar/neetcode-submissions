class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        cnt = 1
        maxi = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cnt += 1
            else:
                maxi = max(maxi, cnt)
                cnt = 1  # reset to 1, not 0

        return max(maxi, cnt)
