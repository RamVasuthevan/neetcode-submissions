class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {val:ind for ind,val in enumerate(nums)}

        for ind,val in enumerate(nums):
            if (target-val) in d and d[(target-val)]!=ind:
                return [ind,d[(target-val)]]

        raise ValueError(f'There is no way to form target={target} by summing two unique values in nums={nums}')