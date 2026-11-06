class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                swap(i, l)
                l += 1
                i += 1

            elif nums[i] == 1:
                i += 1

            else:
                swap(i, r)
                r -= 1

        