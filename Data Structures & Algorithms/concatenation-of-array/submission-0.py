class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        m = len(nums) 
        num = [0] * (2*m)
        for i in range(m):
            num[i + m] = num[i] = nums[i]

        return num