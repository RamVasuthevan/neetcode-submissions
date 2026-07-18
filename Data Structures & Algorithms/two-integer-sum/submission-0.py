class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for ind,n in enumerate(nums):
            if target-n in d:
                return sorted([ind,d[target-n]])
            d[n] = ind