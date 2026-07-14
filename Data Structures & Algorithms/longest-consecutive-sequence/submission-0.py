class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for n in nums:
            #check if it is the start of a sequence
            if n - 1 not in hashset: #if the num doesn't have eft neigfhbor then it's a start of a sequence
                length = 0
                while (n + length) in hashset:
                    length += 1
                longest = max(length, longest)
        return longest
