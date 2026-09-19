class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list) 
        for s in strs:
            # a[sorted(s)].append(s) 
            # cannot use 'list' as a dict key
            # therefore first create a string from the list then use that as a key
            sortedS = ''.join(sorted(s))
            a[sortedS].append(s)
        return list(a.values())
            