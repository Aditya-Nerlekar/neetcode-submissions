class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        cnt = 1
        maxi = 1

        if not nums:
            return 0

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                cnt += 1
            else:
                if cnt > maxi:
                    maxi = cnt
                cnt = 1
        
        return max(maxi,cnt)