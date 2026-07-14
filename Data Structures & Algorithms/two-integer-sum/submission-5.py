class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_sum = {}
        for i, j in enumerate(nums):
            complement = target - j
            if complement in new_sum:
                return [new_sum[complement], i]
            new_sum[j] = i
        return new_sum
