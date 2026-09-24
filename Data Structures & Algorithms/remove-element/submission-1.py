class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        a = []
        for n in nums:
            if (n != val):
                a.append(n)
            else:
                continue
        for i in range(len(a)):
            nums[i] = a[i]
        return len(a)
        """
            
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k