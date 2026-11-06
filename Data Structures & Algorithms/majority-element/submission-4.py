class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        mc, res = 0, 0

        for num in nums:
            c = count.get(num, 0) + 1
            count[num] = c
            if c > mc:
                res = num
                mc = c

        return res