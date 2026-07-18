from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = defaultdict(list)
        for s in strs:
            D[tuple(sorted(list(s)))].append(s)
        return list(D.values())
        