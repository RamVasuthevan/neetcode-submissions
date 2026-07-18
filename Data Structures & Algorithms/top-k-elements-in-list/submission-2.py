from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return list(val for val,freq in sorted(list(c.items()), key=lambda tup:tup[1], reverse=True))[:k]
