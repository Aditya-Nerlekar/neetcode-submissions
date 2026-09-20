class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        a = defaultdict(list) 
        for s in strs:
            # a[sorted(s)].append(s) 
            # cannot use 'list' as a dict key
            # therefore first create a string from the list then use that as a key
            sortedS = ''.join(sorted(s))
            a[sortedS].append(s)
        return list(a.values())
        """
        res = defaultdict(list)
        for s in strs:
            a = [0] * 26
            for c in s:
                # i = c - "a" # ❌ ERROR: can't subtract strings
                i = ord(c) - ord("a")    # ✅ convert characters to ASCII values
                a[i] += 1
            # res[a].append(s) # ❌ ERROR: list is unhashable, can't be a dict key
            res[tuple(a)].append(s)      # ✅ convert list to tuple so it can be a dict key
        # return res.values() # ❌ ERROR
        return list(res.values())        # ✅ convert dict_values to a list