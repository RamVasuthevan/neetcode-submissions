from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        C = Counter(nums)
        for key,freq in C.items():
            if freq > 1:
                return True
        return False