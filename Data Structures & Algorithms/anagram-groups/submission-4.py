class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for s in strs:
            num = [0] * 26
            for c in s:
                num[ord(c) - ord('a')]+= 1
            count[tuple(num)].append(s)
        return list(count.values())