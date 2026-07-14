class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter =  defaultdict(int)
        for c in s:
            counter[c] += 1
        for c in t:
            counter[c] -= 1
        for v in counter.values():
            if v != 0:
                return False
        return True
        