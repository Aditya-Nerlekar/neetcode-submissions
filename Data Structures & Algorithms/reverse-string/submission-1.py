class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp = []
        for i in range(len(s)-1, -1, -1): #range(start, stop, step)
            temp.append(s[i])
        for i in range(len(s)):
            s[i] = temp[i]

        """
        i, j = 0, len(s) - 1
        while(i < j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        """



        