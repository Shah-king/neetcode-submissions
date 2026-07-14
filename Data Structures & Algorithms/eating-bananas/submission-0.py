class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) //2 
            total_hour = 0
            for p in piles:
                total_hour += math.ceil(p/ mid)
            if total_hour <= h:
                right = mid
            else:
                left = mid + 1
        return left
