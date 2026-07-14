class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        res = []
        for n in nums:
            if n in duplicate:
                return True
            duplicate.add(n)
            res.append(n)
        return False
