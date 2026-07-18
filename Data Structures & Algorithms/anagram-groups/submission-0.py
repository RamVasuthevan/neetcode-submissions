from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = defaultdict(list)
        for s in strs:
            D[frozenset(Counter(s).items())].append(s)
        return list(D.values())
        