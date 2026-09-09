class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_map = {0:1}
        for n in nums:
            current_sum += n
            complement = current_sum - k
            if complement in prefix_map:
                count += prefix_map[complement]
            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
        return count