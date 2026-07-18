from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        S = set()

        for item in nums:
            if item in S:
                return True
            S.add(item)
        return False