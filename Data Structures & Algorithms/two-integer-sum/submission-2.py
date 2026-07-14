class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i, k in enumerate(nums):
            new_num = target - k
            if new_num in hashset:
                return [hashset[new_num], i]
            hashset[k] = i

