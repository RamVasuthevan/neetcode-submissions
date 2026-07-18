from itertools import accumulate 
import operator

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = accumulate(nums[:-1],operator.mul,initial=1)
        suffix = list(accumulate(reversed(nums[1:]),operator.mul,initial=1))[::-1]
        return [p*s for p,s in zip(prefix,suffix)]
        