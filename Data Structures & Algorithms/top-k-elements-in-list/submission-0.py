from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        C = Counter(nums)
        return [val for val,count in C.most_common(k)]