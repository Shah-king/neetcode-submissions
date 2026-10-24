class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        l, r = 0, len(height) - 1
        Leftmax, Rightmax = height[l], height[r]
        while l < r:
            if Leftmax < Rightmax:
                l += 1
                Leftmax = max(Leftmax, height[l])
                res += Leftmax - height[l]
            else:
                r -= 1
                Rightmax = max(Rightmax, height[r])
                res += Rightmax - height[r]
        return res
            