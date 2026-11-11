class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        res = set()

        for num in nums:
            count[num] += 1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                count[nums[i]] -= 1
                count[nums[j]] -= 1

                n = -nums[i] - nums[j]

                if count[n] > 0:
                    res.add(tuple(sorted([nums[i], nums[j], n])))

                count[nums[i]] += 1
                count[nums[j]] += 1

        return [list(x) for x in res]
                

        


