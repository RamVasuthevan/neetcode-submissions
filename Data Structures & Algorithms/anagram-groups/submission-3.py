from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            key = frozenset(Counter(s).items())
            d[key].append(s)
        
        return list(d.values())