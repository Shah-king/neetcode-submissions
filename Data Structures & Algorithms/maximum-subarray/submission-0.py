class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]
        for n in nums[1:]:
            curr_sum = max(n, curr_sum + n)
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
        