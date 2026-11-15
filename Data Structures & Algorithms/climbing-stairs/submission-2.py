class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev, curr = 1, 2
        
        for i in range(n-2):
            temp = curr
            curr = prev + curr
            prev = temp

        return curr


        