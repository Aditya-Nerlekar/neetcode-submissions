class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix = strs[0]
        # for i in range(1, len(strs)):
        #     j = 0
        #     while j < min(len(prefix), len(strs[i])):
        #         if prefix[j] != strs[i][j]:
        #             break
        #         j += 1
        #     prefix = prefix[:j]
        
        # return prefix
        ######################################################
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i == len(s) or strs[0][i] != s[i]:
        #             return s[:i]
        # return strs[0]   
        #######################################################
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs)
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]

